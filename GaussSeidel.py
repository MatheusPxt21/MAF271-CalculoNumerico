import numpy as np

def MET_GAUSSSEIDEL(A, b, inicial, MAXIMO_iteracoes, tolerancia):
    N = len(A)
    x = inicial.copy()
    iteracoes = 0
    erro = tolerancia + 1
    while iteracoes < MAXIMO_iteracoes and erro > tolerancia:
        x_prev = x.copy()
        for i in range(N):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], x_prev[i+1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        erro = np.linalg.norm(x - x_prev)
        iteracoes += 1
    if iteracoes == MAXIMO_iteracoes:
        print("Maximo de iteracoes atingidas")
    else:
        print("Convergiu em", iteracoes, "iteracoes.")
    return x

A = np.array([[4, -1, 1],
              [2, 7, 1],
              [1, 1, 3]])

b = np.array([3, 19, 1])
inicial = np.zeros(len(b))
MAXIMO_iteracoes = 100
tolerancia = 1e-6
resultado = MET_GAUSSSEIDEL(A, b, inicial, MAXIMO_iteracoes, tolerancia)
print("Resultado:", resultado)