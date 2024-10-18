'''
Dado un número de dos cifras, diseñe un algoritmo que permita obtener el 
número invertido.
entadas:
dijito1:
dijito2:
salidas:
numeroin:
'''
ni = int(input("escibe el numero: "))
d1 = int(input("escribe el dijito1: "))
d2 = int(input("escribe el dijito2: "))
d1 = ( ni / 10 )
d2 = ( ni % 10 )
iv = ( d2 * 10 + d1 )
print("el inveriso de n1 es: ",iv)
