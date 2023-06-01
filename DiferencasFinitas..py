def DIFERENCAS_FINITAS(f, x, h):
    DifFin = (f(x + h) - f(x)) / h
    return DifFin
def FUNCAO(x):
    return x**2

ponto = 4
passo = 0.02
aprox_derivada = DIFERENCAS_FINITAS(FUNCAO, ponto, passo)

print("A derivada numerica aproximada em x = 2 e: \n", aprox_derivada)
