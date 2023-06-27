def TaylorSegundaOrdem(f, df, x0, y0, h, num_steps):
    x_values = [x0]
    y_values = [y0]
    
    for _ in range(num_steps):
        x = x_values[-1]
        y = y_values[-1]
        df_dx = df(x, y)
        df_dy = -1
        delta_x = h
        delta_y = h * f(x, y) + (h ** 2) * (df_dx + (df_dy * f(x, y))) / 2
        x_next = x + delta_x
        y_next = y + delta_y
        x_values.append(x_next)
        y_values.append(y_next)
    
    return x_values, y_values
# Função f(x, y) = x - y
def f(x, y):
    return x - y
# Derivada de y em relação a x (df(x, y) / dx)
def df(x, y):
    return x - y
# Valores iniciais
x0 = 0
y0 = 2
h = 0.2
n = 5
x_values, y_values = TaylorSegundaOrdem(f, df, x0, y0, h, n)
print("\n\n Taylor 2 Ordem:")
for x, y in zip(x_values, y_values):
    print(f"x = {x:.2f}, y = {y:.4f}")
