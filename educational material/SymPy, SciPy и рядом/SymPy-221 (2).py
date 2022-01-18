import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x, y = symbols('x y')
a = 2;
b = 1
F = x ** 2 / a ** 2 + y ** 2 / b ** 2 - 1
Fx = F.diff(x)
Fy = F.diff(y)
x0 = 1.5  # x координата точки касания
y0 = solve(F.subs(x, x0), y)[-1]  # находим y координаты точек касания
# и выбираем последнюю из списка
Fx0 = Fx.subs([(x, x0), (y, y0)])  # значение производной Fx в точке касания
Fy0 = Fy.subs([(x, x0), (y, y0)])  # значение производной Fy в точке касания
# создание numpy функций из символьных выражений
Fun = lambdify((x, y), F, "numpy")
Tan = lambdify((x, y), Fx0 * (x - x0) + Fy0 * (y - y0), "numpy")
Norm = lambdify((x, y), Fx0 * (y - y0) - Fy0 * (x - x0), "numpy")
# построение графиков эллипса, касательной и нормали
t = np.linspace(-a, a, 31)
Xf, Yf = np.meshgrid(t, t)
plt.figure()
plt.contour(Xf, Yf, Fun(Xf, Yf), [0], linewidths=3, colors='b')
tx = np.linspace(x0 - 1.0, x0 + 1.0, 21)
y0 = float(y0)  # преобразование символьного значения в числовое
ty = np.linspace(y0 - 1, y0 + 1, 21)
Xt, Yt = np.meshgrid(tx, ty)
plt.contour(Xt, Yt, Tan(Xt, Yt), [0], linewidths=2, colors='r')
plt.contour(Xt, Yt, Norm(Xt, Yt), [0], linewidths=2, colors='g')
# plt.gcf().gca().axis([-3,3,-3,3]);
plt.gcf().gca().axis('equal');
plt.gcf().set_facecolor('white')
plt.show()
