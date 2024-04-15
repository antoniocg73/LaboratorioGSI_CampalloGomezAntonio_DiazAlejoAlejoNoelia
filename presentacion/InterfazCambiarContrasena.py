from tkinter import *
from tkinter import PhotoImage, messagebox
from dominio.perfil import Perfil
class InterfazCambiarContrasena:

    def __init__(self, nombreUsuario, ventanaAnterior):
        #Definición ventana anterior
        self.ventanaAnterior = ventanaAnterior
        self.ventanaAnterior.withdraw()
        #Definición ventana Cambiar Contraseña
        self.ventana = Tk()
        self.ventana.title("Cambiar contraseña")
        self.ventana.resizable(False, False)
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        self.nombreUsuario = nombreUsuario

        #Definición frame Cambiar Contraseña
        self.frameContrasena = Frame(self.ventana, bg='#81C2AE', height=300, width=650)
        self.frameContrasena.pack(fill=BOTH, expand=True)

        #botones del cambiar contraseña
        self.botonCambiarContrasena = Button(self.frameContrasena, text="Cambiar", fg="black", width=30, command=self.cambiar_contrasena)
        self.botonCambiarContrasena .place(x=355 ,y=210)

        #labels del cambiar contraseña
        self.lblContrasenaAntigua = Label(self.frameContrasena, text="Contraseña Antigua", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblContrasenaAntigua.place(x=30 ,y=60)
        self.lblContrasenaNueva = Label(self.frameContrasena, text="Contraseña Nueva", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblContrasenaNueva.place(x=35 ,y=130)

        ##texto del cambiar contraseña
        self.txtContrasenaAntigua=Entry(self.frameContrasena, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtContrasenaAntigua.place(x=210 ,y=60)
        self.txtContrasenaNueva=Entry(self.frameContrasena, justify=LEFT, width=33, font=('Comic Sans', 14), show="*")
        self.txtContrasenaNueva.place(x=210 ,y=130)

        self.ventana.mainloop()

    def cambiar_contrasena(self):
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas confirmar la actualización de las calificaciones?")
        if respuesta:
            antigua = self.txtContrasenaAntigua.get()
            nueva = self.txtContrasenaNueva.get()
            perfil = Perfil()
            if antigua == nueva:
                messagebox.showerror("Error", "La contraseña nueva no puede ser igual a la antigua.")
            elif len(nueva) < 4:
                messagebox.showerror("Error", "La contraseña nueva debe tener al menos 4 caracteres.")
            else:
                resultado, mensaje = perfil.cambiar_contrasena(self.nombreUsuario, antigua, nueva)
                if resultado:
                    messagebox.showinfo("Éxito", mensaje)
                    
                else:
                    messagebox.showerror("Error", mensaje)
            self.ventanaAnterior.update()
            self.ventanaAnterior.deiconify()
            self.ventana.destroy()

    def cerrar_ventana(self):
        self.ventanaAnterior.update()
        self.ventanaAnterior.deiconify()
        self.ventana.destroy()


    