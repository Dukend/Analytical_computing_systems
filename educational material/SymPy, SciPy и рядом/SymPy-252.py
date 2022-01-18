import numpy as np
from scipy.integrate import odeint, ode
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def f(y, t):
    y1, y2, y3, y4 = y
    return [y2
        , -y1 / (y1 ** 2 + y3 ** 2) ** (3 / 2)
        , y4
        , -y3 / (y1 ** 2 + y3 ** 2) ** (3 / 2)]


t = np.linspace(0, 20, 1001)
y0 = [1, 0, 0, 0.4]
[y1, y2, y3, y4] = odeint(f, y0, t, full_output=False).T
fig, ax = plt.subplots()
fig.set_facecolor('white')
ax.plot(y1, y3, linewidth=1)
circle = Circle((0, 0), 0.03, facecolor='orange')  # круг
ax.add_patch(circle)
plt.axis('equal')
plt.grid(True)

# Теперь добавим код создания анимации движения планеты.
import matplotlib.animation as animation

fig2 = plt.figure(facecolor='white')
ax = plt.axes(xlim=(-0.2, 1.2), ylim=(-0.4, 0.4))
line, = ax.plot([], [], lw=3)
circle = Circle((0, 0), 0.05, facecolor='orange')
ax.add_patch(circle)
pc = plt.Circle((y0[0], y0[2]), 0.02, fc='b')
ax.add_patch(pc)
ax.grid(True)


def redraw(i):
    x = y1[0:i + 1]
    y = y3[0:i + 1]
    line.set_data(x, y)
    pc.center = (x[-1], y[-1])


anim = animation.FuncAnimation(fig2, redraw, frames=126, interval=50)
plt.show()
