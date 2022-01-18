from sympy import symbols, solve, latex, pprint, sqrt, exp, diff, integrate, cos, sin

x, y, HELLO, WORLD = symbols('x, y, HELLO, WORLD')
pprint ( latex ( solve ( x**2 + HELLO * x + WORLD, x ) ) )
pprint(integrate(exp(x*y**2)+sqrt(x)*y**2,y))

from sympy.plotting import plot3d_parametric_surface
u, v = symbols('u v')
plot3d_parametric_surface(cos(u)*v,sin(u)*v,u,(u,0,10),(v, -2,2))

