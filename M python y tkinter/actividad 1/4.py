n = 3
suma = 0 
i = 1
while (i<= n):
    print ("Ingrese la nota numero: ", i)
    nota = float(input())
    suma = suma+nota
    i+=1
    prom=suma/n
    print("el promedio de notas es: ",prom)