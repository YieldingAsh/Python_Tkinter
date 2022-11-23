import tkinter
import random
  
colours = ['A','B','C','D','F',
           'G','H','I','E','O']
colours2 = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','Gray','Purple','Brown']
colours3 = ['Rojo','Azul','Verde','Rosa','Negro',
           'Amarillo','Naranja','Gris','Violeta','Marron']
score = 0
numeros = [0,1,2,3,4,5,6,7,8,9]
i = 0
  
timeleft = 60
  
def startGame(event):
      
    if timeleft == 60:
          
        countdown()
          
    nextColour()

def nextColour():

    global score
    global timeleft
  
    if timeleft > 0:
        
        global i
        e.focus_set()
        if e.get().lower() == colours3[i].lower():
              
            score += 1
        
        e.delete(0, tkinter.END)

        random.shuffle(numeros)
        i = numeros[1]
        random.shuffle(colours)

        label.config(fg = str(colours2[i]), text = str(colours[0]))
          
        scoreLabel.config(text = "Score: " + str(score))

def countdown():

    global score
    global timeleft
    global i
  
    if timeleft > 0:
  
        timeleft -= 1
    
        timeLabel.config(text = "Tiempo Restante: "
                               + str(timeleft))
                                 
        timeLabel.after(1000, countdown)
  
root = tkinter.Tk()
  
root.title("COLORGAME")
  
root.geometry("375x200")
  
instructions = tkinter.Label(root, text = "Escribir el nombre del color",
                                      font = ('Helvetica', 12))
instructions.pack()
scoreLabel = tkinter.Label(root, text = "Aprieta enter para empezar",
                                      font = ('Helvetica', 12))
scoreLabel.pack()
  
timeLabel = tkinter.Label(root, text = "Time left: " +
              str(timeleft), font = ('Helvetica', 12))
                
timeLabel.pack()
  
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()
  
e = tkinter.Entry(root)
  
root.bind('<Return>', startGame)
e.pack()
  
e.focus_set()
  
root.mainloop()