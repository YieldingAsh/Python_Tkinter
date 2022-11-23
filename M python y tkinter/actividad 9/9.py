from tkinter import *
import tkinter
from setuptools import Command

def agregar():
    lista_elementos.insert(END, entrada.get())
    entrada.set(' ')

def borrar():
    for i in lista_elementos.curselection():
        lista_elementos.delete(i)

ventana=Tk()
ventana.geometry("600x400")
ventana.title("Lista")

lista_elementos=Listbox(ventana,width=50)

lista_elementos.place(x=100,y=120)
lista_etiq=Label(ventana,text="Lista de Elementos").place(x=100,y=100)

entrada=StringVar()
entrada_elementos=Entry(ventana,text=entrada,width=40).place(x=150,y=20)

boton_añadir=Button(ventana,text="Agregar",heigh=2,width=18,command=agregar).place(x=400,y=60)

btn_limpiar=Button(ventana,text="Eliminar",width=40, command=borrar).place(x=100, y=60)

ventana.mainloop()