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
w.setCameraPosition(distance=40)

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

## Example 2:
## Array of vertex positions, three per face
verts = np.empty((36, 3, 3), dtype=np.float32)

theta = np.linspace(0, 2*np.pi, 37)[:-1]
verts[:,0] = np.vstack([2*np.cos(theta), 2*np.sin(theta), [0]*36]).T
verts[:,1] = np.vstack([4*np.cos(theta+0.2), 4*np.sin(theta+0.2), [-1]*36]).T
verts[:,2] = np.vstack([4*np.cos(theta-0.2), 4*np.sin(theta-0.2), [1]*36]).T


## Colors are specified per-vertex
colors = np.random.random(size=(verts.shape[0], 3, 4))
m2 = gl.GLMeshItem(vertexes=verts, vertexColors=colors, smooth=False, shader='balloon',
                   drawEdges=True, edgeColor=(1, 1, 0, 1))
m2.translate(-5, 5, 0)

w.addItem(m2)

# one peace of turbin:

verts = np.empty((1, 3, 3), dtype=np.float32)
verts[0:1] = [[0, 0, 0],
              [0, 1, 0],
              [0, 0, 1]]
m3 = gl.GLMeshItem(vertexes=verts[0:1], vertexColors=colors, smooth=False, shader='balloon',
                   drawEdges=True, edgeColor=(1, 1, 0, 1))
print(verts[0:1])
w.addItem(m3)


sys.exit(app.exec_())  # Запускаем цикл обработки событий
