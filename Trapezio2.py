def Trapezio(f, a, b, n):
    h = (b - a) / n  
    x_values = [a + i * h for i in range(n+1)] 
    y_values = [f(x) for x in x_values]

    integral = (h/2) * (y_values[0] + 2 * sum(y_values[1:n]) + y_values[n])
    return integral

def funcao(x):
    return x**2 + (1/x)

a = 1.0
b = 1.2
n = 1
resultado = Trapezio(funcao, a, b, n)

print(f"Valor aproximado da integral: {resultado:.4f}")