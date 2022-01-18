import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def f(y, t,params):
    y1, y2 = y 
    a,b,c,d=params
    return [y1*(a-b*y2),
            y2*(-c+d*y1)]

t = np.linspace(0,7,71)
y0 = [2, 1]
fig = plt.figure(facecolor='white' )
plt.hold(True)
for b in range(4,1,-1):
    params=[3,b,1,1]
    st=' a=%d b=%d c=%d d=%d' % tuple(params)
    [y1,y2]=odeint(f, y0, t,args=(params,), full_output=False).T
    plt.plot(y1,y2,linewidth=2, label=st)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.xlim(0,3)