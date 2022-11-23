
from turtle import clear


mi_lista = ["Rosa",57,25,11,64]
print(mi_lista)
print(mi_lista[1])

mi_lista.append("sagitario")
print(mi_lista)

mi_lista[2],mi_lista[3] = mi_lista[3], mi_lista[2]
print(mi_lista)

mi_lista[0] = 64
mi_lista[4] = "Rosa"
print(mi_lista)

print(mi_lista[::-1])

print(mi_lista[3:])

print(mi_lista[:2])

print(mi_lista[-4])

print(mi_lista[-2])

print(mi_lista[0:4])

mi_lista.clear()
print(mi_lista)
