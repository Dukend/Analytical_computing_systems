# -*- coding: utf-8 -*-
"""
Demonstrates a variety of uses for ROI. This class provides a user-adjustable
region of interest marker. It is possible to customize the layout and 
function of the scale/rotate handles in very flexible ways. 
"""

import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sys


app = QtWidgets.QApplication(sys.argv)

pg.setConfigOptions(imageAxisOrder='row-major')

## Create image to display
arr = np.ones((100, 100), dtype=float)
arr[45:55, 45:55] = 0
arr[25, :] = 5
arr[:, 25] = 5
arr[75, :] = 5
arr[:, 75] = 5
arr[50, :] = 10
arr[:, 50] = 10
arr += np.sin(np.linspace(0, 20, 100)).reshape(1, 100)
arr += np.random.normal(size=(100,100))

# add an arrow for asymmetry
arr[10, :50] = 10
arr[9:12, 44:48] = 10
arr[8:13, 44:46] = 10


## create GUI
app = QtGui.QApplication([])
w = pg.GraphicsWindow(size=(1000,800), border=True)
w.setWindowTitle('pyqtgraph example: ROI Examples')

text = """Data Selection From Image.<br>\n
Drag an ROI or its handles to update the selected image.<br>
Hold CTRL while dragging to snap to pixel boundaries<br>
and 15-degree rotation angles.
"""
w1 = w.addLayout(row=0, col=0)
label1 = w1.addLabel(text, row=0, col=0)
v1a = w1.addViewBox(row=1, col=0, lockAspect=True)
v1b = w1.addViewBox(row=2, col=0, lockAspect=True)
img1a = pg.ImageItem(arr)
v1a.addItem(img1a)
img1b = pg.ImageItem()
v1b.addItem(img1b)
v1a.disableAutoRange('xy')
v1b.disableAutoRange('xy')
v1a.autoRange()
v1b.autoRange()

roi = pg.RectROI([20, 20], [60, 60], pen=(0, 9))
roi.addRotateHandle([1, 0], [0.5, 0.5])

def update(roi):
    img1b.setImage(roi.getArrayRegion(arr, img1a), levels=(0, arr.max()))
    v1b.autoRange()
    
roi.sigRegionChanged.connect(update)
v1a.addItem(roi)

update(roi)
    
    
sys.exit(app.exec_())