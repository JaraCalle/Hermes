import cv2
import numpy as np
import face_recognition as fr
import os
import random
from datetime import datetime

carpeta_principal = os.path.dirname(__file__)
carpeta_fotos = os.path.join(carpeta_principal,"fotos")
carpeta_src= os.path.join(carpeta_principal,"src")
archivo_csv= os.path.join(carpeta_src,"attendance.csv")

def codrostros(images):
    listacod = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cod = fr.face_encodings(img)[0]
        listacod.append(cod)

    return listacod

def horario(nombre):
    with open(archivo_csv,"r+") as h:
        data = h.readline()
        listanombres = []
        cambio= "si"

        while data:
            entrada = data.split(",")
            listanombres.append(entrada[0])
            data= h.readline()

        for a in listanombres:
            if nombre==a:
                cambio= "no"
            

        if cambio=="si":
            info = datetime.now()
            fecha = info.strftime("%Y:%m:%d")
            hora = info.strftime("%H:%M:%S")

            h.writelines(f"\n{nombre},{fecha},{hora}")
            print(info)
def main():
    #Accedemos a la carpeta
    path = carpeta_fotos
    images = []
    clases = []
    lista = os.listdir(path)
    print(lista)

    comp1 = 100

    for lis in lista:
        imgdb = cv2.imread(f"{path}/{lis}")
        images.append(imgdb)
        clases.append(os.path.splitext(lis)[0])

    print(clases)

    rostrocod = codrostros(images)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        frame2 = cv2.resize(frame, (0, 0), None, 0.25, 0.25)

        rgb = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

        faces = fr.face_locations(rgb)
        facescod = fr.face_encodings(rgb, faces)

        for facecod, faceloc in zip(facescod, faces):
            comparacion = fr.compare_faces(rostrocod, facecod)

            simi = fr.face_distance(rostrocod, facecod)

            min = np.argmin(simi)

            if comparacion[min]:
                nombre = clases[min].upper()
                print(nombre)

                yi, xf, yf, xi = faceloc

                yi, xf, yf, xi = yi*4, xf*4, yf*4, xi*4

                indice = comparacion.index(True)

                if comp1 != indice:
                    r = random.randrange(0, 255, 50)
                    g = random.randrange(0, 255, 50)
                    b = random.randrange(0, 255, 50)

                    comp1 = indice
                
                if comp1 == indice:
                    cv2.rectangle(frame, (xi, yi), (xf, yf), (r, g, b), 3)
                    cv2.rectangle(frame, (xi, yf-35), (xf, yf), (r, g, b), cv2.FILLED)
                    cv2.putText(frame, nombre, (xi+6, yf-6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                    horario(nombre)

        cv2.imshow("Reconocimiento Facial", frame)

        t = cv2.waitKey(5)
        if t == 27:
            break