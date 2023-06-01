import numpy as np

def f(x):
    return x**3 - x - 1

def f_function(x):
    return 3*x**2 - 1

def met_NEWTON_MODIFICADO(f, f_function, x0, iteracoes_MAX, tolerancia):
    x = x0
    iteracoes = 0
    erro = tolerancia + 1
    
    while iteracoes < iteracoes_MAX and erro > tolerancia:
        x_aux = x
        fx = f(x)
        fpx = f_function(x)
        
        if abs(fpx) < tolerancia:
            print("A derivada da função é muito próxima de zero.")
            break
        
        x = x - fx / fpx
        
        erro = abs(x - x_aux)
        iteracoes += 1
    
    if iteracoes >= iteracoes_MAX:
        print("O método de Newton modificado não convergiu dentro do número máximo de iterações.")
    
    return x
x0 = 1.0
iteracoes_MAX = 100
tolerancia = 1e-6
root = met_NEWTON_MODIFICADO(f, f_function, x0, iteracoes_MAX, tolerancia)
print("Raiz da função: x =", root)