from sympy import *
from sympy.plotting import plot3d_parametric_surface

u, v = symbols('u v')
plot3d_parametric_surface(cos(u) * v, sin(u) * v, u, (u, 0, 10), (v, -2, 2))
