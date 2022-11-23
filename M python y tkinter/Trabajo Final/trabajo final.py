from tkinter import *
import tkinter
import os
from setuptools import command
import psutil

def eliminar():
        for process in psutil.process_iter():
            if process.name() == entrada.get():
                os.system("taskkill /im " + str(process.pid))
                lista_elementos.delete(0,END)
                test()
                entrada.set("")





def test():
    lista_elementos.delete(0,END)
    for process in psutil.process_iter():
        pInfoDict =  process.as_dict(attrs=['pid', 'memory_percent', 'name', 'create_time'])
        lista_elementos.insert(END, pInfoDict)



ventana=Tk()
ventana.geometry("600x400")
ventana.title("Visualisador de procesos")

lista_elementos=Listbox(ventana,width=150,height=50)

lista_elementos.place(x=100,y=120)
lista_etiq=Label(ventana,text="Lista de Procesos").place(x=100,y=100)

entrada=StringVar()
entrada_texto=Label(ventana,text="Escriba ej(proceso.exe) para terminar un proceso").place(x=150,y=5)
entrada_elementos=Entry(ventana,text=entrada,width=40).place(x=150,y=25)

boton_añadir=Button(ventana,text="Terminar Proceso",heigh=2,width=18,command=eliminar).place(x=410,
y=15)

btn_limpiar=Button(ventana, text="Visualizar procesos", width=40, command=test).place(x=100, y=60)

ventana.mainloop()