from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import sys


QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseDesktopOpenGL)
app = QtWidgets.QApplication(sys.argv)

w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLMeshItem')
w.setCameraPosition(distance=7)

g = gl.GLGridItem()
g.scale(2,2,1)
w.addItem(g)

#AXIS
size = QtGui.QVector3D(2, 2, 2)
axis = gl.GLAxisItem(size, antialias=False)
# z - green
# y - yellow
# x - blue
w.addItem(axis)

## Example 3:
## sphere

md = gl.MeshData.sphere(rows=10, cols=20)
#colors = np.random.random(size=(md.faceCount(), 4))
#colors[:,3] = 0.3
#colors[100:] = 0.0
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m3 = gl.GLMeshItem(meshdata=md, smooth=False, shader='balloon')

# m3.translate(5, -5, 0)
w.addItem(m3)


sys.exit(app.exec_())  # Запускаем цикл обработки событий
