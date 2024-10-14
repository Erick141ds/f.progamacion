'''
ejercicio 3:
programa que calcula la hipotenusa a partir de los 
dos catetos
entrada:
catetoA: int -> a
catetoB: int -> b
salidas:
Hipogtenusa: float -> c
Analisis: se utiliza el teorama de pitagoras
'''
a = input("esscribe el valor del cateto A: ")
a = int(a)
b = input("escribe el valor del cateto B: " )
b = int(b)
c = (a * a + b * b) ** (1/2)
c = match.sqrt(a * a + b * b)
print("el valor de la ipotenusa es: ",c)
