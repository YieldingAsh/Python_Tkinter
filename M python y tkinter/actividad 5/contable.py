#Jubilacion 11%, Obra social 3%, sindicato 1%
#Cuotas: 3 sin interes, 6 15%, 9 25%, 12 35%
def porcentaje():
    num1=int(input('Ingrese el monto: '))
    num2=int(input('Ingrese el numero del porcentaje: '))
    res=(num1*num2)/100
    print('El {}% de {} es {}'.format(num2, num1, res))

def descuento():
    num1=int(input('Ingrese el monto: '))
    num2=int(input('Ingrese el numero del porcentaje de descuento: '))
    res=num1-((num1*num2)/100)
    print('El {}% de descuento, ha convertido el numero de {} a {}'.format(num2, num1, res))

def incremento():
    num1=int(input('Ingrese el monto: '))
    num2=int(input('Ingrese el numero del porcentaje de incremento: '))
    res=num1+((num1*num2)/100)
    print('El {}% de incremento, ha convertido el numero de {} a {}'.format(num2, num1, res))

def interes_simple():
    num1=int(input('Ingrese la cuota del mes: '))
    num2=int(input('Ingrese la cantidad de meses: '))
    if(num2>=4 and num2<=6):
        num3=10
        res=num1+((num1*num3)/100)
        print('El {}% de interes, ha convertido el monto de {} a {}'.format(num3, num1, res))
    elif(num2>=7 and num2<=9):
        num3=20
        res=num1+((num1*num3)/100)
        print('El {}% de interes, ha convertido el monto de {} a {}'.format(num3, num1, res))
    elif(num2>=10 and num2<=12):
        num3=30
        res=num1+((num1*num3)/100)
        print('El {}% de interes, ha convertido el monto de {} a {}'.format(num3, num1, res))
    elif(num2>=13):
        num3=40
        res=num1+((num1*num3)/100)
        print('El {}% de interes, ha convertido el monto de {} a {}'.format(num3, num1, res))
    else:
        num3=0
        res=num1+((num1*num3)/100)
        print('El {}% de interes, ha convertido el monto de {} a {}'.format(num3, num1, res))

def aporte_jubilatorio():
    num1=int(input('Ingrese su salario: '))
    num2=11
    res=(num1*num2)/100
    print('El aporte jubilatorio del {}%, equivale a {} de {}'.format(num2, res, num1))

def aporte_obra_social():
    num1=int(input('Ingrese su salario: '))
    num2=3
    res=(num1*num2)/100
    print('El aporte a la obra social del {}%, equivale a {} de {}'.format(num2, res, num1))

def aporte_sindicato():
    num1=int(input('Ingrese su salario: '))
    num2=1
    res=(num1*num2)/100
    print('El aporte al sindicato del {}%, equivale a {} de {}'.format(num2, res, num1))

def promedio():
    suma=0
    num1=int(input('¿Cuantos numeros desea ingresar?: '))
    for i in range(num1):
        num2=int(input('-{} Ingrese el numero: '.format(i)))
        suma=suma+num2
    res=suma/num1
    print('El promedio de los numeros es igual a {}'.format(res))

def cuotas_sin_interes_12():
    num1=int(input('Ingrese el total de la compra: '))
    res=num1/12
    print('{} en 12 cuotas sin interes es igual a {}'.format(num1, res))

def cuotas_con_interes():
    num1=int(input('Ingrese el total de la compra: '))
    num2=int(input('Ingrese la cantidad de meses: '))
    if(num2>=4 and num2<=6):
        num3=10
        res=(num1/num2)+(num1+num3)/100
        print('El {}% de interes, ha convertido el monto de {} a {}'.format(num3, num1, res))
    elif(num2>=7 and num2<=9):
        num3=20
        res=(num1/num2)+(num1+num3)/100
        print('El {}% de interes, ha convertido el monto de {} a {}'.format(num3, num1, res))
    elif(num2>=10 and num2<=12):
        num3=30
        res=(num1/num2)+(num1+num3)/100
        print('El {}% de interes, ha convertido el monto de {} a {}'.format(num3, num1, res))
    elif(num2>=13):
        num3=40
        res=(num1/num2)+(num1+num3)/100
        print('El {}% de interes, ha convertido el monto de {} a {}'.format(num3, num1, res))
    else:
        num3=0
        res=(num1/num2)+(num1+num3)/100
        print('El {}% de interes, ha convertido el monto de {} a {}'.format(num3, num1, res))
