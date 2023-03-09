# Operadores logicos: and, or, not
# AND es para cuando tenemos 2 condiciones y se tienen que cumplir ambas
# OR es para cuando tenemos 2 condiciones y se puede cumplir una o la otra
# NOT vuelve algo que era falso en verdadero

billetera = True
plata = True

if billetera and plata:
    # al usar and ambos tienen que ser true para que el if evalue la totalidad en true
    print("Podes comprar")

sarten_caliente = True
manteca = False

if sarten_caliente or manteca:
    # En el caso de que uno de los valores sea true el if evaluea como true la totalidad
    print("Se puede cocina")

nafta = False
encendido = True
edad = 18

if not nafta and encendido and edad >= 18:
    print("Podes manejar")
