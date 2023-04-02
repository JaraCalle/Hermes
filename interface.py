from tkinter import *
from PIL import ImageTk, Image
import cv2 
from cv2 import *
import numpy as np
import face_recognition as fr
import os
import random
from datetime import datetime

def app_definition():    

    # Cámara en vivo
    def video_stream():
        _, frame = cap.read()
        resize = cv2.resize(frame, (262, 210))
        cv2image = cv2.cvtColor(resize, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        imgtk = ImageTk.PhotoImage(image=img)
        cam_vivo.imgtk = imgtk
        cam_vivo.configure(image=imgtk)
        cam_vivo.after(10, video_stream)

    root = Tk()
    
    # Configuración de la ventana
    root.title("Hermes")
    root.resizable(False, False)
    frame1 = create_frames("left")
    frame2 = create_frames("right")
    
    # Imagen de fondo
    #bg = PhotoImage(file = "src/images/background.png")
    #foto_bg = Label(frame1, image=bg)
    #foto_bg.place(x=0, y=0, relwidth=1, relheight=1)

    # Título del frame
    titulo = Label(frame2, text="Hermes", font=("Arial", 20)).place(relx=.5, rely=.05,anchor= CENTER)
    titulo = Label(frame2, text="Sistema de reconocimiento facial", font=("Arial", 10)).place(relx=.5, rely=.1,anchor= CENTER)
    

    # Cámara de video en vivo
    cam_vivo  =Label(frame1)
    cam_vivo.place(relx=.5, rely=.5,anchor= CENTER)
    cam_vivo.config(width="225", height="200")
    global cap
    cap = cv2.VideoCapture(0)

    # Formulario para registrar a una persona
    nom_label = Label(frame2, text="Nombre", font=("Arial", 10)).place(relx=.5, rely=.25,anchor= CENTER)
    global nom_entry 
    nom_entry = Entry(frame2)
    nom_entry.place(relx=.5, rely=.3,anchor= CENTER)

    apellido_label = Label(frame2, text="Apellidos", font=("Arial", 10)).place(relx=.5, rely=.45,anchor= CENTER)
    global apellido_entry 
    apellido_entry = Entry(frame2)
    apellido_entry.place(relx=.5, rely=.5,anchor= CENTER)

    nit_label = Label(frame2, text="Documento de identidad", font=("Arial", 10)).place(relx=.5, rely=.65,anchor= CENTER)
    global nit_entry 
    nit_entry = Entry(frame2)
    nit_entry.place(relx=.5, rely=.7,anchor= CENTER)

    button = Button(frame2, text="Registrar", command=take_picture)
    button.place(relx=.5, rely=.8,anchor= CENTER)

    video_stream()
    root.mainloop()

# Función para crear los frames laterales
def create_frames(pos):
    miframe=Frame()
    miframe.pack(side = pos, fill="y")
    miframe.config(width="500", height="450")
    return miframe

def take_picture():

    # Datos del formulario
    nombre = nom_entry.get().replace(" ", "_")
    apellido = apellido_entry.get().replace(" ", "_")
    nit = nit_entry.get().replace(" ", "_")

    # Comprobar que no me vayan a dejar nada vacío :/
    if nombre == "" or apellido == "" or nit == "":
        print("No se puede dejar ningún campo vacío")
        return
    else:
        # leer la camara
        result, image = cap.read()
        
        # Si todo salio bien :D
        if result:

            # Mostrar la foto
            cv2.imshow(f"{nombre}_{apellido}", image)
        
            # Guardar la foto
            cv2.imwrite(f"src/fotos/{nombre}_{apellido}-{nit}.png", image)

            # limpia el formulario
            nom_entry.delete(0, END)
            apellido_entry.delete(0, END)
            nit_entry.delete(0, END)

        else:
            print("No se detectó ninguna cámara para poder tomar la foto bro... :c")
