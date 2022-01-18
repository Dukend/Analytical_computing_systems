"""
Пример. Нарисовать в одном графическом окне символьный график и график
matplotlib, не прибегая к преобразованиям выражений.
"""
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
p1 = sp.plot(x ** 3 - x, (x, -1.5, 1.5))  # sympy график
fig = plt.gcf()  # Get the current figure
fig.set_facecolor('white')
ax = fig.gca()  # Get the current axes - получение осей sympy графика
t = np.linspace(-1.5, 1.5, 16)
z = t ** 5 - t
ax.plot(t, -z, '-sr', linewidth=3)  # matplotlib график
ax.grid(True)
ax.axis('equal')
"""Вначале мы построили график символьного выражения x**3-x. 
Затем получили ссылку на объект axes этого графика.
Этот объект принадлежит модулю matplotlib.pyplot и имеет метод plot() этой библиотеки."""
