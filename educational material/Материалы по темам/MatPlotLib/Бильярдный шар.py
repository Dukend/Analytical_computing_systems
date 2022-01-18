import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Rectangle


def initpict():
    pc.center = (x0, y0)
    ax.add_patch(pc)
    return pc,  # return [ ] оставляет стартовый шар нарисованным


def redraw(i):
    global x, y, dx, dy
    if x + r > rbod:
        x = rbod - r
        dx = -dx
    elif x - r < lbod:
        x = r
        dx = -dx
    else:
        x = x + dx
    if y + r > ubod or y + dy + r > ubod:
        y = ubod - r
        dy = -dy
    elif y - r < dbod or y - r + dy < dbod:
        y = r
        dy = -dy
    else:
        y = y + dy
    pc.center = (x, y)
    return pc,


fig = plt.figure(facecolor='white')
fig.set_dpi(100)
rbod = 4
lbod = 0
ubod = 4
dbod = 0  # границы области
ax = plt.axes(xlim=(lbod, rbod), ylim=(dbod, ubod))
ax.set_aspect('equal')
# начальное положение и радиус шара
x0 = 3
y0 = 1
r = 0.35
dx = 0.03
dy = 0.0125  # вектор начальной скорости (направления)
x = x0
y = y0
pc = plt.Circle((x, y), r, fc='b')
anim = animation.FuncAnimation(fig, redraw,
                               init_func=initpict, frames=400, interval=20, blit=True)
plt.show()
