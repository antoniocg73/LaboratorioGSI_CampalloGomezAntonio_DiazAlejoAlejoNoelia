from tkinter import *
from tkinter import PhotoImage, messagebox
from tkinter.ttk import Combobox
import webbrowser
import re


class InterfazAplicacion:

    # Imágenes
    imagenLogo = "archivosExternos/LogoESINoFondo.png"
    imagenUsuario = "archivosExternos/usuarioLogin.png"
    imagenContrasena = "archivosExternos/contrasenaLogin.png"

    def __init__(self):

        #Configuración de la ventana
        self.ventana = Tk()
        self.ventana.title("ESI-Recommendations")
        self.ventana.geometry("820x1000")
        self.ventana.resizable(False, False)


        #Definición frame Login
        self.frameLogin = Frame(height=920, width=850, bg = '#81C2AE')
        self.frameLogin.pack(fill=BOTH, expand=True)

        #imagenes
        self.loginLogoImagen = PhotoImage(file=self.imagenLogo)
        self.lblLoginLogoImagen = Label(self.frameLogin, image=self.loginLogoImagen)
        self.lblLoginLogoImagen.config(width=300, height=300, bg = '#81C2AE')
        self.lblLoginLogoImagen.place(x=410, y=150, anchor=CENTER)

        self.loginUsuarioImagen = PhotoImage(file=self.imagenUsuario)
        self.lblLoginUsuarioImagen = Label(self.frameLogin, image=self.loginUsuarioImagen)
        self.lblLoginUsuarioImagen.config(width=100, height=00, bg = '#81C2AE')
        self.lblLoginUsuarioImagen.place(x=200, y=362, anchor=CENTER)

        self.loginContrasenaImagen = PhotoImage(file=self.imagenContrasena)
        self.lblLoginContrasenaImagen = Label(self.frameLogin, image=self.loginContrasenaImagen)
        self.lblLoginContrasenaImagen.config(width=100, height=00, bg = '#81C2AE')
        self.lblLoginContrasenaImagen.place(x=200, y=512, anchor=CENTER)

        #botones del login
        self.botonRegistro = Button(self.frameLogin,text="Registrarse",fg="black", width=20, command=self.registrar_usuario)
        self.botonRegistro.place(x=230 ,y=650)        
        self.botonAutenticarse = Button(self.frameLogin, text="Autenticarse", fg="black", width=20, command=self.verificar_credenciales)
        self.botonAutenticarse.place(x=450 ,y=650)
        
        #labels del login
        self.lblUsuario = Label(self.frameLogin, text="Usuario", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblUsuario.place(x=230 ,y=300)
        self.lblContrasena = Label(self.frameLogin, text="Contraseña", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblContrasena.place(x=230 ,y=450)

        #texto del login
        self.txtLogin=Entry(self.frameLogin, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtLogin.place(x=230 ,y=350)
        self.txtContrasena=Entry(self.frameLogin, justify=LEFT, width=33, font=('Comic Sans', 14), show="*")
        self.txtContrasena.place(x=230 ,y=500)
        
        self.ventana.mainloop()


    def registrar_usuario(self):

        #Definición frame Registrar
        self.frameRegistrar = Frame(self.frameLogin, bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        self.frameRegistrar.place(x=130, y=40, width=550, height=660)
        
        #botones del registrar
        self.botonRegistro = Button(self.frameRegistrar, text="Registro", fg="black", width=25, command=self.registrar_nuevo_usuario)
        self.botonRegistro.place(x=315 ,y=570)
        
        #labels del registrar
        self.lblDatos = Label(self.frameRegistrar, text="Datos", font=("Comic Sans",20), fg="white", background="#81C2AE")
        self.lblDatos.place(x=50 ,y=30)

        self.lblUsuario = Label(self.frameRegistrar, text="Usuario", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblUsuario.place(x=50 ,y=100)
        self.lblContrasena = Label(self.frameRegistrar, text="Contraseña", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblContrasena.place(x=20 ,y=180)
        self.lblNombre = Label(self.frameRegistrar, text="Nombre", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblNombre.place(x=50 ,y=260)
        self.lblApellido = Label(self.frameRegistrar, text="Apellido", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblApellido.place(x=50 ,y=340)
        self.lblDNI = Label(self.frameRegistrar, text="DNI", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblDNI.place(x=80 ,y=420)
        self.lblTelefono = Label(self.frameRegistrar, text="Telefono", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblTelefono.place(x=40 ,y=500)

        #texto del registrar
        self.txtLogin=Entry(self.frameRegistrar, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtLogin.place(x=130 ,y=100)
        self.txtContrasena=Entry(self.frameRegistrar, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtContrasena.place(x=130 ,y=180)
        self.txtNombre=Entry(self.frameRegistrar, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtNombre.place(x=130 ,y=260)
        self.txtApellido=Entry(self.frameRegistrar, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtApellido.place(x=130 ,y=340)
        self.txtDNI=Entry(self.frameRegistrar, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtDNI.place(x=130 ,y=420)
        self.txtTelefono=Entry(self.frameRegistrar, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtTelefono.place(x=130 ,y=500)

 
    def verificar_credenciales(self):

        #Definición frame Perfil
        self.framePerfil = Frame(self.frameLogin, bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        self.framePerfil.place(x=50, y=50, width=550, height=640)

        #botones del perfil
        self.botonCambiarContrasena = Button(self.framePerfil, text="Cambiar contraseña", fg="black", width=25)
        self.botonCambiarContrasena.place(x=312 ,y=550)

        self.botonCalificaciones = Button(self.frameLogin, text="Calificaciones", fg="black", width=25)
        self.botonCalificaciones.place(x=620 ,y=100)
        self.botonGustos = Button(self.frameLogin, text="Gustos", fg="black", width=25)
        self.botonGustos.place(x=620 ,y=150)
        self.botonFormulario = Button(self.frameLogin, text="Formulario", fg="black", width=25)
        self.botonFormulario.place(x=620 ,y=650)

        #labels del perfil        
        self.lblUsuario = Label(self.framePerfil, text="Usuario", font=("Comic Sans",20), fg="white", background="#81C2AE")
        self.lblUsuario.place(x=50 ,y=50)

        self.lblNombre = Label(self.framePerfil, text="Nombre", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblNombre.place(x=50 ,y=150)
        self.lblApellido = Label(self.framePerfil, text="Apellido", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblApellido.place(x=50 ,y=250)
        self.lblDNI = Label(self.framePerfil, text="DNI", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblDNI.place(x=85 ,y=350)
        self.lblTelefono = Label(self.framePerfil, text="Telefono", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblTelefono.place(x=40 ,y=450)

        #texto del perfil
        self.txtNombre=Entry(self.framePerfil, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtNombre.place(x=130 ,y=150)
        self.txtApellido=Entry(self.framePerfil, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtApellido.place(x=130 ,y=250)
        self.txtDNI=Entry(self.framePerfil, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtDNI.place(x=130 ,y=350)
        self.txtTelefono=Entry(self.framePerfil, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtTelefono.place(x=130 ,y=450)


    def registrar_nuevo_usuario(self):
        self.frameRegistrar.place_forget()
        self.frameLogin.place(x=0, y=0)
