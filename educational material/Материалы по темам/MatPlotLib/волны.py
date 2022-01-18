import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def xs(u, t):
    return u + a * np.sin(w * t - k * u) * (1 + np.exp(-2 * k * h))


def ys(u, t):
    return a * np.cos(w * t - k * u) * (1 - np.exp(-2 * k * h))


def redraw(i):
    t = i / 10  # момент времени текущего кадра
    u = np.linspace(-2 * L, 2 * L, 100)
    X = xs(u, t)
    Y = ys(u, t) + h
    # начальная и конечная точки области заливки должны находиться на оси x!
    X = np.insert(X, 0, X[0])
    Y = np.insert(Y, 0, 0)
    X = np.append(X, X[-1])
    Y = np.append(Y, 0)
    # для изменение данных передается массив из двух столбцов,
    # например, ptch.set_xy([[0,0],[3,-5],[6,-9],[9,0]])
    # преобразуем одномерные массивы координат в двумерный массив pp
    XY = np.vstack((X, Y))
    pp = XY.T
    ptch.set_xy(pp)  # меняем данные Polygon–а


L = 6
w = 1
a = 1
h = 6
k = 0.4  # параметры задачи
fig = plt.figure(facecolor='white')
fig.set_dpi(100)
ax = plt.axes(xlim=(-2 * (L - 1), 2 * (L - 1)), ylim=(0, h + 2))
ax.set_yticklabels(['0', '', '2', '', '4', '', '6', '', '8'])  # подписи меток верт. оси
ptch, = ax.fill([0, 5, 10], [0, 0, 0], 'c')  # создаем пустой объект;
# fill возвращает список/кортеж объектов класса Polygon
ax.add_patch(ptch)
ax.set_aspect('equal')
anim = animation.FuncAnimation(fig, redraw, frames=120, interval=50)
plt.show()
