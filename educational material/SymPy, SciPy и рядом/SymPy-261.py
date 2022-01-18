import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import  ode
from math import sqrt

ts = [ ]
ys = [ ]


def fout(t, y): # обработчик шага
    ts.append(t)
    ys.append(list(y.copy()))


def f(t, y): # функция правой части системы ОДУ
    k=0.01
    g=9.81
    y1, y2, y3, y4 = y
    return [y2,
    -k*y2*sqrt(y2**2+y4**2),
    y4,
    -k*y4*sqrt(y2**2+y4**2)-g]
# Решаем ОДУ и строим его график.
tmax=1.41 # время движения, подбирается экспериментально
alph=np.pi/4 # угол бросания тела
v0=10.0 # начальная скорость
ODE=ode(f)
y0,t0=[0, v0*np.cos(alph), 0, v0*np.sin(alph)], 0 # начальные условия
r=ODE.set_integrator('dopri5', max_step=0.1) # метод Рунге – Кутта
r.set_solout(fout) # загрузка обработчика шага
r=ODE.set_initial_value(y0, t0) # задание начальных значений
ret = r.integrate(tmax) # решаем ОДУ
Y=np.array(ys)
fig, ax = plt.subplots()
fig.set_facecolor('white')
ax.plot(Y[:,0],Y[:,2],linewidth=3) # график решения
ax.grid(True)
plt.show()