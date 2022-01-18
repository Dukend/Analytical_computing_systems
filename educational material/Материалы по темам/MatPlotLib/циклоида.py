import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle


def initpict():
    line1.set_data([], [])
    line2.set_data([], [])
    pc.center=(xC,yC)
    ax.add_patch(pc)
    pp.center=(xP,yP)
    ax.add_patch(pp)
    return pc,pp,line1,line2

def redraw(i):
    global xC, xP, yP
    n=i/10
    t=np.linspace(0,n,100)
    x=t-np.sin(t)
    y=1-np.cos(t)
    line1.set_data(x, y)
    xC=n
    pc.center=(xC,yC)
    xP=n-np.sin(n)
    yP=1-np.cos(n)
    pp.center=(xP,yP)
    line2.set_data([n,xP], [1,yP])
    return pc,pp,line1,line2


fig = plt.figure(facecolor='white')
fig.set_dpi(100)
a=1; b=3; dl=1; dh=0.25
ax = plt.axes(xlim=(0, 12), ylim=(0, 3))
ax.set_yticklabels(['0',' ','1',' ','2',' ','3']) # меняем текст меток верт. оси
line1, = ax.plot([], [] ,lw=2)
line2, = ax.plot([], [] ,'r')
xC=0;yC=1; xP=0; yP=0
pc = plt.Circle((xC, yC), 1, fc='c')
pp = plt.Circle((xP, yP), 0.1, fc='k')
ax.set_aspect('equal')
anim = animation.FuncAnimation(fig, redraw, init_func=initpict, frames=120, interval=50, blit=True)
plt.show()