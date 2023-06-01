import numpy as np

def Metodo_JACOBI(A, b, Max_Iteracoes, tolerancia):
    N = A.shape[0]
    x = np.zeros(N)
    x_aux = np.zeros(N)
    iteracoes = 0
    erro = tolerancia + 1
    while iteracoes < Max_Iteracoes and erro > tolerancia:
        for i in range(N):
            sum_term = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x_aux[i] = (b[i] - sum_term) / A[i, i]
        erro = np.linalg.norm(x_aux - x)
        x = np.copy(x_aux)
        iteracoes += 1
    if iteracoes == Max_Iteracoes:
        print("Maximo de iteracoes alcancado!")
    else:
        print("Convergiu em", iteracoes, "iteracoes.")
    return x

A = np.array([[15, 5, -5],
              [4, 10, 1],
              [2, -2, 8]])
b = np.array([30, 23, -10])
Max_Iteracoes = 100
tolerancia = 1e-6
RESULTADO = Metodo_JACOBI(A, b, Max_Iteracoes, tolerancia)
print("RESULTADO:", RESULTADO)