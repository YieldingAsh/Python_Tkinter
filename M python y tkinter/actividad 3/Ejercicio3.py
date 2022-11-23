from pip import main

kiniela_ganadora = ['3','5','4','5','3']
texto = ["Ingrese su primer numero:","Ingrese su segundo numero:","Ingrese su tercer numero:","Ingrese su cuarto numero:","Ingrese su quinto numero:",]
kiniela = []

L = "1"
i = 0
while i < 5:
    L = (input(""))
    if L < "10" or L > "0":
        if L.isdigit():
            print ("Se subio correctamente")
            kiniela.append(L)
            i += 1
        else:
            print("Pone un numero y positivo porfavor")
            main
    else:
        print("Ponga un numero entre 0 y 10 porfavor")
        main

print("Tu kiniela es:",kiniela)
if kiniela == kiniela_ganadora:
    print("Tu kiniela es la kiniela ganadora")
    kiniela.sort()
    print("Tu kiniela ordena:",kiniela)
    exit()
else:
    print("Tu kiniela no es la kiniela ganadora, mejor suerte la proxima")
    kiniela.sort()
    print("Tu kiniela ordena:",kiniela)
    exit()
