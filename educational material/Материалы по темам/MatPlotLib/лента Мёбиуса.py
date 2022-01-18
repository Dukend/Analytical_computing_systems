import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

"""
    стр. 170
"""

# координатные функции
xs = lambda u, v: (R + v * np.cos(n * u / 2)) * np.cos(u)
ys = lambda u, v: (R + v * np.cos(n * u / 2)) * np.sin(u)
zs = lambda u, v: v * np.sin(n * u / 2)


def initpict():
    global u
    u = np.linspace(0, du, 1)  # очистка вектора u перед стартовым кадром


def redraw(i):  # рисование i-го кадра
    global u
    u = np.append(u, (i + 1) * du)  # добавление точки к вектору u
    U, V = np.meshgrid(u, v)
    X = xs(U, V)
    Y = ys(U, V)
    Z = zs(U, V)
    ax.clear()
    # после очистки восстанавливаем видимые размеры графической области
    ax.set_xlim3d(xyLeft, xyRight)
    ax.set_ylim3d(xyLeft, xyRight)
    ax.set_zlim3d(-H, H)
    ax.plot(xc, yc, zc, color='brown', linewidth=3)  # направляющая окружность
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color='0.5', alpha=0.4)


R = 4
H = 2
n = 1
NumFrames = 40  # количество кадров
du = 2 * np.pi / NumFrames
xyRight = R + 1
xyLeft = -xyRight
fig = plt.figure(facecolor='white')
fig.set_dpi(100)
ax = Axes3D(fig, xlim=(xyLeft, xyRight), ylim=(xyLeft, xyRight), zlim=(-H, H))
# координаты точек направляющей окружности одинаковые для всех кадров
t = np.linspace(0, 2 * np.pi, 100)
vt = np.zeros(np.size(t))
xc = xs(t, vt)
yc = ys(t, vt)
zc = zs(t, vt)
# массив параметра v поверхности одинаков для всех моментов времени
v = np.linspace(-H / 2, H / 2, 11)
anim = animation.FuncAnimation(fig, redraw, init_func=initpict, frames=NumFrames, interval=20, repeat=True, blit=False)
plt.show()
