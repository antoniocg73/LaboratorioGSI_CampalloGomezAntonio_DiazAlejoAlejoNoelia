from tkinter import *
from tkinter import PhotoImage, messagebox
from tkinter.ttk import Combobox
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

        self.botonCalificaciones = Button(self.framePerfil, text="Calificaciones", fg="black", width=25, command=self.initMenuCalificaciones)
        self.botonCalificaciones.place(x=620 ,y=100)
        self.botonGustos = Button(self.framePerfil, text="Gustos", fg="black", width=25)
        self.botonGustos.place(x=620 ,y=150)
        self.botonFormulario = Button(self.framePerfil, text="Formulario", fg="black", width=25)
        self.botonFormulario.place(x=620 ,y=650)

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
        self.botonActualizarFormulario = Button(self.frameCalificaciones, text="Actualizar notas", fg="black", width=25)
        self.botonActualizarFormulario.place(x=350 ,y=710)
        self.botonVolverFormulario = Button(self.frameCalificaciones, text="Volver al perfil", fg="black", width=25, command=self.initMenuPerfil)
        self.botonVolverFormulario.place(x=585 ,y=710)

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




        self.initMenuLogin()
        self.ventana.mainloop()

    def initMenuLogin(self):
        self.frameLogin.place(x=0, y=0)
        self.framePerfil.place_forget()
        self.frameRegistrar.place_forget()
        self.frameCalificaciones.place_forget()
    
    def initMenuPerfil(self):
        self.framePerfil.place(x=0, y=0)
        self.frameLogin.place_forget()
        self.frameRegistrar.place_forget()
        self.frameCalificaciones.place_forget()

        # Crear una instancia de la clase Perfil
        perfil = Perfil()

        # Obtener los datos del usuario
        datos_usuario = perfil.obtener_datos(self.txtLogin.get())
        # Verificar si se obtuvieron datos del usuario
        if datos_usuario:
            self.limpiarCamposPerfil()

            # Establecer los datos en los Entry correspondientes
            self.txtNombre.insert(0, datos_usuario[0])
            self.txtNombre.config(state='disabled')

            self.txtApellido.insert(0, datos_usuario[1])
            self.txtApellido.config(state='disabled')

            self.txtDNI.insert(0, datos_usuario[3])
            self.txtDNI.config(state='disabled')

            self.txtTelefono.insert(0, datos_usuario[2])
            self.txtTelefono.config(state='disabled')
        else:
            # Si no se encuentran datos del usuario, mostrar un mensaje de error
            messagebox.showerror("Error", "No se encontraron datos del usuario.")
            

    def initMenuRegistrar(self):
        self.frameRegistrar.place(x=0, y=0)
        self.framePerfil.place_forget()
        self.frameLogin.place_forget()
        self.frameCalificaciones.place_forget()

    def initMenuCalificaciones(self):
        self.frameCalificaciones.place(x=0, y=0)
        self.framePerfil.place_forget()
        self.frameLogin.place_forget()
        self.frameRegistrar.place_forget()

         # Crear una instancia de la clase Perfil
        perfil = Perfil()
        # Obtener los datos del usuario
        notas_usuario = perfil.obtener_calificaciones(self.txtLogin.get()) 
        print(notas_usuario)  
        print(notas_usuario[0])
        print(notas_usuario[1])

        if notas_usuario:
            #eda, si, logica, algebra, metodologia, ipoi, bbdd, sisinf, redesi, redesii, ssoo, pctr, teco, eco, arco, orco, ssdd, isoi, isoii, progi, progii
            campos = [self.txtEDA, self.txtSI, self.txtLogica, self.txtAlgebra, self.txtMetodologia, self.txtIPOI, self.txtBBDDTI, self.txtSisInf, self.txtRedesI, self.txtRedesII, self.txtSSOO, self.txtPCTR, self.txtTECO, self.txtECO, self.txtARCO, self.txtORCO, self.txtSSDD, self.txtISOI, self.txtISOII, self.txtProgI, self.txtProgII]
            self.txtBBDDIngSoftware.insert(0, notas_usuario[6])
            self.txtBBDDIngSoftware.config(state='disabled')
            for i in range(len(notas_usuario)):
                print(notas_usuario[i])
                campos[i].insert(0, notas_usuario[i])
                campos[i].config(state='disabled')
            '''
            self.txtEDA.insert(0, notas_usuario[0])
            self.txtEDA.config(state='disabled')
            self.txtSI.insert(0, notas_usuario[1])
            self.txtSI.config(state='disabled')
            self.txtLogica.insert(0, notas_usuario[2])
            self.txtLogica.config(state='disabled')
            self.txtAlgebra.insert(0, notas_usuario[3])
            self.txtAlgebra.config(state='disabled')
            self.txtMetodologia.insert(0, notas_usuario[4])
            self.txtMetodologia.config(state='disabled')
            self.txtIPOI.insert(0, notas_usuario[5])
            self.txtIPOI.config(state='disabled')
            self.txtBBDDTI.insert(0, notas_usuario[6])
            self.txtBBDDTI.config(state='disabled')
            self.txtSisInf.insert(0, notas_usuario[7])
            self.txtSisInf.config(state='disabled')
            self.txtRedesI.insert(0, notas_usuario[8])
            self.txtRedesI.config(state='disabled')
            self.txtRedesII.insert(0, notas_usuario[9])
            self.txtRedesII.config(state='disabled')
            self.txtSSOO.insert(0, notas_usuario[10])
            self.txtSSOO.config(state='disabled')
            self.txtPCTR.insert(0, notas_usuario[11])
            self.txtPCTR.config(state='disabled')
            self.txtTECO.insert(0, notas_usuario[12])
            self.txtTECO.config(state='disabled')
            self.txtECO.insert(0, notas_usuario[13])
            self.txtECO.config(state='disabled')
            self.txtARCO.insert(0, notas_usuario[14])
            self.txtARCO.config(state='disabled')
            self.txtORCO.insert(0, notas_usuario[15])
            self.txtORCO.config(state='disabled')
            self.txtSSDD.insert(0, notas_usuario[16])
            self.txtSSDD.config(state='disabled')
            self.txtISOI.insert(0, notas_usuario[17])
            self.txtISOI.config(state='disabled')
            self.txtISOII.insert(0, notas_usuario[18])
            self.txtISOII.config(state='disabled')
            self.txtProgI.insert(0, notas_usuario[19])
            self.txtProgI.config(state='disabled')
            self.txtProgII.insert(0, notas_usuario[20])
            self.txtProgII.config(state='disabled')
            '''
        else:
            # Si no se encuentran datos del usuario, mostrar un mensaje de error
            messagebox.showerror("Error", "No se encontraron las notas del usuario.")

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

    def initMenuCambiarContrasena(self):
        InterfazCambiarContrasena(self.txtLogin.get())
        self.txtNombre.config(state='normal')
        self.txtApellido.config(state='normal')
        self.txtDNI.config(state='normal')
        self.txtTelefono.config(state='normal')


    def limpiarCamposRegistro(self):
        self.txtLoginRegistro.delete(0, END)
        self.txtContrasenaRegistro.delete(0, END)
        self.txtNombre.delete(0, END)
        self.txtApellido.delete(0, END)
        self.txtDNI.delete(0, END)
        self.txtTelefono.delete(0, END)
    
    def limpiarCamposPerfil(self):
        self.txtNombre.delete(0, END)
        self.txtApellido.delete(0, END)
        self.txtDNI.delete(0, END)
        self.txtTelefono.delete(0, END)

