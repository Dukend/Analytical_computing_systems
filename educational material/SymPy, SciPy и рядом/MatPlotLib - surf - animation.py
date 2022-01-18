import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import copy
fig = plt.figure(facecolor='white')
ax=Axes3D(fig, xlim=(-1, 1), ylim=(-1, 1), zlim=(-1,1.0))
# поверхность 1
x = np.linspace(-1,1,31)
y = np.linspace(-1,1,31)
X,Y=np.meshgrid(x,y)
Z=1-X**2-Y**2
ZZ=copy.deepcopy(Z) # запоминаем Z для 7-й поверхности
p1=ax.plot_surface(X,Y,Z,rstride=1,cstride=1,color='r', alpha=0.8)
# поверхность 2
Z=1-X**2-Y**2;
Z[Z>0]=0
p2=ax.plot_surface(X,Y,Z,rstride=1,cstride=1,color='b', alpha=0.8)
# поверхность 3
a=2.4; Z=np.sin(4*np.pi*(X**2+Y**2)/a**2)
p3=ax.plot_surface(X,Y,Z,rstride=1,cstride=1,color='g', alpha=0.8)
# поверхность 4
Z=1-X**2-Y**2;
Z[Z<0]=0
Z=0.5-1.5*np.sqrt(Z)
p4=ax.plot_surface(X,Y,Z,rstride=1,cstride=1,color='c', alpha=0.8)
# поверхность 5
Z=1.3-np.abs(X-Y)-np.abs(X+Y)
Z[Z<0]=0
Z=0.5-1.5*np.sqrt(Z)
p5=ax.plot_wireframe(X,Y,Z,rstride=1,cstride=1,color='m',
alpha=0.8, lw=2)
# объект 6 (кривая)
theta = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
z = np.linspace(-1, 1, 1000)
r=np.abs(z)
x = r * np.sin(6*theta)
y = r * np.cos(6*theta)
p6,=ax.plot(x, y, z,c='c',lw=3)
# объект 7 (кривая в форме поверхности)
# X,Y,Z первой поверхности
ZZ[ZZ<0]=0
p7,=ax.plot3D(np.ravel(X),np.ravel(Y),np.ravel(ZZ),lw=2,c='brown')
# список объектов для анимирования
piclist=[(p1,),(p2,),(p3,),(p4,),(p5,),(p6,),(p7,)]
anim = animation.ArtistAnimation(fig, piclist, interval=1000,
blit=True, repeat_delay=100)
plt.show()