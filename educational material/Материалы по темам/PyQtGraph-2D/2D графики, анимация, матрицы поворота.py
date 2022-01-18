from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import math
import sys


def rot_mat(axis, angle_grad):
    angle = (angle_grad *math.pi)/180
    if axis == 'x':
        return np.array([
                [1, 0, 0],
            [0, math.cos(angle), math.sin(angle)],
            [0, -math.sin(angle), math.cos(angle)]])
    if axis == 'y':
        return np.array([[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-math.sin(angle), 0, math.cos(angle)]])
    if axis == 'z':
        return np.array([[math.cos(angle), math.sin(angle), 0], [-math.sin(angle), math.cos(angle), 0], [0, 0, 1]])

    print("rot_mat: Нет такой матрицы!!!")
    exit(-9)


app = QtGui.QApplication([])

win = pg.GraphicsWindow(title="Scatter Plot Symbols")
win.resize(1000, 1000)

pg.setConfigOptions(antialias=True)

plot = win.addPlot(title="Plotting with symbols")
plot.addLegend()

xValues = []
yValues = []
crd = []
for i in range(-10, 11, 1):
    x = i
    y = x**2
    z = 0
    xValues.append(x)
    yValues.append(y)
    crd.append([x, y, z])

crd = np.array(crd)
crd_src = crd[:]
crd = np.dot(crd, rot_mat('z', 0))
r = 10
shift = [0, r, 0]
xValues = crd[:, 0]
yValues = crd[:, 1]

plt = plot.plot(    x = xValues,
                      y = yValues,
                      pen=(205, 92, 92),
                      symbolBrush=(205, 92, 92),
                      symbolPen='w', symbol='o', symbolSize=14, name="symbol='o'")
xValues = []
yValues = []
for i in range(0, 360, 1):
    angle = (i * math.pi)/180
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    xValues.append(x)
    yValues.append(y)

plot.plot(   x = xValues
           , y = yValues
           , pen=(205, 92, 92)
           , name="symbol='circle r'")

# plt = pg.graphicsItems.PlotDataItem.PlotDataItem
plot.enableAutoRange('xy', False)
plot.setXRange(-100, 100)
plot.setYRange(-100, 100)


time_global_i =0
time_global_i_max = 360


def update():
    global plt, crd_src, \
        time_global_i, time_global_i_max,\
        shift

    time_global_i = (time_global_i + 1) % time_global_i_max
    angle = -time_global_i
    rot_mat_z = rot_mat('z', angle)
    crd = np.add(crd_src, shift)
    crd = np.dot(crd, rot_mat_z)
    plt.setData(crd[:, 0], crd[:, 1])


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)


sys.exit(app.exec_())  # Запускаем цикл обработки событий
