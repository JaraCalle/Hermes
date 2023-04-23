# Importaciones
import interfaz.index as gui
import customtkinter as ctk
from tkinter import *
import os
import cv2 
from cv2 import *
from PIL import ImageTk, Image

# Configuraciones globales para la aplicación

# --> Rutas
# Carpeta principal
carpeta_principal = os.path.dirname(__file__)
#.\Hermes\interfaz
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
#.\Hermes\interfaz\imagenes
carpeta_temas = os.path.join(carpeta_principal,"temas")
#.\Hermes\interfaz\temas
carpeta_fotos = os.path.join(carpeta_principal,"fotos")
#.\Hermes\interfaz\fotos

# Modo de color y tema
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme(os.path.join(carpeta_temas,"dark-blue.json"))

class Registro:
    # Cámara en vivo
    def video_stream(self):
        _, frame = cap.read()
        resize = cv2.resize(frame, (262, 210))
        cv2image = cv2.cvtColor(resize, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        imgtk = ImageTk.PhotoImage(image=img)
        self.cam_vivo.imgtk = imgtk
        self.cam_vivo.configure(image=imgtk)
        self.cam_vivo.after(10, self.video_stream)
    
    # Boton volver atrás
    def btn_volver_atras(self):
        # Destuir ventana principal
        self.root.destroy()
        # Instanciación de la ventana registro
        ventana_index = gui.Index()
    
    def __init__(self):
        # Creación de la ventana principal
        self.root = ctk.CTk()
        self.root.title("Hermes - Formulario de registro")
        self.root.iconbitmap(os.path.join(carpeta_imagenes, "logo.ico"))
        self.root.geometry("550x350")
        self.root.resizable(False,False)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Contenido de la ventana
        # Frame izquierdo
        self.left_frame = ctk.CTkFrame(master=self.root, width=300)
        self.left_frame.grid(row=0, column=0, padx= 20, pady=20, sticky="nsew")

        #Frame derecho
        self.right_frame = ctk.CTkFrame(master=self.root)
        self.right_frame.grid(row=0, column=1, padx= 20, pady=20, sticky="nsew")
        
        # Contenido del frame derecho
        # Frame superior del interior
        self.titulo_frame = ctk.CTkFrame(master=self.right_frame)
        self.titulo_frame.grid(row=0, column=0, padx=40, pady=10)
        # -> Titulos
        self.titulo = ctk.CTkLabel(self.titulo_frame, text="Hermes",font=("CTkFont",  20))
        self.titulo.grid(row=0, column=0, pady=0)
        self.titulo = ctk.CTkLabel(self.titulo_frame, text="Sistema de reconocimiento facial")
        self.titulo.grid(row=1, column=0)
        # Frame centro del interior
        self.form_frame = ctk.CTkFrame(master=self.right_frame)
        self.form_frame.grid(row=1, column=0, pady=30)
        # -> Formulario
        # --> Nombre
        self.nombre_entry = ctk.CTkEntry(master=self.form_frame, placeholder_text="Nombre")
        self.nombre_entry.grid(row=0, column=0)
        # --> Apellido
        self.apellido_entry = ctk.CTkEntry(master=self.form_frame, placeholder_text="Apellido")
        self.apellido_entry.grid(row=1, column=0, pady=15)
        # --> Numero de identificación
        self.id_entry = ctk.CTkEntry(master=self.form_frame, placeholder_text="Número de ID")
        self.id_entry.grid(row=2, column=0)
        # Botón de enviar formulario
        ctk.CTkButton(self.right_frame, text="Tomar foto", command=self.btn_tomar_fot).grid(row=3, column=0, pady=10)

        # Contenido del frame izquierdo
        # Botón de volver atrás
        self.icon = ctk.CTkImage(Image.open(os.path.join(carpeta_imagenes, "volver.png")))
        ctk.CTkButton(self.left_frame, image=self.icon, text="",corner_radius=50, width=32, height=32, command=self.btn_volver_atras).grid(row=0, column=0)
        ctk.CTkLabel(master=self.left_frame, text="").grid(row=1, column=1, padx=80)

        # Cámara de video en vivo
        self.cam_vivo  = Label(self.left_frame)
        self.cam_vivo.place(relx=.5, rely=.5,anchor= CENTER)
        self.cam_vivo.config(width="225", height="200")
        global cap
        cap = cv2.VideoCapture(0)

        self.video_stream()
        self.root.mainloop()
    
    # Boton tomar foto
    def btn_tomar_fot(self):
        # Datos del formulario
        nombre = self.nombre_entry.get().replace(" ", "_")
        apellido = self.apellido_entry.get().replace(" ", "_")
        nit = self.id_entry.get().replace(" ", "_")

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
                cv2.imwrite(os.path.join(carpeta_fotos,f"{nombre}_{apellido}-{nit}.png"), image)
                # limpia el formulario
                self.nombre_entry.delete(0, END)
                self.apellido_entry.delete(0, END)
                self.id_entry.delete(0, END)
            else:
                print("No se detectó ninguna cámara para poder tomar la foto bro... :c")
