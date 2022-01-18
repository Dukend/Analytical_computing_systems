from sympy import symbols, plotting, latex, S, plot

x = symbols('x')
f1 = x**2
f2 = -x**2
str = latex(S('x**2 , -x**2 ', evaluate=False))
p = plot(   (f1, (x, -1, 0))
         ,  (f2, (x, 0, 1))
         ,  title = '$'+str+'$'
         , show=False)
p[0].line_color = 'blue'
p[1].line_color = 'red'
p.show()
