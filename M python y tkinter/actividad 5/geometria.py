from math import pi

def peri_cuadrado():
    num1=int(input('Ingrese la medida de uno de los lados de la figura en cm: '))
    res=4*num1
    print('El perimetro del cuadrado equivale a {} cm'.format(res))
def area_cuadrado():
    num1=int(input('Ingrese la medida de uno de los lados de la figura en cm: '))
    res=pow(num1,2)
    print('El area del cuadrado equivale a {} cm'.format(res))

def peri_rectangulo():
    num1=int(input('Ingrese el largo en cm de la figura: '))
    num2=int(input('Ingrese el alto en cm de la figura: '))
    res=(2*num1)+(2*num2)
    print('El perimetro del rectangulo equivale a {} cm'.format(res))
def area_rectangulo():
    num1=int(input('Ingrese la base en cm de la figura: '))
    num2=int(input('Ingrese la altura en cm de la figura: '))
    res=num1*num2
    print('El area del rectangulo equivale a {} cm'.format(res))

def peri_triangulo():
    num1=int(input('Ingrese el primer lado de la figura en cm: '))
    num2=int(input('Ingrese el segundo lado de la figura en cm: '))
    num3=int(input('Ingrese el tercer lado de la figura en cm: '))
    res=num1+num2+num3
    print('El perimetro del triangulo equivale a {} cm'.format(res))
def area_triangulo():
    num1=int(input('Ingrese la base en cm de la figura: '))
    num2=int(input('Ingrese la altura en cm de la figura: '))
    res=(num1*num2)/2
    print('El area del triangulo equivale a {} cm'.format(res))

def peri_rombo():
    num1=int(input('Ingrese la medida de uno de los lados de la figura en cm: '))
    res=4*num1
    print('El perimetro del rombo equivale a {} cm'.format(res))
def area_rombo():
    num1=int(input('Ingrese la diagonal horizontal en cm de la figura: '))
    num2=int(input('Ingrese la diagonal vertical en cm de la figura: '))
    res=(num1*num2)/2
    print('El area del rombo equivale a {} cm'.format(res))

def peri_paralelogramo():
    num1=int(input('Ingrese el largo en cm de la figura: '))
    num2=int(input('Ingrese el alto en cm de la figura: '))
    res=(2*num1)+(2*num2)
    print('El perimetro del paralelogramo equivale a {} cm'.format(res))
def area_paralelogramo():
    num1=int(input('Ingrese la base en cm de la figura: '))
    num2=int(input('Ingrese la altura en cm de la figura: '))
    res=num1*num2
    print('El area del paralelogramo equivale a {} cm'.format(res))

def peri_trapecio():
    num1=int(input('Ingrese el primer lado de la figura en cm: '))
    num2=int(input('Ingrese el segundo lado de la figura en cm: '))
    num3=int(input('Ingrese el tercer lado de la figura en cm: '))
    num4=int(input('Ingrese el cuarto lado  de la figura en cm: '))
    res=num1+num2+num3+num4
    print('El perimetro del trapecio equivale a {} cm'.format(res))
def area_trapecio():
    num1=int(input('Ingrese el lado inferior de la figura en cm'))
    num2=int(input('Ingrese el lado superior de la figura en cm'))
    num3=int(input('Ingrese la altura de la figura en cm'))
    res=((num1+num2)/2)*num3
    print('El area del trapecio equivale a {} cm'.format(res))

def peri_poligono():
    num1=int(input('Ingrese la medida de uno de los lados de la figura en cm: '))
    num2=int(input('Ingrese la cantidad de lados de la figura: '))
    res=num1*num2
    print('El perimetro del poligono regular equivale a {} cm'.format(res))
def area_poligono():
    num1=int(input('Ingrese la medida de uno de los lados de la figura en cm: '))
    num2=int(input('Ingrese la cantidad de lados de la figura: '))
    num3=int(input('Ingrese la apotema (distancia desde el centro hasta el borde) de la figura en cm: '))
    res=((num1*num2)*num3)/2
    print('El area del poligono regular equivale a {} cm'.format(res))

def peri_circulo():
    num1=int(input('Ingrese el radio (distancia desde el centro hasta el borde) de la figura en cm: '))
    res=2*pi*num1
    print('El perimetro del circulo equivale a {} cm'.format(res))
def area_circulo():
    num1=int(input('Ingrese el radio (distancia desde el centro hasta el borde) de la figura en cm: '))
    res=pi*pow(num1,2)
    print('El area del circulo equivale a {} cm'.format(res))