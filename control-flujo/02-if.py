# Si un usuario es mayor a 55 corresponde descuento

"""usuario = input("Edad del usuario: ")
usuario = int(usuario)
if usuario >= 55:
    print("Corresponde descuento")"""

# Si es mayor igual de 18 puede ver la pelicula
"""edad = input("Indique su edad: ")
edad = int(edad)
if edad >= 18:
    print("Puede ver la pelicula")
else:
    print("No puede ver la pelicula")"""
# Si no endentamos o hacemos TAB luego de un if o else no va reconocel el codigo consecuente

# Si es mayor de 18, y descuento si es mayor a 55
edad = input("Indique su edad: ")
edad = int(edad)
if edad >= 55:
    print("Puede ver la pelicula, tiene descuento.")
elif edad >= 18:
    print("Puede ver la pelicula.")
else:
    print("No puede ver la pelicula.")
# Los datos dentro de las funciones if se evaluan de arriba para abajo.
# Lo que quiere decir que si el primer if es verdadero el resto de los if,elif y else seren decestimados.
# El orden en el cual coloquemos los datos en el else if es sumamente importante debido a esto.
# Se pueden tener una cantidad infinita de elif
