from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
import sys


app = QtGui.QApplication([])

win = pg.PlotWidget()
print("win = ", win)
win.resize(1000, 600)
win.show()

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

# ======================================
a = 10
b = 5
vb = win.getViewBox()
ball = QtGui.QGraphicsEllipseItem(QtCore.QRectF(0, 0, 2*a, 2*b))
ball.setPen(pg.mkPen(100, 200, 100))
ball.setBrush(pg.mkBrush("w"))
vb.addItem(ball)


sys.exit(app.exec_())
