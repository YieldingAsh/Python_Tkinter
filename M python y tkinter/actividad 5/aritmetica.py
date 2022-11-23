from msvcrt import getch

def suma():
    num1=int(input('Ingrese el primer numero: '))
    num2=int(input('Ingrese el segundo numero: '))
    res=num1+num2
    print('La suma de {} y {} es igual a {}'.format(num1, num2, res))
    getch()

def resta():
    num1=int(input('Ingrese el primer numero: '))
    num2=int(input('Ingrese el segundo numero: '))
    res=num1-num2
    print('La resta de {} y {} es igual a {}'.format(num1, num2, res))
    getch()

def multiplicacion():
    num1=int(input('Ingrese el primer numero: '))
    num2=int(input('Ingrese el segundo numero: '))
    res=num1*num2
    print('La multiplicacion de {} y {} es igual a {}'.format(num1, num2, res))
    getch()

def division():
    num1=int(input('Ingrese el primer numero: '))
    num2=int(input('Ingrese el segundo numero: '))
    res=num1/num2
    print('La division de {} y {} es igual a {}'.format(num1, num2, res))
    getch()