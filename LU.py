MAX = 100
 
def Metodo_LU(MATRIZ, b, N):
 
    lower = [[0 for x in range(N)] 
                for y in range(N)]
    upper = [[0 for x in range(N)] 
                for y in range(N)]
    
    print("Metodo - LU")
    print()
    
    for i in range(N):
        lower[i][i] = 1

    for i in range(N):

        for k in range(i, N):

            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])
 
            upper[i][k] = MATRIZ[i][k] - sum

        if(i!=0):
            print("Passo", i, "- Matriz M: ", i - 1)
            for c in range(N):
                for s in range(N):
                    print("{:.3f}".format(lower[c][s]), end = "\t")
                print()
            print()
        for k in range(i, N):
            if (i == k):
                lower[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])
                lower[k][i] = float((MATRIZ[k][i] - sum) /
                                       upper[i][i])
        print()
    print("Tringular Inferior - L \t\t\t Triangular Superior - U")
    for i in range(N):
        for j in range(N):
            print("{:.3f}".format(lower[i][j]), end = "\t")
        print("", end = "\t\t")

        for j in range(N):
            print("{:.3f}".format(upper[i][j]), end = "\t")
        print("", end = "")
        print()

    y = [0 for i in range(N)]
    y[0] = b[0]/lower[0][0]
    y[0] = round(y[0], 5)
    print("\nValores matriz Ly = b")
    print("y1 = %.3f"%y[0])
    for j in range(1, N):
        valor = 0
        for k in range(0,j):
            valor-=lower[j][k]*y[k]
        valor+=b[j]
        valor = round(valor, 5)
        y[j] = valor/lower[j][j]
        
        print("y%d = %.3f"%(j+1, y[j]))
    
    x = [0 for i in range(N)]
    x[N-1] = y[N-1]/upper[N-1][N-1]

    for i in range(N-2, -1, -1):
        valor = 0
        for j in range(N-1, i, -1):
            valor-=x[j]*upper[i][j]
        valor+=y[i]
        valor = round(valor, 5)
        x[i] = valor/upper[i][i]
    
    print("\nValores matriz Ux = y")
    for i in range(N):
        print("x%d = %.3f"%(i+1, x[i]))
MATRIZ = [[2, 3, 1],
       [1, 1, 2],
       [4, 2, 1]]
b = [4, 5, 6]
Metodo_LU(MATRIZ, b, 3)