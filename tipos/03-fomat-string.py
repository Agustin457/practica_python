#Concatenacion se STRINGS
nombre = "Agustin"
apellido = "Belizan"

nombre_completo = nombre + " " + apellido
print(nombre_completo)

#Como deberia de hacer concatenacion de strings
nombre_completo2 = f"{nombre} {apellido}"
print (nombre_completo2)
#De esta manera usando F se pueden concatenar 2 variable de manera mas facil
#F es un operador donde se pueden concatenar vairables y expreciones como 2 + 2
nombre_completo3 = f"{nombre} {2 +2}"
print(nombre_completo3)
#otra variante de lo mismos podria ser
nombre_completo4 = f"{nombre[0:3]} {2 +2}" 
print(nombre_completo4)