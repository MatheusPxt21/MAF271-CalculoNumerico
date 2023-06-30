def Trapezio(f, a, b, n):
    h = (b-a)/n
    valor_x = [a + i * h for i in range(n-1)]
    valor_y = [f(x) for x in valor_x]

    Inter = (h/2) * (valor_y[0] + 2 * sum(valor_y[1:n]) + valor_y[n])
    return Inter

def funcao(x):
    return x**2 + (1/x)

a = 1.0
b = 1.2
n = 1

resultado = Trapezio(funcao, a, b, n)
print(f"O valor aproximado da integral é: {resultado}")

#esta dando erro