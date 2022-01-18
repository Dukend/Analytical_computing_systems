import numpy as np
from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
import sys

app = QtWidgets.QApplication(sys.argv)
mw = QtGui.QMainWindow()
mw.setWindowTitle('pyqtgraph example: ViewBox')
mw.show()
mw.resize(800, 600)
gv = pg.GraphicsView()
mw.setCentralWidget(gv)
l = QtGui.QGraphicsGridLayout()
l.setHorizontalSpacing(0)
l.setVerticalSpacing(0)
vb = pg.ViewBox()
p1 = pg.PlotDataItem()
vb.addItem(p1)


def updateData():
    global x, y, ellipse
    # x += 0.01
    global x, y, dx, dy
    if x + r > rbod:
        x = rbod - r
        dx = -dx
    elif x - r < lbod:
        x = r
        dx = -dx
    else:
        x = x + dx
    if y + r > ubod or y + dy + r > ubod:
        y = ubod - r
        dy = -dy
    elif y - r < dbod or y - r + dy < dbod:
        y = r
        dy = -dy
    else:
        y = y + dy
    ellipse.setPos(x-r, y-r)

x = 0
dx = 1.03
dy = 1.0125
y = 0
rbod = 10
lbod = 0
ubod = 10
dbod = 0  # границы области
r = 1

rect = QtGui.QGraphicsRectItem(QtCore.QRectF(0, 0, 10, 10))
ellipse = QtGui.QGraphicsEllipseItem(QtCore.QRectF(x, y, 2*r, 2))
ellipse.setPen(pg.mkPen(100, 200, 100))
rect.setPen(pg.mkPen(200, 100, 100))
vb.addItem(ellipse)
vb.addItem(rect)
l.addItem(vb, 0, 1)
gv.centralWidget.setLayout(l)

t = QtCore.QTimer()
t.timeout.connect(updateData)
t.start(50)

sys.exit(app.exec_())