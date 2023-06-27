import math

def funcao(x):
   return math.exp(-x ** 2)

def SegundaSimpson(a, b, n):
    if n < 0 or n % 3 != 0:
      return "erro!"
    h = (b - a) / n
    soma_impar, soma_par = 0 ,0
    for k in range(1,n,2):
      soma_impar += funcao(a + k * h)
    for k in range(2, n, 2):
      soma_par += funcao(a + k * h)
    return ((3 * h) / 8) * (funcao(a) + 3 * soma_impar + 3 * soma_par + 2 * funcao(b))

a = 1.6
b = 2
n = 3

print(f"\n\nResultado pela Segunda Regra de Simpson (aproximadamente): {SegundaSimpson(a, b, n):.4f}")