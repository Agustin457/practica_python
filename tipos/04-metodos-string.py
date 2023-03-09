animal = "  chanCHito feliz  "
print(animal.upper())
# upper es un metodo que tranfoma el texto en letras mayusculas
print(animal.lower())
print(animal.capitalize())
# capitalize lo que hace es pone la primera letra del texto en mayuscula y el resto en minuscula
print(animal.title())
# title lo que hace es que
print(animal.strip())
# strip remueve todos los espacios en blanco que se encuentras a la izq y a la derecha de mi texto
# strip tiene su variente de lstrip para los espacios de la izquierda y rstrip para los de la derecha
# Aca estamos viendo un metodo, un metodo es una funcion que se encuentra dentro de un objeto
print(animal.strip().capitalize())
# Como dejo de funcional el capitalize ya que la primera letra es un espacio colocamos un strip antes del capitalize para solucionar estre problema
# Aprendemos encadenar los metodos
subcadena = "CH"
print(animal.find(subcadena))
# Find utiliza para ubicar la posicion caracteres en espesifico, tambien se puede buscar otra variable
# Al no encontrar lo que busca te devuelve un resultado negativo, sirve para sacar el indice(donde se encuentra)
print(animal.replace("nCH","j"))
# Como dice su nombre busca reemplaza texto de la string inicial por lo que nosotros querramos
# Replace necesita 2 argumento, los caracteres que queres remplazar, y luego el valor que vas a remplazar
print("nCH" in animal)
# in se utiliza para saber si estos caracteres se encuentran en la strin o no
print("nCH" not in animal)
# en este caso es lo contrario, ambos metodos devuelven boolean
