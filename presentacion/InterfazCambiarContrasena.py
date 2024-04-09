from tkinter import *



class InterfazCambiarContrasena:

    def __init__(self):
        #Definición ventana Cambiar Contraseña
        ventana = Tk()
        ventana.title("Cambiar contraseña")
        ventana.resizable(False, False)

        #Definición frame Cambiar Contraseña
        self.frameContrasena = Frame(ventana, bg='#81C2AE', height=300, width=650)
        self.frameContrasena.pack(fill=BOTH, expand=True)

        #botones del cambiar contraseña
        self.botonCambiarContrasena = Button(self.frameContrasena, text="Cambiar", fg="black", width=30)
        self.botonCambiarContrasena .place(x=355 ,y=210)

        #labels del cambiar contraseña
        self.lblContrasenaAntigua = Label(self.frameContrasena, text="Contraseña Antigua", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblContrasenaAntigua.place(x=30 ,y=60)
        self.lblContrasenaNueva = Label(self.frameContrasena, text="Contraseña Nueva", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblContrasenaNueva.place(x=35 ,y=130)

        ##texto del cambiar contraseña
        self.txtContrasenaAntigua=Entry(self.frameContrasena, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtContrasenaAntigua.place(x=210 ,y=60)
        self.txtContrasenaNueva=Entry(self.frameContrasena, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtContrasenaNueva.place(x=210 ,y=130)

        ventana.mainloop()

    