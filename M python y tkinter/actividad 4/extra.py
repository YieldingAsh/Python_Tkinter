from re import A

from pip import main


alumnos = []
i = 1
L = 0
int = 10    

while i < 11:
    print("Ingresar la nota del alumno numero",i,":")
    L=(input(""))
    if L > 10:
        print(L)
        if 12 > 10:
            print("Ponga un numero alrededor de 0 o 10 porfavor")
            main
        else:
            alumnos.append(L)
            i += 1
    else:
        print("Ingrese un numero y que se positivo por favor")
        main 

i = 1
o = 0
A = 0
D = 0
while i < 11:
    print("El alumno numero",i,":")
    if alumnos[o] > "7" or alumnos[o] == "7":
        print("Nota:",alumnos[o])
        print("Aprobado")
        i += 1
        o += 1
        A += 1
    else:
        print("Nota:",alumnos[o])
        print("Desaprobado")
        i += 1
        o += 1
        D += 1

print("Alumnos totales aprobados:",A,", Alumnos totales desaprobados",D)

