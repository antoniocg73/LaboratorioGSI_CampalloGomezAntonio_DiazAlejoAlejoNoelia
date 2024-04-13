from tkinter import *
from tkinter import PhotoImage, messagebox
from tkinter.ttk import Combobox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from presentacion.InterfazCambiarContrasena import InterfazCambiarContrasena
from dominio.login import Login
from dominio.registro import Registro
from dominio.perfil import Perfil
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
        self.frameLogin.place(x=0, y=0)

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
        self.botonRegistro = Button(self.frameLogin,text="Registrarse",fg="black", width=20, command=self.initMenuRegistrar)
        self.botonRegistro.place(x=230 ,y=650)        
        self.botonAutenticarse = Button(self.frameLogin, text="Autenticarse", fg="black", width=20, command=self.verificarCredenciales)
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
        
        









        #Definición frame Perfil
        self.framePerfil = Frame(bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2, height=920, width=850)
        self.framePerfil.place(x=0, y=0)
        self.framePerfilDatos = Frame(self.framePerfil, bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2, width=550, height=640)
        self.framePerfilDatos.place(x=50, y=50)

        #botones del perfil
        self.botonCambiarContrasena = Button(self.framePerfilDatos, text="Cambiar contraseña", fg="black", width=25, command=self.initMenuCambiarContrasena)
        self.botonCambiarContrasena.place(x=312 ,y=550)
        self.botonCerrarSesion = Button(self.framePerfilDatos, text="Cerrar sesión", fg="black", width=25, command=self.initMenuLogin)
        self.botonCerrarSesion.place(x=50 ,y=550)

        self.botonCalificaciones = Button(self.framePerfil, text="Calificaciones", fg="black", width=25, command=self.initMenuCalificaciones)
        self.botonCalificaciones.place(x=620 ,y=100)
        self.botonGustos = Button(self.framePerfil, text="Ver gustos", fg="black", width=25, command=self.initMenuGustos)
        self.botonGustos.place(x=620 ,y=150)
        self.botonFormulario = Button(self.framePerfil, text="Formulario", fg="black", width=25, command=self.initMenuFormulario)
        self.botonFormulario.place(x=620 ,y=600)
        self.botonObtenerRecomendaciones = Button(self.framePerfil, text="Obtener recomendaciones", fg="black", width=25, command=self.obtenerRecomendaciones)
        self.botonObtenerRecomendaciones.place(x=620 ,y=650)

        #labels del perfil        
        self.lblUsuario = Label(self.framePerfilDatos, text="Usuario", font=("Comic Sans",20), fg="white", background="#81C2AE")
        self.lblUsuario.place(x=50 ,y=50)

        self.lblNombre = Label(self.framePerfilDatos, text="Nombre", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblNombre.place(x=50 ,y=150)
        self.lblApellido = Label(self.framePerfilDatos, text="Apellido", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblApellido.place(x=50 ,y=250)
        self.lblDNI = Label(self.framePerfilDatos, text="DNI", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblDNI.place(x=85 ,y=350)
        self.lblTelefono = Label(self.framePerfilDatos, text="Telefono", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblTelefono.place(x=40 ,y=450)

        #texto del perfil
        self.txtNombre=Entry(self.framePerfilDatos, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtNombre.place(x=130 ,y=150)
        self.txtApellido=Entry(self.framePerfilDatos, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtApellido.place(x=130 ,y=250)
        self.txtDNI=Entry(self.framePerfilDatos, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtDNI.place(x=130 ,y=350)
        self.txtTelefono=Entry(self.framePerfilDatos, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtTelefono.place(x=130 ,y=450)










        #Definición frame Registrar
        self.frameRegistrar = Frame(bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2, height=920, width=850)
        self.frameRegistrar.place(x=0, y=0)
        self.frameRegistrarDatos = Frame(self.frameRegistrar, bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2, width=550, height=570)
        self.frameRegistrarDatos.place(x=130, y=40)

        #botones del registrar
        self.botonRegistro = Button(self.frameRegistrar, text="Registro", fg="black", width=25, command=self.registrarUsuario)
        self.botonRegistro.place(x=180 ,y=670)
        self.botonVolver = Button(self.frameRegistrar, text="Volver", fg="black", width=25, command=self.initMenuLogin)
        self.botonVolver.place(x=450 ,y=670)
        
        #labels del registrar
        self.lblDatos = Label(self.frameRegistrarDatos, text="Datos", font=("Comic Sans",20), fg="white", background="#81C2AE")
        self.lblDatos.place(x=50 ,y=30)

        self.lblUsuario = Label(self.frameRegistrarDatos, text="Usuario", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblUsuario.place(x=50 ,y=100)
        self.lblContrasena = Label(self.frameRegistrarDatos, text="Contraseña", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblContrasena.place(x=20 ,y=180)
        self.lblNombre = Label(self.frameRegistrarDatos, text="Nombre", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblNombre.place(x=50 ,y=260)
        self.lblApellido = Label(self.frameRegistrarDatos, text="Apellido", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblApellido.place(x=50 ,y=340)
        self.lblDNI = Label(self.frameRegistrarDatos, text="DNI", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblDNI.place(x=80 ,y=420)
        self.lblTelefono = Label(self.frameRegistrarDatos, text="Telefono", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblTelefono.place(x=40 ,y=500)

        #texto del registrar
        self.txtLoginRegistro=Entry(self.frameRegistrarDatos, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtLoginRegistro.place(x=130 ,y=100)
        self.txtContrasenaRegistro=Entry(self.frameRegistrarDatos, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtContrasenaRegistro.place(x=130 ,y=180)
        self.txtNombreRegistro=Entry(self.frameRegistrarDatos, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtNombreRegistro.place(x=130 ,y=260)
        self.txtApellidoRegistro=Entry(self.frameRegistrarDatos, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtApellidoRegistro.place(x=130 ,y=340)
        self.txtDNIRegistro=Entry(self.frameRegistrarDatos, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtDNIRegistro.place(x=130 ,y=420)
        self.txtTelefonoRegistro=Entry(self.frameRegistrarDatos, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtTelefonoRegistro.place(x=130 ,y=500)













         #Definición frames de Calificaciones
        self.frameCalificaciones = Frame(bg = '#81C2AE', height=920, width=850)
        self.frameCalificaciones.place(x=0, y=0)

        self.frameComputacion = Frame(self.frameCalificaciones, bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        self.frameComputacion.place(x=50, y=50, width=350, height=300)
        self.frameComputadores = Frame(self.frameCalificaciones, bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        self.frameComputadores.place(x=420, y=50, width=350, height=300)
        self.frameTI = Frame(self.frameCalificaciones, bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        self.frameTI.place(x=50, y=370, width=350, height=300)
        self.frameIngSoftware = Frame(self.frameCalificaciones, bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        self.frameIngSoftware.place(x=420, y=370, width=350, height=300)

        #botones de calificaciones
        self.botonActualizarCalificaciones = Button(self.frameCalificaciones, text="Actualizar notas", fg="black", width=25, command=self.actualizarCalificaciones)
        self.botonActualizarCalificaciones.place(x=350 ,y=710)
        self.botonVolverCalificaciones = Button(self.frameCalificaciones, text="Volver al perfil", fg="black", width=25, command=self.initMenuPerfil)
        self.botonVolverCalificaciones.place(x=585 ,y=710)
        self.botonConfirmarCalificaciones = Button(self.frameCalificaciones, text="Confirmar", fg="black", width=25, command=self.confirmarCalificaciones)
        self.botonConfirmarCalificaciones.place(x=115 ,y=710)
        self.botonConfirmarCalificaciones.config(state=DISABLED)

        #labels de calificaciones       
        self.lblComputacion = Label(self.frameComputacion, text="Computación", font=("Comic Sans",15), fg="white", background="#81C2AE")
        self.lblComputacion.place(x=20 ,y=20)
        self.lblComputadores = Label(self.frameComputadores, text="Computadores", font=("Comic Sans",15), fg="white", background="#81C2AE")
        self.lblComputadores.place(x=20 ,y=20)
        self.lblTI = Label(self.frameTI, text="Tecnología Información", font=("Comic Sans",15), fg="white", background="#81C2AE")
        self.lblTI.place(x=20 ,y=20)
        self.lblIngSoftware = Label(self.frameIngSoftware, text="Ingeniería del Software", font=("Comic Sans",15), fg="white", background="#81C2AE")
        self.lblIngSoftware.place(x=20 ,y=20)

        #labels de computacion
        self.lblEDA = Label(self.frameComputacion, text="EDA", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblEDA.place(x=40 ,y=80)
        self.lblSI = Label(self.frameComputacion, text="SI", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblSI.place(x=50 ,y=150)
        self.lblLogica = Label(self.frameComputacion, text="Lógica", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblLogica.place(x=30 ,y=220)
        self.lblAlgebra = Label(self.frameComputacion, text="Álgebra", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblAlgebra.place(x=190 ,y=80)
        self.lblMetodologia = Label(self.frameComputacion, text="Metodología", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblMetodologia.place(x=165,y=150)

        #labels de computadores
        self.lblSSOO = Label(self.frameComputadores, text="SSOO", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblSSOO.place(x=40 ,y=80)
        self.lblPCTR = Label(self.frameComputadores, text="PCTR", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblPCTR.place(x=40 ,y=130)
        self.lblTECO = Label(self.frameComputadores, text="TECO", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblTECO.place(x=40 ,y=180)
        self.lblECO = Label(self.frameComputadores, text="ECO", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblECO.place(x=45 ,y=230)
        self.lblORCO = Label(self.frameComputadores, text="ORCO", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblORCO.place(x=190,y=80)
        self.lblARCO = Label(self.frameComputadores, text="ARCO", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblARCO.place(x=190 ,y=130)
        self.lblSSDD = Label(self.frameComputadores, text="SSDD", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblSSDD.place(x=190,y=180)

        #labels de ingenieria del software
        self.lblISOI = Label(self.frameIngSoftware, text="ISOI", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblISOI.place(x=45 ,y=80)
        self.lblISOII = Label(self.frameIngSoftware, text="ISOII", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblISOII.place(x=30 ,y=150)
        self.lblBBDDIngSoftware = Label(self.frameIngSoftware, text="BBDD", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblBBDDIngSoftware.place(x=30 ,y=220)
        self.lblProgI = Label(self.frameIngSoftware, text="ProgI", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblProgI.place(x=185 ,y=80)
        self.lblProgII = Label(self.frameIngSoftware, text="ProgII", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblProgII.place(x=182,y=150)

        #labels de TI
        self.lblIPOI = Label(self.frameTI, text="IPOI", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblIPOI.place(x=40 ,y=80)
        self.lblBBDDTI = Label(self.frameTI, text="BBDD", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblBBDDTI.place(x=30 ,y=150)
        self.lblSisInf = Label(self.frameTI, text="Sis. Inf", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblSisInf.place(x=30 ,y=220)
        self.lblRedesI = Label(self.frameTI, text="RedesI", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblRedesI.place(x=185 ,y=80)
        self.lblRedesII = Label(self.frameTI, text="RedesII", font=("Comic Sans",11), fg="white", background="#81C2AE")
        self.lblRedesII.place(x=180,y=150)

        #texto de computacion
        self.txtEDA=Entry(self.frameComputacion, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtEDA.place(x=90 ,y=80)
        self.txtSI=Entry(self.frameComputacion, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtSI.place(x=90 ,y=150)
        self.txtLogica=Entry(self.frameComputacion, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtLogica.place(x=90 ,y=220)
        self.txtAlgebra=Entry(self.frameComputacion, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtAlgebra.place(x=260 ,y=80)
        self.txtMetodologia=Entry(self.frameComputacion, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtMetodologia.place(x=260 ,y=150)

        #texto del computadores
        self.txtSSOO=Entry(self.frameComputadores, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtSSOO.place(x=95 ,y=80)
        self.txtPCTR=Entry(self.frameComputadores, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtPCTR.place(x=95 ,y=130)
        self.txtTECO=Entry(self.frameComputadores, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtTECO.place(x=95 ,y=180)
        self.txtECO=Entry(self.frameComputadores, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtECO.place(x=95 ,y=230)
        self.txtORCO=Entry(self.frameComputadores, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtORCO.place(x=250 ,y=80)
        self.txtARCO=Entry(self.frameComputadores, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtARCO.place(x=250 ,y=130)
        self.txtSSDD=Entry(self.frameComputadores, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtSSDD.place(x=250 ,y=180)

        #texto de ingenieria del software
        self.txtISOI=Entry(self.frameIngSoftware, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtISOI.place(x=90 ,y=80)
        self.txtISOII=Entry(self.frameIngSoftware, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtISOII.place(x=90 ,y=150)
        self.txtBBDDIngSoftware=Entry(self.frameIngSoftware, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtBBDDIngSoftware.place(x=90 ,y=220)
        self.txtProgI=Entry(self.frameIngSoftware, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtProgI.place(x=250 ,y=80)
        self.txtProgII=Entry(self.frameIngSoftware, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtProgII.place(x=250 ,y=150)
                  
        #texto de TI
        self.txtIPOI=Entry(self.frameTI, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtIPOI.place(x=90 ,y=80)
        self.txtBBDDTI=Entry(self.frameTI, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtBBDDTI.place(x=90 ,y=150)
        self.txtSisInf=Entry(self.frameTI, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtSisInf.place(x=90 ,y=220)
        self.txtRedesI=Entry(self.frameTI, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtRedesI.place(x=250 ,y=80)
        self.txtRedesII=Entry(self.frameTI, justify=LEFT, width=4, font=('Comic Sans', 11))
        self.txtRedesII.place(x=250 ,y=150)













        #Definicion frame Gustos
        self.frameGustos = Frame(bg = '#81C2AE', height=920, width=850)
        self.frameGustos.place(x=0, y=0)
        self.frameGustosPreguntas = Frame(self.frameGustos, bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        self.frameGustosPreguntas.place(x=50, y=50, width=720, height=659)

        #botones de gustos
        self.botonVolverGustos = Button(self.frameGustos, text="Volver al perfil", fg="black", width=25, command=self.initMenuPerfil)
        self.botonVolverGustos.place(x=590 ,y=732)

        #labels de gustos
        self.lblRespuestas = Label(self.frameGustosPreguntas, text="Respuestas", font=("Comic Sans",15), fg="white", background="#81C2AE")
        self.lblRespuestas.place(x=20 ,y=20)
        self.lblP1 = Label(self.frameGustosPreguntas, text="P1", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblP1.place(x=20 ,y=70)
        self.lblP2 = Label(self.frameGustosPreguntas, text="P2", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblP2.place(x=20 ,y=135)
        self.lblP3 = Label(self.frameGustosPreguntas, text="P3", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblP3.place(x=20 ,y=200)
        self.lblP4 = Label(self.frameGustosPreguntas, text="P4", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblP4.place(x=20 ,y=265)
        self.lblP5 = Label(self.frameGustosPreguntas, text="P5", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblP5.place(x=20 ,y=330)
        self.lblP6 = Label(self.frameGustosPreguntas, text="P6", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblP6.place(x=20 ,y=395)
        self.lblP7 = Label(self.frameGustosPreguntas, text="P7", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblP7.place(x=20 ,y=460)
        self.lblP8 = Label(self.frameGustosPreguntas, text="P8", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblP8.place(x=20 ,y=525)
        self.lblP9 = Label(self.frameGustosPreguntas, text="P9", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblP9.place(x=20 ,y=590)

        #texto de gustos
        self.txtP1=Entry(self.frameGustosPreguntas, justify=LEFT, width=77, font=('Comic Sans', 11))
        self.txtP1.place(x=60 ,y=70)
        self.txtP2=Entry(self.frameGustosPreguntas, justify=LEFT, width=77, font=('Comic Sans', 11))
        self.txtP2.place(x=60 ,y=135)
        self.txtP3=Entry(self.frameGustosPreguntas, justify=LEFT, width=77, font=('Comic Sans', 11))
        self.txtP3.place(x=60 ,y=200)
        self.txtP4=Entry(self.frameGustosPreguntas, justify=LEFT, width=77, font=('Comic Sans', 11))
        self.txtP4.place(x=60 ,y=265)
        self.txtP5=Entry(self.frameGustosPreguntas, justify=LEFT, width=77, font=('Comic Sans', 11))
        self.txtP5.place(x=60 ,y=330)
        self.txtP6=Entry(self.frameGustosPreguntas, justify=LEFT, width=77, font=('Comic Sans', 11))
        self.txtP6.place(x=60 ,y=395)
        self.txtP7=Entry(self.frameGustosPreguntas, justify=LEFT, width=77, font=('Comic Sans', 11))
        self.txtP7.place(x=60 ,y=460)
        self.txtP8=Entry(self.frameGustosPreguntas, justify=LEFT, width=77, font=('Comic Sans', 11))
        self.txtP8.place(x=60 ,y=525)
        self.txtP9=Entry(self.frameGustosPreguntas, justify=LEFT, width=77, font=('Comic Sans', 11))
        self.txtP9.place(x=60 ,y=590)




















             #Definición frame Formulario
        self.frameFormulario = Frame(bg = '#81C2AE', height=960, width=850)
        self.frameFormulario.place(x=0, y=0)
        self.frameFormularioPreguntas = Frame(self.frameFormulario, bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        self.frameFormularioPreguntas.place(x=30, y=15, width=750, height=710)

        #botones de formulario
        self.botonVolverFormulario = Button(self.frameFormulario, text="Volver al perfil", fg="black", width=25, command=self.initMenuPerfil)
        self.botonVolverFormulario.place(x=598 ,y=742)
        self.botonCambiosFormulario = Button(self.frameFormulario, text="Confirmar Cambios", fg="black", width=25, command=self.confirmarFormulario)
        self.botonCambiosFormulario.place(x=370 ,y=742)

        #labels de formulario
        self.lblFormulario = Label(self.frameFormularioPreguntas, text="Formulario", font=("Comic Sans",15), fg="white", background="#81C2AE")
        self.lblFormulario.place(x=20 ,y=20)
        self.lblP1Formulario = Label(self.frameFormularioPreguntas , text="P1. ¿Qué área te resulta más atractiva? ", font=("Comic Sans",12), fg="white", background="#81C2AE")
        self.lblP1Formulario.place(x=20 ,y=65)
        self.lblP2Formulario = Label(self.frameFormularioPreguntas , text="P2. ¿Qué tipo de programación te interesa más?", font=("Comic Sans",12), fg="white", background="#81C2AE")
        self.lblP2Formulario.place(x=20 ,y=135)
        self.lblP3Formulario = Label(self.frameFormularioPreguntas , text="P3. ¿Qué aspecto de la informática te intriga más?", font=("Comic Sans",12), fg="white", background="#81C2AE")
        self.lblP3Formulario.place(x=20 ,y=205)
        self.lblP4Formulario = Label(self.frameFormularioPreguntas , text="P4. ¿Qué te gustaría aprender más sobre?", font=("Comic Sans",12), fg="white", background="#81C2AE")
        self.lblP4Formulario.place(x=20 ,y=275)
        self.lblP5Formulario = Label(self.frameFormularioPreguntas , text="P5. ¿Qué habilidades te gustaría desarrollar más?", font=("Comic Sans",12), fg="white", background="#81C2AE")
        self.lblP5Formulario.place(x=20 ,y=345)
        self.lblP6Formulario = Label(self.frameFormularioPreguntas , text="P6. ¿Qué aspecto de la informática te gustaría aplicar en tu futuro profesional?", font=("Comic Sans",12), fg="white", background="#81C2AE")
        self.lblP6Formulario.place(x=20 ,y=415)
        self.lblP7Formulario = Label(self.frameFormularioPreguntas , text="P7. ¿Cuál es tu objetivo principal al estudiar informática?", font=("Comic Sans",12), fg="white", background="#81C2AE")
        self.lblP7Formulario.place(x=20 ,y=485)
        self.lblP8Formulario = Label(self.frameFormularioPreguntas , text="P8. ¿Qué área de la informática te motiva más en términos de innovación y avance tecnológico?", font=("Comic Sans",13), fg="white", background="#81C2AE")
        self.lblP8Formulario.place(x=20 ,y=555)
        self.lblP9Formulario = Label(self.frameFormularioPreguntas , text="P9. ¿Qué tipo de desafíos te resultan más emocionantes?", font=("Comic Sans",12), fg="white", background="#81C2AE")
        self.lblP9Formulario.place(x=20 ,y=625)

        #opciones de formulario
        opcionesP1 = ("a) Desarrollo de software y sistemas.", "b) Estructura y funcionamiento de los computadores. ", "c) Manipulación y análisis de datos. ","d) Gestión y diseño de redes de computadores.")
        opcionesP2 = ("a) Desarrollo de aplicaciones de software.","b) Programación de sistemas y tiempo real.", "c) Implementación de algoritmos y estructuras de datos.", "d) Diseño y configuración de redes informáticas.")
        opcionesP3 = ("a) Interacción humano-computador y experiencia de usuario.", "b) Arquitectura y funcionamiento interno de los computadores.", "c) Análisis y manipulación de grandes volúmenes de datos.", "d) Integración de interfaces de usuario con sistemas de información empresariales.")
        opcionesP4 = ("a) Desarrollo de software y gestión de proyectos.", "b) Estructura y funcionamiento de los sistemas informáticos.", "c) Algoritmos y técnicas de programación avanzada.", "d) Creación de interfaces de usuario.")
        opcionesP5 = ("a) Programación orientada a objetos y desarrollo de aplicaciones.", "b) Comprensión profunda de los sistemas operativos y la arquitectura de computadores.","c) Análisis de datos y desarrollo de soluciones inteligentes.", "d) Configuración y administración de redes y sistemas de información.")
        opcionesP6 = ("a) Desarrollo de software para diferentes plataformas y aplicaciones.", "b) Diseño y optimización de sistemas informáticos complejos.", "c) Investigación y desarrollo en inteligencia artificial y análisis de datos.", "d) Implementación y gestión de infraestructuras tecnológicas empresariales y diseño de interfaces.")
        opcionesP7 = ("a) Convertirme en un desarrollador de software altamente competente.","b) Profundizar en el funcionamiento interno de los sistemas informáticos.","c) Explorar nuevas tecnologías y aplicaciones en el análisis de datos.", "d) Adquirir habilidades para gestionar y asegurar sistemas de información empresariales y desarrollo software de interfaces aplicando lógica en el proyecto.")
        opcionesP8 = ("a) Desarrollo de software y aplicaciones para resolver problemas del mundo real.", "b) Investigación y diseño de nuevas arquitecturas de computadoras.", "c) Exploración de técnicas de inteligencia artificial para automatización y optimización.", "d) Implementación de infraestructuras de red para mejorar la conectividad y la seguridad.")
        opcionesP9 = ("a) Crear soluciones intuitivas y eficientes para usuarios finales.", "b) Resolver problemas complejos relacionados con la escalabilidad y el rendimiento de los sistemas informáticos.", "c) Abordar problemas de análisis de datos para obtener información significativa.", "d) Garantizar la disponibilidad y la integridad de la infraestructura tecnológica en entornos empresariales.")
                      
        #combobox de formulario
        self.comboboxP1 = Combobox(self.frameFormularioPreguntas , font=('Comic Sans', 10), values=opcionesP1, width=95, state='readonly')
        self.comboboxP1.current(0)  
        self.comboboxP1.place(x=20 ,y=100)
        self.comboboxP2 = Combobox(self.frameFormularioPreguntas , font=('Comic Sans', 10), values=opcionesP2, width=95, state='readonly')
        self.comboboxP2.current(0)  
        self.comboboxP2.place(x=20 ,y=170)
        self.comboboxP3 = Combobox(self.frameFormularioPreguntas , font=('Comic Sans', 10), values=opcionesP3, width=95, state='readonly')
        self.comboboxP3.current(0)  
        self.comboboxP3.place(x=20 ,y=240)
        self.comboboxP4 = Combobox(self.frameFormularioPreguntas , font=('Comic Sans', 10), values=opcionesP4, width=95, state='readonly')
        self.comboboxP4.current(0) 
        self.comboboxP4.place(x=20 ,y=310)
        self.comboboxP5 = Combobox(self.frameFormularioPreguntas , font=('Comic Sans', 10), values=opcionesP5, width=95, state='readonly')
        self.comboboxP5.current(0)  
        self.comboboxP5.place(x=20 ,y=380)
        self.comboboxP6 = Combobox(self.frameFormularioPreguntas , font=('Comic Sans', 10), values=opcionesP6, width=95, state='readonly')
        self.comboboxP6.current(0)  
        self.comboboxP6.place(x=20 ,y=450)
        self.comboboxP7 = Combobox(self.frameFormularioPreguntas , font=('Comic Sans', 10), values=opcionesP7, width=95, state='readonly')
        self.comboboxP7.current(0)  
        self.comboboxP7.place(x=20 ,y=520)
        self.comboboxP8 = Combobox(self.frameFormularioPreguntas , font=('Comic Sans', 10), values=opcionesP8, width=95, state='readonly')
        self.comboboxP8.current(0)  
        self.comboboxP8.place(x=20 ,y=590)
        self.comboboxP9 = Combobox(self.frameFormularioPreguntas , font=('Comic Sans', 10), values=opcionesP9, width=95, state='readonly')
        self.comboboxP9.current(0) 
        self.comboboxP9.place(x=20 ,y=660)


















        self.initMenuLogin()
        self.ventana.mainloop()

    def initMenuLogin(self):
        self.frameLogin.place(x=0, y=0)
        self.framePerfil.place_forget()
        self.frameRegistrar.place_forget()
        self.frameCalificaciones.place_forget()
        self.frameGustos.place_forget()
        self.frameFormulario.place_forget()
        self.escribirDatosPerfil()
        self.escribirDatosCalificaciones()
        self.escribirGustos()
        self.limpiarCamposCalificaciones()
        self.limpiarCamposGustos()
        self.limpiarCamposPerfil()
        self.limpiarCamposRegistro()
        self.limpiarCamposLogin()
        
    
    def initMenuPerfil(self):
        self.framePerfil.place(x=0, y=0)
        self.frameLogin.place_forget()
        self.frameRegistrar.place_forget()
        self.frameCalificaciones.place_forget()
        self.frameGustos.place_forget()
        self.frameFormulario.place_forget()
        self.escribirDatosPerfil()

        # Crear una instancia de la clase Perfil
        perfil = Perfil()

        # Obtener los datos del usuario
        datos_usuario = perfil.obtener_datos(self.txtLogin.get())
        # Verificar si se obtuvieron datos del usuario
        if datos_usuario:
            self.limpiarCamposPerfil()

            # Establecer los datos en los Entry correspondientes
            self.txtNombre.insert(0, datos_usuario[0])
            self.txtApellido.insert(0, datos_usuario[1])
            self.txtDNI.insert(0, datos_usuario[3])
            self.txtTelefono.insert(0, datos_usuario[2])
            self.noEscribirDatosPerfil()
        else:
            # Si no se encuentran datos del usuario, mostrar un mensaje de error
            messagebox.showerror("Error", "No se encontraron datos del usuario.")
            

    def initMenuRegistrar(self):
        self.frameRegistrar.place(x=0, y=0)
        self.framePerfil.place_forget()
        self.frameLogin.place_forget()
        self.frameCalificaciones.place_forget()
        self.frameGustos.place_forget()
        self.frameFormulario.place_forget()


    def initMenuCalificaciones(self):
        self.frameCalificaciones.place(x=0, y=0)
        self.framePerfil.place_forget()
        self.frameLogin.place_forget()
        self.frameRegistrar.place_forget()
        self.frameGustos.place_forget()
        self.frameFormulario.place_forget()

        self.botonConfirmarCalificaciones.config(state=DISABLED)
        self.botonActualizarCalificaciones.config(state=NORMAL)


         # Crear una instancia de la clase Perfil
        perfil = Perfil()
        # Obtener los datos del usuario
        notas_usuario = perfil.obtener_calificaciones(self.txtLogin.get()) 

        if notas_usuario:
            self.limpiarCamposCalificaciones()
            #eda, si, logica, algebra, metodologia, ipoi, bbdd, sisinf, redesi, redesii, ssoo, pctr, teco, eco, arco, orco, ssdd, isoi, isoii, progi, progii
            campos = [self.txtEDA, self.txtSI, self.txtLogica, self.txtAlgebra, self.txtMetodologia, self.txtIPOI, self.txtBBDDTI, self.txtSisInf, self.txtRedesI, self.txtRedesII, self.txtSSOO, self.txtPCTR, self.txtTECO, self.txtECO, self.txtARCO, self.txtORCO, self.txtSSDD, self.txtISOI, self.txtISOII, self.txtProgI, self.txtProgII]
            self.txtBBDDIngSoftware.insert(0, notas_usuario[6])
            for i in range(len(notas_usuario)):
                campos[i].insert(0, notas_usuario[i])
            self.noEscribirDatosCalificaciones()
        else:
            # Si no se encuentran datos del usuario, mostrar un mensaje de error
            messagebox.showerror("Error", "No se encontraron las notas del usuario.")

    def initMenuCambiarContrasena(self):
        InterfazCambiarContrasena(self.txtLogin.get())

    def initMenuGustos(self):
        self.frameGustos.place(x=0, y=0)
        self.framePerfil.place_forget()
        self.frameLogin.place_forget()
        self.frameRegistrar.place_forget()
        self.frameCalificaciones.place_forget()
        self.frameFormulario.place_forget()
        self.escribirGustos()
        # Crear una instancia de la clase Perfil
        perfil = Perfil()
        # Obtener los datos del usuario
        gustos_usuario = perfil.obtener_gustos(self.txtLogin.get())
        if gustos_usuario:
            self.limpiarCamposGustos()
            #pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9
            campos = [self.txtP1, self.txtP2, self.txtP3, self.txtP4, self.txtP5, self.txtP6, self.txtP7, self.txtP8, self.txtP9]
            for i in range(len(gustos_usuario)):
                campos[i].insert(0, gustos_usuario[i])
            self.noEscribirGustos()
        else:
            # Si no se encuentran datos del usuario, mostrar un mensaje de error
            messagebox.showerror("Error", "No se encontraron los gustos del usuario.")

    def initMenuFormulario(self):
        self.frameFormulario.place(x=0, y=0)
        self.framePerfil.place_forget()
        self.frameLogin.place_forget()
        self.frameRegistrar.place_forget()
        self.frameCalificaciones.place_forget()
        self.frameGustos.place_forget()
        self.comboboxInicio0()

    def verificarCredenciales(self):
        usuario = self.txtLogin.get()
        contrasena = self.txtContrasena.get()
        login = Login()
        if login.verificar_usuario(usuario, contrasena):
            messagebox.showinfo("Autenticación exitosa", "¡Autenticación exitosa!")
            self.initMenuPerfil()
        else:
            messagebox.showerror("Autenticación fallida", "¡Autenticación fallida!")
            # Limpiar el contenido del campo de contraseña si la autenticación falla
            self.txtContrasena.delete(0, END)

    def registrarUsuario(self):
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas confirmar el registro?")
        if respuesta:
            usuario = self.txtLoginRegistro.get()
            contrasena = self.txtContrasenaRegistro.get()
            nombre = self.txtNombreRegistro.get()
            apellido = self.txtApellidoRegistro.get()
            dni = self.txtDNIRegistro.get()
            telefono = self.txtTelefonoRegistro.get()
            registro = Registro()
            # Verificar si algún campo está vacío
            if not (usuario and contrasena and nombre and apellido and dni and telefono):
                messagebox.showerror("Campos incompletos", "Debes completar todos los campos")
                return
            exito, mensaje = registro.registrar_usuario(dni, usuario, contrasena, nombre, apellido, telefono)
            if exito:
                messagebox.showinfo("Registro exitoso", mensaje)
                self.initMenuLogin()
            else:
                messagebox.showerror("Registro fallido", mensaje)
                # Limpiar el contenido del campo de contraseña si el registro falla
                self.limpiarCamposRegistro()

    def actualizarCalificaciones(self):
        self.escribirDatosCalificaciones()
        self.botonConfirmarCalificaciones.config(state=NORMAL)
        self.botonActualizarCalificaciones.config(state=DISABLED)


    def confirmarCalificaciones(self):
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas confirmar la actualización de las calificaciones?")
        if respuesta:
            perfil = Perfil()
            #eda, si, logica, algebra, metodologia, ipoi, bbdd, sisinf, redesi, redesii, ssoo, pctr, teco, eco, arco, orco, ssdd, isoi, isoii, progi, progii
            notas = [self.txtEDA.get(), self.txtSI.get(), self.txtLogica.get(), self.txtAlgebra.get(), self.txtMetodologia.get(), self.txtIPOI.get(), self.txtBBDDTI.get(), self.txtSisInf.get(), self.txtRedesI.get(), self.txtRedesII.get(), self.txtSSOO.get(), self.txtPCTR.get(), self.txtTECO.get(), self.txtECO.get(), self.txtARCO.get(), self.txtORCO.get(), self.txtSSDD.get(), self.txtISOI.get(), self.txtISOII.get(), self.txtProgI.get(), self.txtProgII.get()]
            exito, mensaje = perfil.actualizar_calificaciones(self.txtLogin.get(), notas)
            if exito:
                messagebox.showinfo("Actualización exitosa", mensaje)

            else:
                messagebox.showerror("Actualización fallida", mensaje)
            self.initMenuCalificaciones()
            self.noEscribirDatosCalificaciones()

        else:
            self.initMenuCalificaciones()
            self.noEscribirDatosCalificaciones()

    def confirmarFormulario(self):
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas confirmar las respuestas del formulario?")
        if respuesta:
            perfil = Perfil()
            respuestas = [self.comboboxP1.get(), self.comboboxP2.get(), self.comboboxP3.get(), self.comboboxP4.get(), self.comboboxP5.get(), self.comboboxP6.get(), self.comboboxP7.get(), self.comboboxP8.get(), self.comboboxP9.get()]
            exito, mensaje = perfil.actualizar_formulario(self.txtLogin.get(), respuestas)
            if exito:
                messagebox.showinfo("Realización exitosa", mensaje)
            else:
                messagebox.showerror("Realización fallida", mensaje)
            self.initMenuFormulario()
        else:
            self.initMenuFormulario()

    def obtenerRecomendaciones(self):
        respuesta = messagebox.askyesno("Confirmación", "Vas a proceder a obtener tu recomendación, esto no quiere decir que sea tu decisión, esto solo se toma de manera orientativo, ¿estás listo?")
        if respuesta:
            self.initMenuCalificaciones()
            self.initMenuGustos()
            perfil = Perfil()
            notas_computacion, notas_computadores, notas_ing_software, notas_ti = self.obtenerNotas()
            recomendacion = perfil.obtener_recomendaciones(self.txtLogin.get(), notas_computacion, notas_computadores, notas_ing_software, notas_ti)
        else:
            self.initMenuPerfil()

    def obtenerNotas(self):
        notas_computacion = {
            float(self.txtEDA.get() or 0),
            float(self.txtSI.get() or 0),
            float(self.txtLogica.get() or 0),
            float(self.txtAlgebra.get() or 0),
            float(self.txtMetodologia.get() or 0)
        }

        notas_computadores = {
            float(self.txtSSOO.get() or 0),
            float(self.txtPCTR.get() or 0),
            float(self.txtTECO.get() or 0),
            float(self.txtECO.get() or 0),
            float(self.txtORCO.get() or 0),
            float(self.txtARCO.get() or 0),
            float(self.txtSSDD.get() or 0)
        }

        notas_ing_software = {
            float(self.txtISOI.get() or 0),
            float(self.txtISOII.get() or 0),
            float(self.txtBBDDIngSoftware.get() or 0),
            float(self.txtProgI.get() or 0),
            float(self.txtProgII.get() or 0)
        }

        notas_ti = {
            float(self.txtIPOI.get() or 0),
            float(self.txtBBDDTI.get() or 0),
            float(self.txtSisInf.get() or 0),
            float(self.txtRedesI.get() or 0),
            float(self.txtRedesII.get() or 0)
        }
        return notas_computacion, notas_computadores, notas_ing_software, notas_ti


    def noEscribirDatosCalificaciones(self):
        self.txtEDA.config(state='disabled')
        self.txtSI.config(state='disabled')
        self.txtLogica.config(state='disabled')
        self.txtAlgebra.config(state='disabled')
        self.txtMetodologia.config(state='disabled')
        self.txtIPOI.config(state='disabled')
        self.txtBBDDTI.config(state='disabled')
        self.txtSisInf.config(state='disabled')
        self.txtRedesI.config(state='disabled')
        self.txtRedesII.config(state='disabled')
        self.txtSSOO.config(state='disabled')
        self.txtPCTR.config(state='disabled')
        self.txtTECO.config(state='disabled')
        self.txtECO.config(state='disabled')
        self.txtARCO.config(state='disabled')
        self.txtORCO.config(state='disabled')
        self.txtSSDD.config(state='disabled')
        self.txtISOI.config(state='disabled')
        self.txtISOII.config(state='disabled')
        self.txtProgI.config(state='disabled')
        self.txtProgII.config(state='disabled')
        self.txtBBDDIngSoftware.config(state='disabled')

    def escribirDatosCalificaciones(self):
        self.txtEDA.config(state='normal')
        self.txtSI.config(state='normal')
        self.txtLogica.config(state='normal')
        self.txtAlgebra.config(state='normal')
        self.txtMetodologia.config(state='normal')
        self.txtIPOI.config(state='normal')
        self.txtBBDDTI.config(state='normal')
        self.txtSisInf.config(state='normal')
        self.txtRedesI.config(state='normal')
        self.txtRedesII.config(state='normal')
        self.txtSSOO.config(state='normal')
        self.txtPCTR.config(state='normal')
        self.txtTECO.config(state='normal')
        self.txtECO.config(state='normal')
        self.txtARCO.config(state='normal')
        self.txtORCO.config(state='normal')
        self.txtSSDD.config(state='normal')
        self.txtISOI.config(state='normal')
        self.txtISOII.config(state='normal')
        self.txtProgI.config(state='normal')
        self.txtProgII.config(state='normal')
        self.txtBBDDIngSoftware.config(state='normal')

    def limpiarCamposCalificaciones(self):
        self.txtEDA.delete(0, END)
        self.txtSI.delete(0, END)
        self.txtLogica.delete(0, END)
        self.txtAlgebra.delete(0, END)
        self.txtMetodologia.delete(0, END)
        self.txtIPOI.delete(0, END)
        self.txtBBDDTI.delete(0, END)
        self.txtSisInf.delete(0, END)
        self.txtRedesI.delete(0, END)
        self.txtRedesII.delete(0, END)
        self.txtSSOO.delete(0, END)
        self.txtPCTR.delete(0, END)
        self.txtTECO.delete(0, END)
        self.txtECO.delete(0, END)
        self.txtARCO.delete(0, END)
        self.txtORCO.delete(0, END)
        self.txtSSDD.delete(0, END)
        self.txtISOI.delete(0, END)
        self.txtISOII.delete(0, END)
        self.txtProgI.delete(0, END)
        self.txtProgII.delete(0, END)
        self.txtBBDDIngSoftware.delete(0, END)

    def limpiarCamposRegistro(self):
        self.txtLoginRegistro.delete(0, END)
        self.txtContrasenaRegistro.delete(0, END)
        self.txtNombre.delete(0, END)
        self.txtApellido.delete(0, END)
        self.txtDNI.delete(0, END)
        self.txtTelefono.delete(0, END)
    
    def limpiarCamposGustos(self):
        self.txtP1.delete(0, END)
        self.txtP2.delete(0, END)
        self.txtP3.delete(0, END)
        self.txtP4.delete(0, END)
        self.txtP5.delete(0, END)
        self.txtP6.delete(0, END)
        self.txtP7.delete(0, END)
        self.txtP8.delete(0, END)
        self.txtP9.delete(0, END)

    def limpiarCamposPerfil(self):
        self.txtNombre.delete(0, END)
        self.txtApellido.delete(0, END)
        self.txtDNI.delete(0, END)
        self.txtTelefono.delete(0, END)

    def limpiarCamposLogin(self):
        self.txtLogin.delete(0, END)
        self.txtContrasena.delete(0, END)

    def comboboxInicio0(self):
        self.comboboxP1.current(0)
        self.comboboxP2.current(0)
        self.comboboxP3.current(0)
        self.comboboxP4.current(0)
        self.comboboxP5.current(0)
        self.comboboxP6.current(0)
        self.comboboxP7.current(0)
        self.comboboxP8.current(0)
        self.comboboxP9.current(0)
        self.comboboxP1.focus_set()

    def escribirDatosPerfil(self):
        self.txtNombre.config(state='normal')
        self.txtApellido.config(state='normal')
        self.txtDNI.config(state='normal')
        self.txtTelefono.config(state='normal')
    
    def noEscribirDatosPerfil(self):
        self.txtNombre.config(state='disabled')
        self.txtApellido.config(state='disabled')
        self.txtDNI.config(state='disabled')
        self.txtTelefono.config(state='disabled')

    def escribirGustos(self):
        self.txtP1.config(state='normal')
        self.txtP2.config(state='normal')
        self.txtP3.config(state='normal')
        self.txtP4.config(state='normal')
        self.txtP5.config(state='normal')
        self.txtP6.config(state='normal')
        self.txtP7.config(state='normal')
        self.txtP8.config(state='normal')
        self.txtP9.config(state='normal')

    def noEscribirGustos(self):
        self.txtP1.config(state='disabled')
        self.txtP2.config(state='disabled')
        self.txtP3.config(state='disabled')
        self.txtP4.config(state='disabled')
        self.txtP5.config(state='disabled')
        self.txtP6.config(state='disabled')
        self.txtP7.config(state='disabled')
        self.txtP8.config(state='disabled')
        self.txtP9.config(state='disabled')