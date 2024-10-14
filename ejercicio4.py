'''
dado 2 numeros , mostrar la suma, resta, divicion, y multiplicación de ambos 
entrada:
nemero1: int -> a
nemero2: int -> b
salida: float -> c
suma: float -> c
resta: float -> c
divición: float -> c
multiplicación: float -> c
'''
a = input("escribe el valor del numero1: ")
a = int(a)
b = input("escribe el valor del numero2: ")
b = int(b)
suma = ( a + b )
resta = ( a - b )
divición = ( a / b )
multiplicación = ( a * b )
print("el valor de la suma es: ",suma)
print("el valor de la resta es: ",resta)
print("el valor de la divición es: ",divición)
print("el valor de la multiplicación es: ", multiplicación)