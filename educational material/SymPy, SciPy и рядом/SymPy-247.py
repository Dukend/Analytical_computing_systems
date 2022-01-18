import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui

QtGui.QGuiApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)


def f(y, t, params):
    y1, y2 = y
    a, b, c, d = params
    return [y1 * (a - b * y2), y2 * (-c + d * y1)]


t = np.linspace(0, 7, 71)
y0 = [2, 1]
fig = plt.figure(facecolor='white')

for b in range(4, 1, -1):
    params = [3, b, 1, 1]
    st = 'a=%d b=%d c=%d d=%d' % tuple(params)
    [y1, y2] = odeint(f, y0, t, args=(params,), full_output=False).T
    plt.plot(y1, y2, linewidth=2, label=st)

plt.legend(fontsize=12)
plt.grid(True)
plt.xlim(0, 3)
plt.show()


def f(y, t, params):
    y1, y2 = y
    a, b, c, d = params
    return [y1 * (a - b * y2), y2 * (-c + d * y1)]


t = np.linspace(0, 7, 71)
ic = np.linspace(1.0, 3.0, 11)  # начальные значения для 1-й функции
fig = plt.figure(facecolor='white')
for r in ic:
    y0 = [r, 1.0]
    y = odeint(f, y0, t, args=([3, 3, 1, 1],))
    plt.plot(y[:, 0], y[:, 1], linewidth=2)

plt.grid(True)  # следующий рисунок слева

x1 = np.linspace(0, 3, 31)
y1 = np.linspace(0, 2, 21)
X1, Y1 = np.meshgrid(x1, y1)  # создание сетки
DX1, DY1 = f([X1, Y1], t, [3, 3, 1, 1])
LN = np.sqrt(DX1 ** 2 + DY1 ** 2)
LN[LN == 0] = 1.  # исключение деления на 0
DX1 /= LN  # нормировка
DY1 /= LN
plt.quiver(X1, Y1, DX1, DY1, LN, pivot='mid', cmap=plt.cm.jet)

plt.show()
