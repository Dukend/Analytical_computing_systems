# -*- coding: utf-8 -*-
"""
Various methods of drawing scrolling plots.
"""
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui
import numpy as np

try:
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


# update all plots
def update():
    try:
        update1()
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
try:
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(50)
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


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
