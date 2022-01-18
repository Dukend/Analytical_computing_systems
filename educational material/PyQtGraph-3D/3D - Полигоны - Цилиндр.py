from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import sys


"""
Simple examples demonstrating the use of GLMeshItem.

"""

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseDesktopOpenGL)
app = QtGui.QApplication([])

w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLMeshItem')
w.setCameraPosition(distance=40)

g = gl.GLGridItem()
g.scale(2, 2, 1)
w.addItem(g)


# cylinder
md = gl.MeshData.cylinder(rows=10, cols=20, radius=[1., 2.0], length=5.)
md2 = gl.MeshData.cylinder(rows=10, cols=20, radius=[2., 0.5], length=10.)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2, 0] = 0
colors[:, 1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m5 = gl.GLMeshItem(meshdata=md, smooth=True, drawEdges=True, edgeColor=(1, 0, 0, 1), shader='balloon')
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2, 0] = 0
colors[:, 1] = np.linspace(0, 1, colors.shape[0])
md2.setFaceColors(colors)
m6 = gl.GLMeshItem(meshdata=md2, smooth=True, drawEdges=False, shader='balloon')
m6.translate(0, 0, 7.5)

m6.rotate(0., 0, 1, 1)
#m5.translate(-3, 3, 0)
w.addItem(m5)
w.addItem(m6)


sys.exit(app.exec_())  # Запускаем цикл обработки событий
