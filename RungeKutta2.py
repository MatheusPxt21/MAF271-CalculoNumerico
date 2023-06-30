import numpy as np

def f(x, y):
    return y * np.cos(x)

x0 = 0
y0 = 1

a = 0
b = 1
N = 10

h = (b - a) / N

xi = [x0]
yi = [y0]

for i in range(N):
    k1 = f(x0, y0)
    k2 = f(x0 + h, y0 + h * k1)
    yk = y0 + (k1 + k2) * h / 2
    x0 = x0 + h
    xi.append(round(x0))
    yi.append(round(yk))
    y0 = yk
    print(f"({round(x0, 2)}, {round(y0, 2)})")

print(xi)
print(yi)