from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import math
import sys


app = QtGui.QApplication([])

xVals = np.linspace(0, 100, 300, endpoint=True)
yVals = []
yVals2 = []

for x in xVals:
    yVals.append(math.sin(x))
    yVals2.append(math.cos(x + math.pi/3))

# pw = pg.plot(xVals, yVals, pen='r')  # plot x vs y in red
pw = pg.PlotItem()
pw.plot(xVals, yVals2, pen='b')
pw.show()
sys.exit(app.exec_())
