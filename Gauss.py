import numpy as np

def MetodoGAUSS(A, b):
    N = len(b)
    for i in range(N-1):
        max_index = np.argmax(np.abs(A[i:, i])) + i
        A[[i, max_index]] = A[[max_index, i]]
        b[[i, max_index]] = b[[max_index, i]]
        for j in range(i+1, N):
            fator = A[j, i] / A[i, i]
            A[j, i:] -= fator * A[i, i:]
            b[j] -= fator * b[i]
    x = np.zeros(N)
    for i in range(N-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x

A = np.array([[1.0, -3.0, 2.0],
              [-2.0, 8.0, -1.0],
              [4.0, -6.0, 5.0]])
b = np.array([11.0, -15.0, 29.0])
x = MetodoGAUSS(A, b)
print("Resultado:")
for i in range(len(x)):
    print(f"x{i+1} = {x[i]}")
