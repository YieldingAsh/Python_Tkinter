from msvcrt import getch
from aritmetica import *
from contable import *
from geometria import *

op1='Y'
while op1 == 'Y':
    print('\nEleguir que operacion quiere hacer:'.center(50))
    print('\n[A] Aritmetica')
    print('\n[B] Contable')
    print('\n[C] Geometria')
    print('\n[D] Salir')
    op2=int(input('\nEscriba su eleccion: '))
    if(op2=='A'):
        print('\n')
        print('\nLas operaciones son:')
        print('\n[A] Suma')
        print('\n[B] Resta')
        print('\n[C] Division')
        print('\n[D] Multiplicacion')
        op3=(input('\nEscriba su eleccion:  '))
        if(op3=='A'):
            print('\n')
            suma()
        elif(op3=='B'):
            print('\n')
            resta()
        elif(op3=='C'):
            print('\n')
            division()
        elif(op3=='D'):
            print('\n')
            multiplicacion()
        else:
            print('\nIngrese otra opcion')
    elif(op2=='B'):
        print('\n')
        print('\nLas operaciones son:')
        print('\n[A] Porcentaje')
        print('\n[B] Descuento')
        print('\n[C] Incremento')
        print('\n[D] Interes simple')
        print('\n[E] Aporte jubilatorio')
        print('\n[F] Aporte obra social')
        print('\n[G] Aporte sindicato')
        print('\n[H] Promedio')
        print('\n[I] Valor en 12 cuotas sin interes')
        print('\n[J] Valor en cuotas con interes fijado')
        op3=(input('\nEscriba su eleccion: '))
        if(op3=='A'):
            print('\n')
            porcentaje()
        elif(op3=='B'):
            print('\n')
            descuento()
        elif(op3=='C'):
            print('\n')
            incremento()
        elif(op3=='D'):
            print('\n')
            interes_simple()
        elif(op3=='E'):
            print('\n')
            aporte_jubilatorio()
        elif(op3=='F'):
            print('\n')
            aporte_obra_social()
        elif(op3=='G'):
            print('\n')
            aporte_sindicato()
        elif(op3=='H'):
            print('\n')
            promedio()
        elif(op3=='I'):
            print('\n')
            cuotas_sin_interes_12()
        elif(op3=='J'):
            print('\n')
            cuotas_con_interes()
        else:
            print('\nIngrese otra opcion')
    elif(op2=='C'):
        print('\n')
        print('\nLas operaciones son:')
        print('\n[A] Perimetro de un cuadrado')
        print('\n[B] Area de un cuadrado')
        print('\n[C] Perimetro de un rectangulo')
        print('\n[D] Area de un rectangulo')
        print('\n[E] Perimetro de un triangulo')
        print('\n[F] Area de un triangulo')
        print('\n[G] Perimetro de un rombo')
        print('\n[H] Area de un rombo')
        print('\n[I] Perimetro de un paralelogramo')
        print('\n[J] Area de un paralelogramo')
        print('\n[K] Perimetro de un trapecio')
        print('\n[L] Area de un trapecio')
        print('\n[M] Perimetro de un poligono regular')
        print('\n[N] Area de un poligono regular')
        print('\n[O] Perimetro de un circulo')
        print('\n[P] Area de un circulo')
        op3=(input('\nEscriba su eleccion: '))
        if(op3=='A'):
            print('\n')
            peri_cuadrado()
        elif(op3=='B'):
            print('\n')
            area_cuadrado()
        elif(op3=='C'):
            print('\n')
            peri_rectangulo()
        elif(op3=='D'):
            print('\n')
            area_rectangulo()
        elif(op3=='E'):
            print('\n')
            peri_triangulo()
        elif(op3=='F'):
            print('\n')
            area_triangulo()
        elif(op3=='G'):
            print('\n')
            peri_rombo()
        elif(op3=='H'):
            print('\n')
            area_rombo()
        elif(op3=='I'):
            print('\n')
            peri_paralelogramo()
        elif(op3=='J'):
            print('\n')
            area_paralelogramo()
        elif(op3=='K'):
            print('\n')
            peri_trapecio()
        elif(op3=='L'):
            print('\n')
            area_trapecio()
        elif(op3=='M'):
            print('\n')
            peri_poligono()
        elif(op3=='N'):
            print('\n')
            area_poligono()
        elif(op3=='O'):
            print('\n')
            peri_circulo()
        elif(op3=='P'):
            print('\n')
            area_circulo()
        else:
            print('\nIngrese otra opcion')
    elif(op2=='D'):
        op1 = 'N'
    else:
        print('\nIngrese otro opcion')
    op1=input('\n¿Desea hacer otra operacion? Y / N: ')
getch()