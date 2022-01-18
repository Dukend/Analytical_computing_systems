from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import math
import sys


QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseDesktopOpenGL)
app = QtWidgets.QApplication(sys.argv)

w = gl.GLViewWidget()
# w.opts['distance'] = 40
w.setCameraPosition(distance=20)
w.showMaximized()
w.setWindowTitle('pyqtgraph 3D example: GLLinePlotItem')

gx = gl.GLGridItem()
gx.rotate(90, 0, 1, 0)
gx.translate(-10, 0, 0)
w.addItem(gx)
gy = gl.GLGridItem()
gy.rotate(90, 1, 0, 0)
gy.translate(0, -10, 0)
w.addItem(gy)
gz = gl.GLGridItem()
gz.translate(0, 0, -10)
w.addItem(gz)

size = QtGui.QVector3D(2, 2, 2)
axis = gl.GLAxisItem(size, antialias=False)
w.addItem(axis)

a = 10
b = 5
crds = []
angles_range = np.linspace(0, 2*math.pi, 360, endpoint=True)
for angle in angles_range:
    x = a*math.cos(angle)
    y = b*math.sin(angle)
    crds.append([x, y, 0])

plt = gl.GLLinePlotItem(  pos=np.array(crds)
                        , color=(1, 1, 0, 1)
                        , width=15)
w.addItem(plt)
# по каким-то причинам в текущей версии библиотеки толщина линий устанавливается сразу
# для всех 3D-объектов


sys.exit(app.exec_())  # Запускаем цикл обработки событий
