'''
pragrama que calcule el area y el perimetro de un rectangulo
a partir de su base y su altura 
entradas:
base: integer
altura: integer
salidas:
perimetro: integer
area: integer
Analisis:
se require calcular con las formulas para area y perimetro
'''
##imput siempre regresa un  string
## para tratarlo como otro dato se debe convertir 
base = input('escribe la base del rectangulo: ')
base = int(base)
altura = input('escrive la altura del rectangulo: ')
altura = int(altura)
area = base * altura
perimetro = base + base + altura + altura 
perimetro = (base + altura) * 2
print('El area del rectangulo es ' + str(area))
print('El perimetro del rectangulo es', perimetro)