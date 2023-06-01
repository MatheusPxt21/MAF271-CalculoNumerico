x = [1, 2, 3, 4]
y = [2, 5, 1, 3]

def DIFERENCAS_DIVIDIDAS(x, y):
    N = len(x)
    coeficientes = [y[0]] + [0] * (N - 1)

    for i in range(1, N):
        for j in range(N - 1, i - 1, -1):
            y[j] = (y[j] - y[j - 1]) / (x[j] - x[j - i])

    for i in range(N):
        coeficientes[i] = y[i]

    return coeficientes

coeficientes = DIFERENCAS_DIVIDIDAS(x, y)
print("\n========DIFERENCAS DIVIDIDAS==============\n\n")
print(coeficientes)
