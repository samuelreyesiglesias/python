#ejemplo2:tkinter libreria guid para crear ventanas, o formularios
# este ejemplo vreemos un form que adapta a la grid los controles: label, entrys, boton de un formulario para
#obtener datos de un cliente y mostrarlos
from tkinter import * ;
from tkinter import messagebox;


#creamos la instancia de tkinter
ventana = Tk()
#configuramos el titulo de la ventana
ventana.title("Ejemplo 2")
#configuramos el tamaño de la ventana
ventana.geometry("400x400")
#configuramos el borde de la ventana
ventana.config(bd=25)
#configuramos el color de fondo de la ventana
ventana.config(bg="red")

#creamos un label
label = Label(ventana, text="Nombre: ")
#colocamos el label en la ventana
label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
#creamos un entry
entry = Entry(ventana)
#colocamos el entry en la ventana
entry.grid(row=0, column=1, padx=10, pady=10) 
#creamos un boton
boton1 = Button(ventana, text="Mostrar")
#colocamos el boton en la ventana
boton1.grid(row=0, column=2, padx=10, pady=10)
#creamos un boton
boton2 = Button(ventana, text="Salir")
#colocamos el boton en la ventana
boton2.grid(row=1, column=2, padx=10, pady=10)

#pintamos todo 
#mainloop: es la funcion que nos permite crear todo lo necesario
# o renderizar los controles y la ventana.-

#definimos las funciones de los botones
def mostrar():  
    messagebox.showinfo("Informacion", f"Nombre: {entry.get()}")

def salir():
    ventana.destroy()

#configuramos los eventos de los botones
boton1.config(command=mostrar)
boton2.config(command=salir)

#listo
ventana.mainloop();

#tenia un error en el nombre de los botones
#entonces ambos se llamaban igual , sustituia el evento o comando
