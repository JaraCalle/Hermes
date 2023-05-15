# Importaciones
import interfaz.registro as gui
import customtkinter as ctk
import interfaz.face as face
import os
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

# Modo de color y tema
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme(os.path.join(carpeta_temas,"dark-blue.json"))

class Index:
    def __init__(self):
        # Creación de la ventana principal
        self.root = ctk.CTk()
        self.root.title("Hermes - Sistema de reconocimiento facial")
        self.root.iconbitmap(os.path.join(carpeta_imagenes, "logo.ico"))
        self.root.geometry("450x300")
        self.root.resizable(False,False)

        # Contenido de la ventana principal
        # Logo
        logo = ctk.CTkImage(
            light_image = (Image.open(os.path.join(carpeta_imagenes, "logo.png"))),
            dark_image = (Image.open(os.path.join(carpeta_imagenes, "logo.png"))),
            size = (250,150)
        ) 

        # Etiqueta para mostrar la imagen
        etiqueta = ctk.CTkLabel(master = self.root,
                                image=logo,
                                text="")
        etiqueta.pack(pady=15)

        # Botón registro
        ctk.CTkButton(self.root, text="Registrar persona", command=self.btn_registro).pack()

        # Botón toma asistencia
        ctk.CTkButton(self.root, text="Tomar asistencia", command=self.btn_asistencia).pack(pady=25)


        # Bucle de ejecución
        self.root.mainloop()

    # Función para el botón "registrar persona" 
    def btn_registro(self):
        # Destuir ventana principal
        self.root.destroy()
        # Instanciación de la ventana registro
        ventana_registro = gui.Registro()

    # Función para el botón "tomar asistencia"
    def btn_asistencia(self):
        # Destruir ventana principal
        self.root.destroy()
        # Instanciación de la ventana asistencia
        ventana_asistencia = Asistencia()


class Asistencia:
    # Boton volver atrás
    def btn_volver_atras(self):
        # Destuir ventana principal
        self.root.destroy()
        # Instanciación de la ventana registro
        ventana_index = Index()

    def __init__(self):
        # Creación de la ventana principal
        self.root = ctk.CTk()
        self.root.title("Hermes - Toma de asistencia")
        self.root.iconbitmap(os.path.join(carpeta_imagenes, "logo.ico"))
        self.root.geometry("450x300")
        self.root.resizable(False,False)
        
        # Contenido de la ventana
        # Frame principal
        self.frame = ctk.CTkFrame(master=self.root, width=400, height=250)
        self.frame.grid(row=0, column=0, padx= 20, pady=20, sticky="nsew")
        #Frame del centro
        self.right_frame = ctk.CTkFrame(master=self.root)
        self.right_frame.grid(row=1, column=1, sticky="nsew")

        # Botón de volver atrás
        self.icon = ctk.CTkImage(Image.open(os.path.join(carpeta_imagenes, "volver.png")))
        ctk.CTkButton(self.frame, image=self.icon, text="",corner_radius=50, width=32, height=32, command=self.btn_volver_atras).grid(row=0, column=0)

        # Contenido del centro
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
        self.nombre_entry = ctk.CTkEntry(master=self.form_frame, placeholder_text="Nombre de la clase")
        self.nombre_entry.grid(row=0, column=0)
        # Botón de enviar formulario
        ctk.CTkButton(self.right_frame, text="Comenzar toma de asistencia", command=face.main).grid(row=2, column=0, pady=10)

        

        # Contenido de la ventana
        self.root.mainloop()