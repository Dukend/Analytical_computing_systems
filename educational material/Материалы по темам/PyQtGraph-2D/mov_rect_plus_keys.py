"""
ViewBox is the general-purpose graphical container that allows the user to
zoom / pan to inspect any area of a 2D coordinate system.

This unimaginative example demonstrates the constrution of a ViewBox-based
plot area with axes, very similar to the way PlotItem is built.
"""

## This example uses a ViewBox to create a PlotWidget-like interface

import numpy as np
from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
import sys

app = QtWidgets.QApplication(sys.argv)

mw = QtGui.QMainWindow()
mw.setWindowTitle('pyqtgraph example: ViewBox')
mw.show()
mw.resize(800, 600)

gw = pg.PlotWidget()
mw.setCentralWidget(gw)

vb = gw.getPlotItem().getViewBox()
print("vb == ", vb)

# vb = pg.ViewBox()

p1 = pg.PlotDataItem()
vb.addItem(p1)


## Just something to play with inside the ViewBox
class movableRect(QtGui.QGraphicsRectItem):
    def __init__(self, *args):
        QtGui.QGraphicsRectItem.__init__(self, *args)
        self.setAcceptHoverEvents(True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsFocusable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        # self.setFocus()

    def hoverEnterEvent(self, ev):
        self.savedPen = self.pen()
        self.setPen(pg.mkPen(255, 255, 255))
        ev.ignore()

    def hoverLeaveEvent(self, ev):
        self.setPen(self.savedPen)
        ev.ignore()

    def mousePressEvent(self, ev):
        if ev.button() == QtCore.Qt.LeftButton:
            ev.accept()
            self.pressDelta = self.mapToParent(ev.pos()) - self.pos()
        else:
            ev.ignore()

    def mouseMoveEvent(self, ev):
        self.setPos(self.mapToParent(ev.pos()) - self.pressDelta)

    def keyPressEvent(self, ev):
        if ev.key() == QtCore.Qt.Key_Space:
            print("rectItem:: space is pressed!")
            ev.accept()
            return
        ev.ignore()

    def focus_changed(self):
        print("focus changed! : ", mw.sender())
        # self.setFocus()


rect = movableRect(QtCore.QRectF(0, 0, 1, 1))
rect.setPen(pg.mkPen(100, 200, 100))
vb.addItem(rect)
rect.grabKeyboard()
sc = QtWidgets.QGraphicsScene()
# vb.setScene(sc)

print("vb. scene = =", vb.scene())
vb.scene().focusItemChanged.connect(rect.focus_changed)
# vb.scene().setStickyFocus(True)


def rand(n):
    data = np.random.random(n)
    data[int(n * 0.1):int(n * 0.13)] += .5
    data[int(n * 0.18)] += 2
    data[int(n * 0.1):int(n * 0.13)] *= 5
    data[int(n * 0.18)] *= 20
    return data, np.arange(n, n + len(data)) / float(n)


def updateData():
    yd, xd = rand(10000)
    p1.setData(y=yd, x=xd)


yd, xd = rand(10000)
updateData()
vb.autoRange()

t = QtCore.QTimer()
t.timeout.connect(updateData)
t.start(50)

sys.exit(app.exec_())
