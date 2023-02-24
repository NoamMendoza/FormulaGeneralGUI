import random
from tkinter import *
import math
from tkinter import Frame
from tkinter import messagebox

#Se hace la operacion de dentro de la raiz para una comprobacion
def raiz(a, b, c):
    r1 = (b ** 2) - 4 * (a * c)
    return r1

#Se hace la formula en caso de que no de una raiz negativa
def formula(a, b, c):
    x1 = ((-b + math.sqrt(raiz(a, b, c))) / (2 * a))
    x2 = ((-b - math.sqrt(raiz(a, b, c))) / (2 * a))
    RR1 = str("X1 =" + str(x1) + "X2 =" + str(x2))
    return RR1

#se hace la formula en caso de que de una raiz negativa
def formulacomplex(a, b, c):
    s1 = -b / (2 * a)
    s2 = math.sqrt(abs(raiz(a, b, c))) / (2 * a)
    RI1 = str("X1 =" + str(s1) + "+" + str(s2) + "i || " + "X2 =" + str(s1) + "-" + str(s2) + "i")
    return RI1

#Se valida que la variable a no sea cero y que la raiz sea negativa
def botonResolver(a, b, c):
    if a != 0:
        if raiz(a, b, c) < 0:
            vartxt4.set(formulacomplex(a, b, c))
        else:
            vartxt4.set(formula(a, b, c))
    else:
        vartxt4.set("Math error: cualquier cosa dividida entre 0 nos da una indeterminación")

#esta funcion limpia todos los campos
def botonLimpiar():
    vartxt1.set("")
    vartxt2.set("")
    vartxt3.set("")
    vartxt4.set("")

#recoge variables y hace la comprovacion de que sean solo numeros enteros o decimales
def recogerVariables():
    particion1 = (vartxt1.get()).partition('.')
    particion2 = (vartxt2.get()).partition('.')
    particion3 = (vartxt3.get()).partition('.')

    if (vartxt1.get())=="" or (vartxt2.get())=="" or (vartxt3.get())=="":
        messagebox.showerror("Error", "Las casillas necesitan estar llenas.")
    else:
        if (vartxt1.get()).isdigit() and (vartxt2.get()).isdigit() and (vartxt3.get()).isdigit():
            a = float(vartxt1.get())
            b = float(vartxt2.get())
            c = float(vartxt3.get())
            botonResolver(a, b, c)
        else:
            if particion1[0].isdigit() and particion1[1] == '.' and particion1[2].isdigit() or (particion1[0] == '' and particion1[1] == '.' and particion1[2].isdigit()) or (particion1[0].isdigit() and particion1[1] == '.' and particion1[2] == ''):
                if particion2[0].isdigit() and particion2[1] == '.' and particion2[2].isdigit() or (particion2[0] == '' and particion2[1] == '.' and particion2[2].isdigit()) or (particion2[0].isdigit() and particion2[1] == '.' and particion2[2] == ''):
                    if particion1[0].isdigit() and particion1[1] == '.' and particion1[2].isdigit() or (particion1[0] == '' and particion1[1] == '.' and particion1[2].isdigit()) or (particion1[0].isdigit() and particion1[1] == '.' and particion1[2] == ''):
                        a = float(vartxt1.get())
                        b = float(vartxt2.get())
                        c = float(vartxt3.get())
                        botonResolver(a, b, c)
                    else:
                        messagebox.showerror("Error", "Ingrese caracteres validos (numeros enteros o decimales)")
                else:
                    messagebox.showerror("Error", "Ingrese caracteres validos (numeros enteros o decimales)")
            else:
                messagebox.showerror("Error", "Ingrese caracteres validos (numeros enteros o decimales)")

#creamos una ventana
ventana = Frame(height=250, width=250)
ventana.pack(padx=5, pady=5)

#creamos las etiquetas
etiqueta1 = Label(text="Variable a:").place(x=0, y=0)
etiqueta2 = Label(text="Variable b:").place(x=0, y=20)
etiqueta3 = Label(text="Variable c:").place(x=0, y=40)
etiqueta4 = Label(text="Resultado:").place(x=0, y=60)

#creamos una variable asignada a un campo para registrar la informacion
vartxt1 = StringVar()
txt1 = Entry(ventana, textvariable=vartxt1).place(x=130, y=0)
vartxt2 = StringVar()
txt2 = Entry(ventana, textvariable=vartxt2).place(x=130, y=20)
vartxt3 = StringVar()
txt3 = Entry(ventana, textvariable=vartxt3).place(x=130, y=40)
vartxt4 = StringVar()
txt4 = Entry(ventana, textvariable=vartxt4, ).place(x=130, y=60)

#creamos los botones y les asignamos las funciones
bResolver = Button(ventana, command=recogerVariables, text="Resolver", padx=42, pady=5).place(x=0, y=130)
bLimpiar = Button(ventana, command=botonLimpiar, text="Limpiar", padx=42, pady=5).place(x=0, y=170) #Listo

ventana.mainloop()