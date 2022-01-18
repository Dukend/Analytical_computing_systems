# стр. 217 "Введение в научный Python"

"""
Построить график символьного выражения одной символьной
переменной, а также графики его первой и второй производных.
Первое решение состоит в использовании графической функции plot() пакета
SymPy
"""
def var1():
    import sympy as sp
    x = sp.symbols('x')
    f0 = x**4 - 15*x**2 - 10*x + 24
    f1 = sp.diff(f0, x)
    print(f1)  # 4*x**3 - 30*x - 10
    f2 = sp.diff(f0, x, 2)
    print(f2)  # 6*(2*x**2 - 5)
    sp.plot(f0, f1, f2, (x, -5, 5))

"""Поскольку управление графикой в графических функциях SymPy ограничено,
то, возможно, вы пожелаете использовать графику других пакетов, а для этого
потребуется преобразование символьного выражения.
Второе решение состоит в преобразовании символьного выражения и его
производных в лямбда – функцию и построении ее графика функцией plot()
модуля mpmath.
"""
def var2():
    import sympy as sp
    import mpmath as mp

    x = sp.symbols('x')
    f0 = x**4 - 15*x**2 - 10*x + 24
    f1 = sp.diff(f0, x)
    print(f1)
    f2 = sp.diff(f0, x, 2)
    print(f2)
    g0 = sp.lambdify(x, f0, 'mpmath')
    g1 = sp.lambdify(x, f1, 'mpmath')
    g2 = sp.lambdify(x, f2, 'mpmath')
    mp.plot([g0, g1, g2], [-5, 5])

"""
Третье решение состоит в преобразовании символьного выражения и его
производных в лямбда – функцию и построении ее графика функцией plot()
модуля matplotlib.pyplot.
"""
def var3():
    import matplotlib.pyplot as plt
    import sympy as sp
    import numpy as np
    x = sp.symbols('x')
    f0 = sp.sin(x)*sp.exp(-x**2)
    f1 = sp.diff(f0, x)
    f2 = sp.diff(f0, x, 2)
    h0 = sp.lambdify(x, f0, 'numpy')
    h1 = sp.lambdify(x, f1, 'numpy')
    h2 = sp.lambdify(x, f2, 'numpy')
    t = np.linspace(-3, 3, 121)
    plt.plot(t, h0(t), 'b', t, h1(t), 'r', t, h2(t), 'g', linewidth=3)
    plt.show()
    """
        Здесь, имея символьные выражения f0, f1 и f2, мы построили лямбда –
    функции h0(x), h1(x), h2(x). Обратите внимание на третий аргумент
    функций lambdify(), которому присвоено значение 'numpy'. Это нужно для
    того, чтобы имена функций sin и exp, используемые в символьных
    выражениях f0, f1 и f2, были преобразованы в соответствующие функции
    модуля numpy. Затем лямбда – функции h0(x), h1(x), h2(x) мы используем
    для создания массивов значений, которые нужны для построения графиков
    функцией matplotlib.pyplot.plot()
    """

var1()
var2()
var3()
