# -*- coding: utf-8 -*-
"""
This example demonstrates the creation of a plot with a customized
AxisItem and ViewBox. 
"""


import pyqtgraph as pg
from PyQt5 import QtCore, QtGui
import numpy as np
import time


class DateAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        try:
            label1 = ''
            label2 = ''
            strns = []
            rng = max(values)-min(values)
            print("Range = ", rng)

            if rng < 120:
                return pg.AxisItem.tickStrings(self, values, scale, spacing)
            if rng < 3600*24:
                string = '%H:%M:%S'
                label1 = '%b %d -'
                label2 = ' %b %d, %Y'
            elif rng < 3600*24*30:
                string = '%d'
                label1 = '%b - '
                label2 = '%b, %Y'
            elif rng < 3600*24*30*24:
                string = '%b'
                label1 = '%Y -'
                label2 = ' %Y'
            else:
                string = '%Y'
                label1 = ''
                label2 = ''

            for x in values:
                try:
                    strns.append(time.strftime(string, time.localtime(x)))
                except ValueError:  ## Windows can't handle dates before 1970
                    strns.append('')
        except:
            pass

        try:
            label = time.strftime(label1, time.localtime(min(values)))+time.strftime(label2, time.localtime(max(values)))
        except ValueError:
            label = ''
        self.setLabel(text=label)
        return strns


class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)
        self.setMouseMode(self.RectMode)
        
    ## reimplement right-click to zoom out
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.autoRange()
            
    def mouseDragEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            ev.ignore()
        else:
            pg.ViewBox.mouseDragEvent(self, ev)

try:
    app = pg.mkQApp()

    axis = DateAxis(orientation='bottom')
    vb = CustomViewBox()

    pw = pg.PlotWidget(viewBox=vb, axisItems={'bottom': axis}, enableMenu=False
                       , title="PlotItem with custom axis and ViewBox<br>Menu disabled, mouse behavior changed: left-drag to zoom, right-click to reset zoom")
    dates = np.arange(1, 9)*(3600*24*365)
    print(dates)
    pw.plot(x=dates, y=[1,6,2,4,3,5,6,8], symbol='o')
    pw.show()
    pw.setWindowTitle('pyqtgraph example: customPlot')

except:
    pass

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    QtGui.QApplication.instance().exec_()
