import math 
MAX = 100; 

def Metodo_Cholesky(matrix, N): 
    contador = 0
    lower = [[0 for x in range(N + 1)]
                for y in range(N + 1)]; 

    print("Metodo de CHOLESKY")
    print()
    for i in range(N):
        for j in range(i + 1):
            contador +=1
            aux = 0; 
            if (j == i):
                for k in range(j): 
                    aux += pow(lower[j][k], 2); 
                lower[j][j] = float(math.sqrt(matrix[j][j] - aux))
                
            else: 
                for k in range(j): 
                    aux += (lower[i][k] *lower[j][k]); 
                if(lower[j][j] > 0): 
                    lower[i][j] = float((matrix[i][j] - aux) / 
                                               lower[j][j])
                
            print("Passo", contador, "- Matriz G")
            for c in range(3):
                for s in range(3):
                    print("{:.3f}".format(lower[c][s]), end = "\t")
                print()
            print()
    print("Triangular Inferior - G\t\tTransposta - Gt"); 
    for i in range(N):
        for j in range(N): 
            print("{:.3f}".format(lower[i][j]), end = "\t")
        print("", end = "\t")
        for j in range(N): 
            print("{:.3f}".format(lower[j][i]), end = "\t")
        print("")
N = 3; 
matrix = [[4, 2, -4],
       [2, 10, 4],
       [-4, 4, 9]]
Metodo_Cholesky(matrix, N); 