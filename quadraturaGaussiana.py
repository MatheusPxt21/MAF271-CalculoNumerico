import math

def quadratura_gaussiana(funcao, a, b, n):
    coeficientes = {
        2: [1, 1],
        3: [0.555555556, 0.888888889, 0.555555556],
        4: [0.3478548451, 0.6521451549, 0.6521451549, 0.3478548451],
        5: [0.2369268850, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268850]
    }
    nos = {
        2: [-0.5773502692, 0.5773502692],
        3: [-0.7745966692, 0, 0.7745966692],
        4: [-0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116],
        5: [-0.9061798459, -0.5384693101, 0, 0.5384693101, 0.9061798459]
    }
    def f(x):
        return eval(funcao)
    integral = 0
    for i in range(n):
        xi = ((b - a) * nos[n][i] + (b + a)) / 2
        integral += coeficientes[n][i] * f(xi)
    
    integral *= (b - a) / 2
    
    return integral

funcao = "math.sin(x)"
inferior = 0
superior = math.pi
ordem = 5 

resultado = quadratura_gaussiana(funcao, inferior, superior, ordem)
print(f"\n\nResultado por Quadratura Gaussiana (aproximadamente): {resultado:.4f}")