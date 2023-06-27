import math

def funcao(x):
   return math.exp(-x ** 2)

def Primeirasimpson(a, b, n):
   if n < 0 or n % 2 != 0:
      return "erro!"
   h = (b - a) / n
   soma_impar, soma_par = 0 ,0
   for k in range(1,n,2):
      soma_impar += funcao(a + k * h)
   for k in range(2, n, 2):
      soma_par += funcao(a + k * h)
   return (h/3) * (funcao(a) + 4 * soma_impar + 2 * soma_par + funcao(b))

a = 1.6
b = 2
n = 2

print(f"Resultado pela Primeira Regra de Simpson (aproximadamente): {Primeirasimpson(a, b, n):.4f}")
