import cv2
import numpy as np
import face_recognition as fr
import os
import random
from datetime import datetime

#Accedemos a la carpeta
path = "src/fotos"
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

def codrostros(images):
    listacod = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cod = fr.face_encodings(img)[0]
        listacod.append(cod)

    return listacod

def horario(nombre):
    with open("src/attendance.csv","r+") as h:
        data = h.readline()
        listanombres = []

        for line in data:
            entrada = line.split(",")
            listanombres.append(entrada[0])

        if nombre not in listanombres:
            info = datetime.now()
            fecha = info.strftime("%Y:%m:%d")
            hora = info.strftime("%H:%M:%S")

            h.writelines(f"\n{nombre},{fecha},{hora}")
            print(info)

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