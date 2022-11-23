from tkinter import *
import tkinter
from setuptools import command

ventana=Tk()
ventana.geometry("600x400")
ventana.title("Cambiar Color del Fondo")
ventana.configure(bg='blue')

def Verde():
    ventana.configure(bg='green')

def Rojo():
    ventana.configure(bg='red')

def Azul():
    ventana.configure(bg='blue')

boton_añadir=Button(ventana,text="Verde",heigh=2,width=18,command=Verde,bg='green').place(x=100,y=15)

boton_añadir2=Button(ventana,text="Rojo",heigh=2,width=18,command=Rojo,bg='red').place(x=200,y=15)

boton_añadir3=Button(ventana,text="Azul",heigh=2,width=18,command=Azul,bg='blue').place(x=300,y=15)

ventana.mainloop()