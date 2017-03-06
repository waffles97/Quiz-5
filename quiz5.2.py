import math
def max_three(a, b, c):
    return max(a, max(b ,c))

a = float(input('Dame el valor de "a": '))
b = float(input('Dame el valor de "b": '))
c = float(input('Dame el valor de "c": '))
maximo = max_three(a,b,c)

print("El valor maximo de la lista es: ", maximo)
