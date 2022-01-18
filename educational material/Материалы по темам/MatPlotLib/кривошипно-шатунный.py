import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Rectangle


def redraw(i, lin):
    alph = np.pi * i / 50  # угол поворота кривошипа в i-ом кадре
    # приращения координат узлов ломаной165
    dx = np.array([0, a * np.cos(alph), np.sqrt(b ** 2 - a ** 2 * np.sin(alph) ** 2),
                   0, dl, 0, -dl, 0])
    dy = np.array([0, a * np.sin(alph), -a * np.sin(alph), -dh, 0, 2 * dh, 0, -dh])
    # массивы координат узлов ломаной
    x = np.cumsum(dx)
    y = np.cumsum(dy)
    lin.set_data(x, y)


fig = plt.figure(facecolor='white')
fig.set_dpi(100)
a = 1
b = 3
dl = 1
dh = 0.25  # геометрические размеры
ax = plt.axes(xlim=(-1.2, 5.2), ylim=(-1.5, 1.5))
line, = ax.plot([], [], lw=3)
ax.set_aspect('equal')
ax.set_xticks([])  # удаляем засечки и метки с оси X
ax.set_yticks([])  # удаляем засечки и метки с оси Y
anim = animation.FuncAnimation(fig, redraw, fargs=(line,),
                               frames=100, interval=50)
plt.show()
