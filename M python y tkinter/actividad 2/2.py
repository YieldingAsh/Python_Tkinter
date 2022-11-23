import string


cadena = "esta es mi Aplicacion"
print (cadena.capitalize()) #Convierte la primera letra de la cadena en mayuscula
print (cadena.lower()) #Convierte una cadena en minusculas 
print (cadena.upper()) #Covierte una cadena en mayusculas
print (cadena.swapcase()) #Convierte mayusculas a minusculas y minusculas a mayusculas
print (cadena.title()) #Convierte una cadena en formato de titulo
print (cadena.center(50, '=')) #Centra el texto
print (cadena.ljust(50, '='))  #Alinear texto a la izquierda 
print (cadena.rjust(50, '=')) #Alinear texto a la derecha
print (cadena.zfill(12)) #Rellenar un tecto anteponiendo ceros
print (cadena.count("a")) #Contar cantidad de apariciones de una subcadena
print (cadena.find("mi",0 ,10 )) #Buscar una subcadna entro de una cadena
print (cadena.startswith("Bienvenido")) #Saber si una cadena comienza con una subcadena determinada
print (cadena.isalnum()) #Saber si una cadena es alfanumerica
print (cadena.isalpha()) #Saber si una cadena es alfabetica
print (cadena.isdigit()) #Saber si una cadena es numerica
print (cadena.islower()) #Saber si una cadena contiene solo minusculas
print (cadena.isupper()) #Saber si una cadena contiene solo mayusculas
print (cadena.isspace()) #Saber si una cadena solo espacios en blanco
print (cadena.istitle()) #Saber si una cadena tiene formato de titulo
print (cadena.format("en Minecraft")) #Dar formato a una cadena, subtituyendo texto dinamicamente 
print (cadena.replace(cadena, "nashe")) #Remplazar texto en una cadena
cadenan = "      nashe       "
print (cadenan.strip(' ')) #Elimina caracteres de los dos lados de una cadena
print (cadenan.lstrip(" na" )) #Elimina caracteres a la izqauierda de una cadena
print (cadenan.rstrip("he ")) #Elimina caracteres a la derecha de una cadena
print ('a' in 'manzana') #Comprueba si la subcadena que se solicita esta en una cadena

C=(input("Ingrese un texto para centrar:"))
print(C.center(50,"="))