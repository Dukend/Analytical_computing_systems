"""
Various methods of drawing scrolling plots.
"""

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import numpy as np
import sys


app = QtWidgets.QApplication(sys.argv)

win = pg.GraphicsWindow()
win.setWindowTitle('pyqtgraph example: Scrolling Plots')


# 1) Simplest approach -- update data in the array such that plot appears to scroll
#    In these examples, the array size is fixed.
p1 = win.addPlot()
p2 = win.addPlot()
data1 = np.random.normal(size=300)
curve1 = p1.plot(data1)
curve2 = p2.plot(data1)
ptr1 = 0
def update1():
    try:
        global data1, curve1, ptr1
        data1[:-1] = data1[1:]  # shift data in the array one sample left
                                # (see also: np.roll)
        data1[-1] = np.random.normal()
        curve1.setData(data1)

        ptr1 += 1
        curve2.setData(data1)
        curve2.setPos(ptr1, 0)
    except:
        Type, Value, Trace = sys.exc_info()
        print("Type: ", Type)
        print("Value:", Value)
        print("Trace:", Trace)
        print("\n", "print_exception()".center(40, "-"))
        traceback.print_exception(Type, Value, Trace, limit=5,
                                  file=sys.stdout)
        print("\n", "print_tb()".center(40, "-"))
        traceback.print_tb(Trace, limit=1, file=sys.stdout)
        print("\n", "format_exception()".center(40, "-"))
        print(traceback.format_exception(Type, Value, Trace, limit=5))
        print("\n", "format_exception_only()".center(40, "-"))
        print(traceback.format_exception_only(Type, Value))
        exit(-11)

# 2) Allow data to accumulate. In these examples, the array doubles in length
#    whenever it is full. 
win.nextRow()
p3 = win.addPlot()
p4 = win.addPlot()
# Use automatic downsampling and clipping to reduce the drawing load
p3.setDownsampling(mode='peak')
p4.setDownsampling(mode='peak')
p3.setClipToView(True)
p4.setClipToView(True)
p3.setRange(xRange=[-100, 0])
p3.setLimits(xMax=0)
curve3 = p3.plot()
curve4 = p4.plot()

data3 = np.empty(100)
ptr3 = 0

def update2():
    try:
        global data3, ptr3
        data3[ptr3] = np.random.normal()
        ptr3 += 1
        if ptr3 >= data3.shape[0]:
            tmp = data3
            data3 = np.empty(data3.shape[0] * 2)
            data3[:tmp.shape[0]] = tmp
        curve3.setData(data3[:ptr3])
        curve3.setPos(-ptr3, 0)
        curve4.setData(data3[:ptr3])
    except:
        Type, Value, Trace = sys.exc_info()
        print("Type: ", Type)
        print("Value:", Value)
        print("Trace:", Trace)
        print("\n", "print_exception()".center(40, "-"))
        traceback.print_exception(Type, Value, Trace, limit=5,
                                  file=sys.stdout)
        print("\n", "print_tb()".center(40, "-"))
        traceback.print_tb(Trace, limit=1, file=sys.stdout)
        print("\n", "format_exception()".center(40, "-"))
        print(traceback.format_exception(Type, Value, Trace, limit=5))
        print("\n", "format_exception_only()".center(40, "-"))
        print(traceback.format_exception_only(Type, Value))
        exit(-11)


# 3) Plot in chunks, adding one new plot curve for every 100 samples
chunkSize = 100
# Remove chunks after we have 10
maxChunks = 10
startTime = pg.ptime.time()
win.nextRow()
p5 = win.addPlot(colspan=2)
p5.setLabel('bottom', 'Time', 's')
p5.setXRange(-10, 0)
curves = []
data5 = np.empty((chunkSize+1,2))
ptr5 = 0

def update3():
    try:
        global p5, data5, ptr5, curves
        now = pg.ptime.time()
        for c in curves:
            c.setPos(-(now-startTime), 0)

        i = ptr5 % chunkSize
        if i == 0:
            curve = p5.plot()
            curves.append(curve)
            last = data5[-1]
            data5 = np.empty((chunkSize+1,2))
            data5[0] = last
            while len(curves) > maxChunks:
                c = curves.pop(0)
                p5.removeItem(c)
        else:
            curve = curves[-1]
        data5[i+1,0] = now - startTime
        data5[i+1,1] = np.random.normal()
        curve.setData(x=data5[:i+2, 0], y=data5[:i+2, 1])
        ptr5 += 1
    except:
        Type, Value, Trace = sys.exc_info()
        print("Type: ", Type)
        print("Value:", Value)
        print("Trace:", Trace)
        print("\n", "print_exception()".center(40, "-"))
        traceback.print_exception(Type, Value, Trace, limit=5,
                                  file=sys.stdout)
        print("\n", "print_tb()".center(40, "-"))
        traceback.print_tb(Trace, limit=1, file=sys.stdout)
        print("\n", "format_exception()".center(40, "-"))
        print(traceback.format_exception(Type, Value, Trace, limit=5))
        print("\n", "format_exception_only()".center(40, "-"))
        print(traceback.format_exception_only(Type, Value))
        exit(-11)


# update all plots
def update():
    update1()
    update2()
    update3()
timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)


sys.exit(app.exec_())