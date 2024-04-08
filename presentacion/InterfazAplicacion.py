from tkinter import *
from tkinter import PhotoImage, messagebox
from tkinter.ttk import Combobox
import webbrowser
import re


class InterfazAplicacion:

    def __init__(self):
        
        #Configuración de la ventana
        self.ventana = Tk()
        self.ventana.title("Gestión de TuriStatSP")
        self.ventana.geometry("1000x1000")
        self.ventana.resizable(False, False)
        self.valor_seleccion = IntVar(value=0) 