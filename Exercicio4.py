
import math

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
x = (b**2) - (4 * a * c)
d = math.sqrt(x)
div = 2 * a 
y = (-b + d) / div
z = (-b - d) / div
print("O valor de delta é {0}".format(d))
print("O valor de x é: {0}, e o valor de y é: {1}".format(y, z))

