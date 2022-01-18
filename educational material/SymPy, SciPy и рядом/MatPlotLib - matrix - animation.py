import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy
fig = plt.figure(facecolor='white')
ax = plt.axes(xlim=(-25, 25), ylim=(-25, 25),aspect='equal')
x = np.arange(-25, 26)
y = np.arange(-25, 26)
X,Y=np.meshgrid(x,y)
ZZ=np.sqrt(X**2+Y**2)
imlist = [ ]
for i in np.arange(36):
    Z=copy.deepcopy(ZZ)-i
    Z[np.logical_and(Z<0,Z>-2)]=(i-17)*2
    Z[np.logical_and(Z<6,Z>4)]=(17-i)*2
    imlist.append((plt.pcolor(x, y, Z , norm=plt.Normalize(-35, 35)),))
anim = animation.ArtistAnimation(fig, imlist, interval=50,
repeat_delay=100, blit=True)
plt.show()