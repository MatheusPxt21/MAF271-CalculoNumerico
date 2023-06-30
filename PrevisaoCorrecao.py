import numpy as np

def previsao(f, y0, h, num_iteracoes):
    t = np.zeros(num_iteracoes+1)
    y = np.zeros(num_iteracoes+1)
    t[0] = 0
    y[0] = y0
    for i in range(num_iteracoes):
        t[i+1] = t[i] + h
        y[i+1] = y[i] + h * f(t[i], y[i])
    return y

def correcao(f, y0, h, num_iteracoes):
    t = np.zeros(num_iteracoes+1)
    y = np.zeros(num_iteracoes+1)
    t[0] = 0
    y[0] = y0
    for i in range(num_iteracoes):
        t[i+1] = t[i] + h
        y[i+1] = y[i] + h * f(t[i+1], y[i+1])
    return y

def equacao(t, y):
    """
    Exemplo de função que define uma equação diferencial y' = f(t, y).
    Neste caso, usamos a equação y' = t - y.
    """
    return t - y

y0 = 1.0
h = 0.1
num_iteracoes = 10
print("\n\nPrevisao - Correcao \n\n")
resultado_explicito = previsao(equacao, y0, h, num_iteracoes)
print(f"(Previsão): \n{resultado_explicito}")
resultado_implicito = correcao(equacao, y0, h, num_iteracoes)
print(f"(Correção): \n{resultado_implicito}")
