from sympy import Symbol, besselj, limit
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import math

import sys, traceback


app = QtGui.QApplication([])

win2 = pg.GraphicsWindow(title="delta")
pg.setConfigOptions(antialias=True)

canvas_2D = win2.addPlot(title = "sin(alpha)")
canvas_2D.addLegend()
canvas_2D.getAxis('left').setLabel(text='sin_alpha')
canvas_2D.getAxis('bottom').setLabel(text='t_N')

# вывод на 2D полотно
sin_alpha_apprx_plt =canvas_2D.plot(np.array(sin_alpha_apprx_arr),
                          pen=(200, 0, 0),
                          symbolBrush=(200, 200, 200),
                          symbolPen=(200, 200, 200),
                          symbol='o',
                          symbolSize=1,
                          name="--- Изменение величины sin_alpha от номера импульса (с округлением до 1e-10)")
sin_alpha_exact_plt =canvas_2D.plot(np.array(sin_alpha_exact_arr),
                          pen=(0, 200, 0),
                          symbolBrush=(200, 0, 200),
                          symbolPen=(200, 0, 200),
                          symbol='s',
                          symbolSize=1,
                          name="--- Изменение величины sin_alpha от номера импульса (без округления)")

nu = Symbol('nu')
f = (2*besselj(1, nu)/nu)**2
detta0 = limit(f, nu, 0).evalf()
print("detta(0) = ", detta0)

detta_Xi_arr = []
for t_N, sina in sin_alpha_exact_arr:
    nu_val = (math.pi * Consts.satellite.laser_reflector_D * sina)/Consts.station.laser_lambda
    detta_x = float(limit(f, nu, nu_val).evalf())
    detta_Xi_arr.append([t_N, detta_x])

detta_Xi_arr = np.array(detta_Xi_arr)
win3 = pg.GraphicsWindow(title="detta")
canvas_2D_2 = win3.addPlot(title = "detta(nu)/detta(0)")
canvas_2D_2.addLegend()
canvas_2D_2.getAxis('left').setLabel(text='detta(nu)/detta(0)')
canvas_2D_2.getAxis('bottom').setLabel(text='t_N (сек.)')

# # вывод на 2D полотно
detta_plt =canvas_2D_2.plot(detta_Xi_arr,
                          pen=(200, 0, 0),
                          symbolBrush=(200, 200, 200),
                          symbolPen=(200, 200, 200),
                          symbol='o',
                          symbolSize=1,
                          name="--- Зависимость величины принимаемого потока отраженного лазерного импульса от nu")

