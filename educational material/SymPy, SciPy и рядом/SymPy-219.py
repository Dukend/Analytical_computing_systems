"""
Пример. Построить график функции y  cosx и графики ее сумм Тейлора
различного порядка.
"""

import sympy as sp
from sympy import symbols
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x')
f = sp.cos(x)
fvec = np.vectorize(lambda val: f.subs(x, val).evalf())
z = np.linspace(-8, 8, num=300)
fig = plt.figure(facecolor='white')
plt.plot(z, fvec(z), linewidth=5, color='r', label='cos(x)')


ax = fig.gca()
for order in range(3, 20, 2):
    s = f.series(x, 0, order)
    svec = np.vectorize(lambda val: s.removeO().subs(x, val))
    ax.plot(z, svec(z), '-', label='n=%i' % order, linewidth=3)
ax.set_xlim(-8, 11)
ax.set_ylim(-2, 2)
ax.legend(fontsize=12)
ax.grid(True)
