# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QObject

import pyqtgraph as pg
from pyqtgraph.graphicsItems.ScatterPlotItem import SpotItem
import numpy as np

import sys, traceback


class MyPlot(pg.PlotWidget):
    # setCursor(Qt::OpenHandCursor);

    # unsetCursor();
    # QApplication::setOverrideCursor(Qt::ClosedHandCursor)

    def keyPressEvent(self, ev):
        try:
            if ev.key() == QtCore.Qt.Key_Space:
                self.space_is_pressed = True
                if self.stopMoving == False:
                    # mousePoint = self.vb.mapSceneToView(ev.pos())
                    # self.pred_X = mousePoint.x()
                    # self.pred_Y = mousePoint.y()
                    self.setCursor(QtCore.Qt.ClosedHandCursor)
                else:
                    self.setCursor(QtCore.Qt.OpenHandCursor)
            elif ev.key() == QtCore.Qt.Key_Left:
                r = self.viewRange()
                delta_range = self.vb.mapSceneToView(QtCore.QPoint(0, 0)) - self.vb.mapSceneToView(QtCore.QPoint(self.drag_delta, self.drag_delta))
                x_new_1 = r[0][0] + delta_range.x()
                x_new_2 = r[0][1] + delta_range.x()
                self.setXRange(x_new_1, x_new_2, padding=0)
            elif ev.key() == QtCore.Qt.Key_Right:
                r = self.viewRange()
                delta_range = self.vb.mapSceneToView(QtCore.QPoint(0,0)) - self.vb.mapSceneToView(QtCore.QPoint(self.drag_delta, self.drag_delta))
                x_new_1=r[0][0] - delta_range.x()
                x_new_2=r[0][1] - delta_range.x()
                self.setXRange(x_new_1, x_new_2, padding=0)
            elif ev.key() == QtCore.Qt.Key_Up:
                r = self.viewRange()
                delta_range = self.vb.mapSceneToView(QtCore.QPoint(0, 0)) - self.vb.mapSceneToView(
                    QtCore.QPoint(self.drag_delta, self.drag_delta))
                y_new_1 = r[1][0] + delta_range.y()
                y_new_2 = r[1][1] + delta_range.y()
                self.setYRange(y_new_1, y_new_2, padding=0)
            elif ev.key() == QtCore.Qt.Key_Down:
                r = self.viewRange()
                delta_range = self.vb.mapSceneToView(QtCore.QPoint(0, 0)) - self.vb.mapSceneToView(
                    QtCore.QPoint(self.drag_delta, self.drag_delta))
                y_new_1 = r[1][0] - delta_range.y()
                y_new_2 = r[1][1] - delta_range.y()
                self.setYRange(y_new_1, y_new_2, padding=0)
            elif ev.key() == QtCore.Qt.Key_Plus or ev.key() == QtCore.Qt.Key_Equal:
                modifiers = QtGui.QGuiApplication.queryKeyboardModifiers()
                if bool(modifiers == QtCore.Qt.ControlModifier):
                    print('Control and \'+\'')
                    self.zoom(1)
            elif ev.key() == QtCore.Qt.Key_Minus:
                modifiers = QtGui.QGuiApplication.queryKeyboardModifiers()
                if bool(modifiers == QtCore.Qt.ControlModifier):
                    self.zoom(-1)
            elif ev.key() == QtCore.Qt.Key_0:
                modifiers = QtGui.QGuiApplication.queryKeyboardModifiers()
                if bool(modifiers == QtCore.Qt.ControlModifier):
                    print('Control and \'0\'')
                    self.zoom(0)

            pg.PlotWidget.keyPressEvent(self, ev)
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

    def keyReleaseEvent(self, ev):
        try:
            if ev.key() == QtCore.Qt.Key_Space:
                self.space_is_pressed = False
                self.unsetCursor()
            pg.PlotWidget.keyReleaseEvent(self, ev)
        except:
            pass

    def mousePressEvent(self, ev):
        try:
            print("\nplot widget: MousePressed: x=", ev.pos().x(), "; y=", ev.pos().y())

            if not self.getPlotItem().sceneBoundingRect().contains(ev.pos()):
                pg.PlotWidget.mousePressEvent(self, ev)
                return

            #modifiers = QtGui.QGuiApplication.queryKeyboardModifiers()
            # if bool(ev.buttons() & QtCore.Qt.LeftButton) and bool(modifiers == QtCore.Qt.ControlModifier):
            #    print('Control+Click')
            # else:
            #    print('not Control+Click')
            #    pg.PlotWidget.mousePressEvent(self, ev)
            #    return

            self.stopMoving = False
            if self.space_is_pressed:
                print("space is pressed: make the hand cursor")
                # self.unsetCursor()
                mousePoint = self.getPlotItem().getViewBox().mapSceneToView(ev.pos())
                self.pred_X = mousePoint.x()
                self.pred_Y = mousePoint.y()
                self.setCursor(QtCore.Qt.ClosedHandCursor)

            ev.accept()
            pg.PlotWidget.mousePressEvent(self, ev)
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

    def mouseReleaseEvent(self, event):
        print("plot widget: release mouse event: x=", event.pos().x(), "; y=", event.pos().y())
        pg.PlotWidget.mouseReleaseEvent(self, event)

        self.stopMoving = True
        print("stopMoving: ", self.stopMoving, "; space_is_pressed: ", self.space_is_pressed)

        # self.unsetCursor()
        if self.space_is_pressed:
            print("set cursor to openHand")
            self.setCursor(QtCore.Qt.OpenHandCursor)
        else:
            print("set cursor to arrow")
            self.unsetCursor()
            # self.setCursor(QtCore.Qt.ArrowCursor)

            # QtWidgets.QApplication.restoreOverrideCursor()
        # self.space_is_pressed = False
        # self.setMouseEnabled(x=True, y=True)

    def zoom(self, scale):
        if scale > 0.01:
            self.getPlotItem().vb.scaleBy((1 / self.scale_step, 1 / self.scale_step))  # getScale('bottom').setScale(curr_scale - 0.5)
            self.scale_curr = self.scale_curr / self.scale_step
        elif scale < -0.01:
            self.getPlotItem().vb.scaleBy((self.scale_step, self.scale_step))  # getScale('bottom').setScale(curr_scale - 0.5)
            self.scale_curr = self.scale_curr * self.scale_step
        else:
            self.getPlotItem().vb.scaleBy((1 / self.scale_curr, 1 / self.scale_curr))  # getScale('bottom').setScale(curr_scale - 0.5)
            self.scale_curr = 1

    def wheelEvent(self, ev):
        try:
            modifiers = QtGui.QGuiApplication.queryKeyboardModifiers()
            if bool(modifiers == QtCore.Qt.ControlModifier):
                numPixels = ev.pixelDelta()
                numDegrees = ev.angleDelta() / 8
                print("Piixels: ", numPixels)
                print("Degreee: ", numDegrees)
                if numDegrees.y() > 0:
                    self.zoom(1)
                elif numDegrees.y() < 0:
                    self.zoom(-1)

                ev.accept()
            pg.PlotWidget.wheelEvent(self, ev)
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

    def __init__(self, parent=None):
        pg.PlotWidget.__init__(self, parent)

        # pg.setConfigOption('leftButtonPan', False)
        self.setMouseEnabled(x=False, y=False)

        self.plot_label = pg.LabelItem(justify='left', angle=0, text="LABEL")
        self.getPlotItem().scene().addItem(self.plot_label)

        x = np.arange(100)
        y = np.random.normal(size=100)
        self.plot(x, y, pen=pg.mkPen(color=(255, 0, 0), width=1.5, style=QtCore.Qt.DotLine))

        x = []
        self.y2 = []
        for i in range(0, 250):
            x.append(i + 0.01)
            # +0.01 --чтобы сетка по X была не int
            # - иначе будет перемещаться лишь по целым меткам,
            # т.е. с 142 на 143, но не на 142.5
            self.y2.append(np.exp(-i / 150.0) * np.cos(i / 10.0))
        # self.plot(x, y2, pen=pg.mkPen(color=(0, 250, 0), width=1.5, style=QtCore.Qt.SolidLine))
        self.chart = self.plot(x, self.y2, pen=pg.mkPen(color=(0, 250, 0), width=1.5, style=QtCore.Qt.SolidLine)
                               , symbolBrush=(250, 250, 0), symbolPen='w', symbol='star', symbolSize=34,
                               name="symbol='star'",
                               fillLevel=-0.3, brush=(50, 50, 200, 100))
        self.enableAutoRange('xy', False)

        # http://www.pyqtgraph.org/documentation/graphicsItems/plotdataitem.html
        # self.setBackground(QtGui.QColor(127, 127, 127))
        self.getPlotItem().setTitle("plot title")
        # self.getPlotItem().listDataItems()[- 1].setFillBrush(pg.mkBrush(color=(0, 250, 0)))
        # last_plot = self.getPlotItem().listDataItems()[- 1]
        self.setLabel('left', "Y Axis", units='A')
        # xScale.setLabel(, units="s")
        self.setLabel('bottom', text="<span style='color: #ff0000; font-weight: bold'>X</span> <i>Axis</i>", units='s')

        self.vb = self.getPlotItem().vb

        # self.setMouseTracking(True)
        # or self.getPlotItem().scene().sigMouseMoved.connect(self.__mouseMoved)
        self.proxy = pg.SignalProxy(self.getPlotItem().scene().sigMouseMoved, rateLimit=60, slot=self.__mouseMoved)

        self.setXRange(139.0, 150.0)
        self.scale_curr = 1.0
        self.scale_step = 1.25

        # чтобы не дергалось, когда нажимаешь не точно на центр маркера точки
        self.pred_X = 0
        self.pred_Y = 0

        self.stopMoving = True
        self.lastClicked = None
        self.last_clicked_point_index = 0
        self.space_is_pressed = False
        self.drag_delta = 100
        self.getPlotItem().showAxis(axis='bottom')
        self.vb.setAspectLocked()
        self.vb.setLimits(xMin=-10, xMax=255)#, minXRange=-5, maxXRange=300)
        # self.enableAutoRange('xy', False)


    def __mouseMoved(self, evt):
        try:
            # evt[0]  ## using signal proxy turns original arguments into a tuple
            pos = evt[0]

            if self.stopMoving:
                return
            if not self.space_is_pressed:
                return
            if pos.x() < 0 or pos.y() < 0:
                return
            if not self.sceneBoundingRect().contains(pos):
                return


            mousePoint = self.vb.mapSceneToView(pos)
            dx = self.pred_X - mousePoint.x()
            dy = self.pred_Y - mousePoint.y()

            print("dy = ", dy)
            print("curr Y range")

            self.pred_X = mousePoint.x()+dx
            self.pred_Y = mousePoint.y()+dy

            r = self.viewRange()
            y_new_1 = r[1][0] + dy
            y_new_2 = r[1][1] + dy
            x_new_1 = r[0][0] + dx
            x_new_2 = r[0][1] + dx
            self.setXRange(x_new_1, x_new_2, padding=0)
            self.setYRange(y_new_1, y_new_2, padding=0)

            # перерисовать, а то scatter'ы отвалятся
            self.chart.updateItems()
            QtWidgets.QApplication.processEvents()

        except:
            print("!!!!!Exception ")

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


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("pyqtgraph example 1: Simple usage")
        self.vbox = QtWidgets.QVBoxLayout()
        self.plot = MyPlot()
        self.vbox.addWidget(self.plot)
        self.setLayout(self.vbox)
        self.resize(1200, 800)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
