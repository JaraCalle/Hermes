# Importaciones
import interfaz.registro as gui
import customtkinter as ctk
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
    def __init__(self):
        # Creación de la ventana principal
        self.root = ctk.CTk()
        self.root.title("Hermes - Toma de asistencia")
        self.root.iconbitmap(os.path.join(carpeta_imagenes, "logo.ico"))
        self.root.geometry("450x300")
        self.root.resizable(False,False)

        # Contenido de la ventana
        self.root.mainloop()