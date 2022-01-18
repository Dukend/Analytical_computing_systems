import pyqtgraph as pg
import numpy as np
from pyqtgraph.Qt import QtCore, QtGui

app = pg.mkQApp()

pw = pg.PlotWidget(title="Example")
x = np.arange(20)
y = x**2/150
pw.plot(x=x, y=y, symbol='o')
pw.show()
pw.setWindowTitle('Example')

ax = pw.getAxis('bottom')  # This is the trick
dx = [(value, str(value)) for value in list((range(int(min(x.tolist())), int(max(x.tolist())+1))))]
ax.setTicks([dx, []])

ay = pw.getAxis('left')  # This is the trick
dy = [(value, str(value)) for value in list((range(int(min(y.tolist())), int(max(y.tolist())+1))))]
ay.setTicks([dy, []])

if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()