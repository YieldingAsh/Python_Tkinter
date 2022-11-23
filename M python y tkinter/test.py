from tkinter import *
raiz = Tk()
raiz.geometry("800x850")
mi_Frame = Frame() #Creacion del Frame
mi_Frame.pack()  #Empaquetamiento del Frame
mi_Frame.config(bg="purple") #cambiar color de fondo 
mi_Frame.config(bd=7) #cambiar el grosor del borde
mi_Frame.config(relief="sunken")   #cambiar el tipo de borde
mi_Frame.config(cursor="heart")    #cambiar el tipo de cursor
mi_Frame.place(relx=0.05,rely=0.1, relwidth=0.31, relheight=0.6) 
mi_Frame4 = Frame() #Creacion del Frame
mi_Frame4.pack()  #Empaquetamiento del Frame
mi_Frame4.config(bg="purple") #cambiar color de fondo
mi_Frame4.config(bd=7) #cambiar el grosor del borde
mi_Frame4.config(relief="sunken")   #cambiar el tipo de borde
mi_Frame4.config(cursor="heart")    #cambiar el tipo de cursor
mi_Frame4.place(relx=0.85,rely=0.1, relwidth=0.31, relheight=0.6) 
mi_Frame3 = Frame() #Creacion del Frame
mi_Frame3.pack()  #Empaquetamiento del Frame
mi_Frame3.config(bg="purple") #cambiar color de fondo 
mi_Frame3.config(bd=7) #cambiar el grosor del borde
mi_Frame3.config(relief="sunken")   #cambiar el tipo de borde
mi_Frame3.config(cursor="heart")    #cam biar el tipo de cursor
mi_Frame3.place(relx=0.85 ,rely=0.1, relwidth=0.31, relheight=0.6) 
mi_Frame2 = Frame() #Creacion del Frame
mi_Frame2.pack()  #Empaquetamiento del Frame
mi_Frame2.config(bg="red") #cambiar color de fondo 
mi_Frame2.config(bd=7) #cambiar el grosor del borde
mi_Frame2.config(relief="sunken")   #cambiar el tipo de borde
mi_Frame2.config(cursor="heart")    #cambiar el tipo de cursor 
mi_Frame2.place(relx=0.05,rely=0.6, relwidth=0.91, relheight=0.3)
raiz.mainloop()