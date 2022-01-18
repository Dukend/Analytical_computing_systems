# Длина цепной линии y  ch x на отрезке 0  x 1.
from scipy.integrate import quad
import numpy as np
import sympy as smp
import matplotlib.pyplot as plt

x = smp.symbols('x')
fn = smp.cosh(x)  # символьное выражение уравнения
f = smp.sqrt(1 + fn.diff(x) ** 2)  # подынтегральное символьное выражение
g = smp.lambdify(x, f, "numpy")  # преобразование в выражение numpy
L = quad(g, 0, 1)  # вычисление интеграла
print(L)  # значение интеграла и точность
# (1.1752011936438014, 1.3047354237503154e-14)
# Сравним с точным значением sinh1.
print(np.sinh(1))
# 1.17520119364
# график цепной линии
fig = plt.figure(facecolor='white')  # ,xlim=(-2,2), ylim=(0,4))
ax = plt.axes(xlim=(-2, 2), ylim=(0, 4))
fun = smp.lambdify(x, fn, "numpy")
x = np.linspace(-2, 2, 81)
ax.plot(x, fun(x), lw=3)
ax.grid(True)
plt.show()
