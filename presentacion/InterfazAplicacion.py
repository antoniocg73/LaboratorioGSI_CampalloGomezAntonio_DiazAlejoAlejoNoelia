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

        self.botonCalificaciones = Button(self.framePerfil, text="Calificaciones", fg="black", width=25)
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









        self.initMenuLogin()
        self.ventana.mainloop()

    def initMenuLogin(self):
        self.frameLogin.place(x=0, y=0)
        self.framePerfil.place_forget()
        self.frameRegistrar.place_forget()
    
    def initMenuPerfil(self):
        self.framePerfil.place(x=0, y=0)
        self.frameLogin.place_forget()
        self.frameRegistrar.place_forget()

        # Crear una instancia de la clase Perfil
        perfil = Perfil()

        # Obtener los datos del usuario
        datos_usuario = perfil.obtener_datos(self.txtLogin.get())
        print(datos_usuario)
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
        cambiarContrasena = InterfazCambiarContrasena()
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

