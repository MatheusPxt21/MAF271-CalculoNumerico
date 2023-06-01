import numpy as np

def Metodo_NEWTON(f, f_function, xZero, iteracoesMAX, tolerancia):
    x = xZero
    iteracoes = 0
    erro = tolerancia + 1
    
    while iteracoes < iteracoesMAX and erro > tolerancia:
        F = f(x)
        f_aux = f_function(x)
        
        if f_aux == 0:
            print("A derivada e zero. Nao e possivel continuar.")
            return None
        
        x_aux = x - F / f_aux
        erro = abs(x_aux - x)
        x = x_aux
        iteracoes += 1
    
    if iteracoes == iteracoesMAX:
        print("Maximo de iteracoes alcancado!")
    else:
        print("Convergiu em", iteracoes, "iteracoes.")
    
    return x

def f(x):
    return x**2 - 4

def f_function(x):
    return 2*x

xZero = 1.5
iteracoesMAX = 100
tolerancia = 1e-6

raiz = Metodo_NEWTON(f, f_function, xZero, iteracoesMAX, tolerancia)

print("Raiz:", raiz)