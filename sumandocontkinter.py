#ejemplo 3: en tkinter, haciendo un calculador de suma, 1 label para el 1er numero, 1 label para el 2do numero, 2 entrys, 1 boton, y un lbel para el resultado

import tkinter as tk

def sumar():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    resultado = num1 + num2
    resultado = "El resultado de la suma es:{0}",resultado
    label_resultado.config(text=resultado)
    #listo, solo falta ajustar la codificacion

#instancia de tkinter es el objeto que crea la  ventana
root = tk.Tk()
#root es el objeto sobre el cual seteamos todos los valores de la ventana
#todas las propieddades
root.title("Calculadora de suma")
#desde el titulo a las dimensiones
root.geometry("400x400")
#configuraciones de si sera o no ajustable
root.resizable(False, False)
#color de fondo
root.configure(background="#333333")
#crear labels
#el label lo creamos con la clase tk y accedemos a la funcion Label, seteamos las propiedades
#como el objeto padre : root, el texto, el color de fondo y el color del texto
label1 = tk.Label(root, text="Numero 1:", bg="#333333", fg="white")
#ajustamos a la grid
label1.grid(column=0,row=0)
label2 = tk.Label(root, text="Numero 2:", bg="#333333", fg="white")
label2.grid(row=1,column=0)
#crear entrys
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)
#crear boton
boton = tk.Button(root, text="Sumar")
boton.config(command=sumar)
boton.grid(row=2, column=1)
#crear label resultado
label_resultado = tk.Label(root, text="", bg="#333333", fg="white")
label_resultado.grid(row=3, column=1)
#ejecutar el loop
root.mainloop()

#fin del archivo : ejecutamos


