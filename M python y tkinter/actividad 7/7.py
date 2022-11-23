from audioop import mul
from tkinter import Tk, Label, Button, Entry
ventana = Tk()
ventana.title("Ejemplo con place")
ventana.geometry("500x300")
ventana.colormapwindows
ventana.configure(background="#006")

def sumar(): 
    n1 = int(txt1.get())
    n2 = int(txt2.get())
    r = n1 + n2
    txt3.delete(0, 'end')
    txt3.insert(0,r)

def restar():
    n1 = int(txt1.get())
    n2 = int(txt2.get())
    r = n1 - n2
    txt3.delete(0, 'end')
    txt3.insert(0,r)

def divi():
    n1 = int(txt1.get())
    n2 = int(txt2.get())
    r = n1 / n2
    txt3.delete(0, 'end')
    txt3.insert(0,r)

def multi():
    n1 = int(txt1.get())
    n2 = int(txt2.get())
    r = n1 * n2
    txt3.delete(0, 'end')
    txt3.insert(0,r)

def potencia():
    n1 = int(txt1.get())
    n2 = int(txt2.get())
    r = n1 ** n2
    txt3.delete(0, 'end')
    txt3.insert(0,r)

def clear():
    txt3.delete("0","end")
    txt2.delete("0","end")
    txt1.delete("0","end")

btn7= Button(ventana, text="Quit", bg="yellow", command= ventana.quit)
btn7.place(x=300, y=220, width=100, height=30)

lbl1 = Label(ventana, text="Primer numero", bg="cyan")
lbl1.place(x=10, y=10, width=100, height=30)
lbl2 = Label(ventana, text="Segundo numero", bg="cyan")
lbl2.place(x=10, y=60, width=100, height=30)
lbl3 = Label(ventana, text="Resultado", bg="cyan")
lbl3.place(x=250, y=35, width=100, height=30)
txt1 = Entry(ventana, text="Primer numero", bg="orange")
txt1.place(x=120, y=10, width=100, height=30)
txt2 = Entry(ventana, text="Segundo numero", bg="orange")
txt2.place(x=120, y=60, width=100, height=30)
txt3 = Entry(ventana, text="Resultado", bg="orange")
txt3.place(x=360, y=35, width=100, height=30)
btn1 = Button(ventana, text="+", bg="green", command=sumar)
btn1.place(x=20, y=120, width=50, height=30)
btn2 = Button(ventana, text="-", bg="green", command=restar)
btn2.place(x=120, y=120, width=50, height=30)
btn3 = Button(ventana, text="/", bg="green", command=divi)
btn3.place(x=220, y=120, width=50, height=30)
btn4 = Button(ventana, text="X", bg="green", command=multi)
btn4.place(x=320, y=120, width=50, height=30)
btn5 = Button(ventana, text="↑", bg="green", command=potencia)
btn5.place(x=420, y=120, width=50, height=30)
btn6 = Button(ventana, text="CLEAR", bg="red", command=clear)
btn6.place(x=200, y=220, width=100, height=30)
ventana.mainloop()