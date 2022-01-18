# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QObject

import pyqtgraph as pg
from pyqtgraph.graphicsItems.ScatterPlotItem import SpotItem
import numpy as np

import sys, traceback


class MyPlot(pg.GraphicsLayoutWidget):

    def setPointsData(self, scatter):
        pts = scatter.points()
        scatter_data = scatter.getData()
        for i, item in enumerate(pts):
            data = { 'x': scatter_data[0][i],
                     'y': scatter_data[1][i],
                    'index': i}
            item.setData(data)
            # print(pts[i].data())

    def mousePressEvent(self, event):
        try:
            print("\n\nplot widget: MousePressed: x=", event.pos().x(), "; y=", event.pos().y())

            if not self.getPlotItem().sceneBoundingRect().contains(event.pos()):
                return

            chartPoint = self.vb.mapSceneToView(event.pos())
            print("\n\nplot widget: Mouse point: x=", chartPoint.x(), "; y=", chartPoint.y())


            if self.lastClicked is not None:
                self.lastClicked.resetPen()
                self.lastClicked = None

            self.pred_X = chartPoint.x()
            self.pred_Y = chartPoint.y()

            pg.PlotWidget.mousePressEvent(self, event)
            for i in self.getPlotItem().dataItems:
                pts = i.scatter.pointsAt(chartPoint)
                if len(pts) > 0:
                    self.lastClicked = pts[0]
                    # p=pg.graphicsItems.ScatterPlotItem.SpotItem()
                    self.lastClicked.setPen('b', width=2)

                    data = i.getData()
                    # найти индекс, отвечающий за текущую точку
                    print("scatter point clicked coords=(",self.lastClicked.pos().x()
                                                        ,", ",self.lastClicked.pos().y(),")")
                    print("plot-chart point clicked coords=(", chartPoint.x(), ", ", chartPoint.y(), ")")
                    print("point data: ", self.lastClicked.data())
                    self.stopMoving = False
                    event.accept()
                    return
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
        # print("plot widget: release mouse event: x=", event.pos().x(), "; y=", event.pos().y())
        pg.PlotWidget.mouseReleaseEvent(self, event)
        self.stopMoving = True
        #self.setMouseEnabled(x=True, y=True)
        event.accept()

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        #pg.setConfigOption('leftButtonPan', False)
        # self.setMouseEnabled(x=False, y=False)
        #
        # self.plot_label = pg.LabelItem(justify='left', angle=0, text="LABEL")
        # self.getPlotItem().scene().addItem(self.plot_label)
        #
        # x = np.arange(100)
        # y = np.random.normal(size=100)
        # self.plot(x, y, pen=pg.mkPen(color=(255, 0, 0), width=1.5, style=QtCore.Qt.DotLine))
        #
        # x = []
        # self.y2 = []
        # for i in range(0, 250):
        #     x.append(i+0.01)
        #     # +0.01 --чтобы сетка по X была не int
        #     # - иначе будет перемещаться лишь по целым меткам,
        #     # т.е. с 142 на 143, но не на 142.5
        #     self.y2.append(np.exp(-i / 150.0) * np.cos(i / 10.0))
        # # self.plot(x, y2, pen=pg.mkPen(color=(0, 250, 0), width=1.5, style=QtCore.Qt.SolidLine))
        # self.chart = self.plot(x, self.y2, pen=pg.mkPen(color=(0, 250, 0), width=1.5, style=QtCore.Qt.SolidLine)
        #                , symbolBrush=(250, 250, 0), symbolPen='w', symbol='star', symbolSize=34, name="symbol='star'",
        #                fillLevel=-0.3, brush=(50, 50, 200, 100))
        # self.setPointsData(self.chart.scatter)
        # self.enableAutoRange('xy', False)
        #
        # # http://www.pyqtgraph.org/documentation/graphicsItems/plotdataitem.html
        # # self.setBackground(QtGui.QColor(127, 127, 127))
        # self.getPlotItem().setTitle("plot title")
        # # self.getPlotItem().listDataItems()[- 1].setFillBrush(pg.mkBrush(color=(0, 250, 0)))
        # # last_plot = self.getPlotItem().listDataItems()[- 1]
        # self.setLabel('left', "Y Axis", units='A')
        # # xScale.setLabel(, units="s")
        # self.setLabel('bottom', text="<span style='color: #ff0000; font-weight: bold'>X</span> <i>Axis</i>", units='s')
        #
        # self.crosshair()
        # # вариант с недостатками:
        # # self.chart.sigPointsClicked.connect(self._clicked)
        #
        # self.setXRange(139, 150)
        #
        # # чтобы не дергалось, когда нажимаешь не точно на центр маркера точки
        # self.pred_X = 0
        # self.pred_Y = 0
        #
        # self.stopMoving = True
        # self.lastClicked = None

    def crosshair(self):
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.addItem(self.vLine, ignoreBounds=True)
        self.addItem(self.hLine, ignoreBounds=True)

        self.vb = self.getPlotItem().vb

        # self.setMouseTracking(True)
        # or self.getPlotItem().scene().sigMouseMoved.connect(self.__mouseMoved)
        self.proxy = pg.SignalProxy(self.getPlotItem().scene().sigMouseMoved, rateLimit=60, slot=self.__mouseMoved)

    def __mouseMoved(self, evt):
        # evt[0]  ## using signal proxy turns original arguments into a tuple
        pos = evt[0]

        if pos.x() < 0 or pos.y() < 0:
            return

        try:
            index = -300

            if self.sceneBoundingRect().contains(pos):
                mousePoint = self.vb.mapSceneToView(pos)
                # print(">>>> -- rect contains")
                index = int(mousePoint.x())
            else:
                return

            #Label:
            if index >= 0 and index < len(self.y2):
                self.plot_label.setText(
                    "<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>" % (
                        mousePoint.x(), self.y2[index], index))  # data1[index], data2[index]))
            self.vLine.setPos(mousePoint.x())
            self.hLine.setPos(mousePoint.y())

            #Scatter point - drag
            if not self.stopMoving: #QtWidgets.QApplication.mouseButtons():


                ind = self.lastClicked.data()['index']
                print("drag a point is active; index: ", ind, " point data: ", self.lastClicked.data())

                data = self.chart.getData()
                dx = mousePoint.x() - self.pred_X
                dy = mousePoint.y() - self.pred_Y

                data[0][ind] = data[0][ind] + dx
                data[1][ind] = data[1][ind] + dy

                self.pred_X = mousePoint.x()
                self.pred_Y = mousePoint.y()

                self.chart.setData(x=data[0], y=data[1])
                self.setPointsData(self.chart.scatter)
                self.lastClicked = self.chart.scatter.points()[ind]
                self.lastClicked.setPen('b', width=2)

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

        self.__frame_time = 30

        # инициализация полей модели
        self.a = 3
        self.b = 2
        self.c = 1
        self.d = 1
        self.fox_start_population = 2
        self.rabbit_start_population = 3

        # инициализация формы
        hbox = QtWidgets.QHBoxLayout()

        self.vbox = QtWidgets.QVBoxLayout()
        self.plot = MyPlot()
        self.vbox.addWidget(self.plot)
        hbox.addLayout(self.vbox)


        box2 = QtWidgets.QGridLayout()
        hbox.addLayout(box2)

        irow = 0
        label = QtWidgets.QLabel("<b style='color: green'>a</b>")
        box2.addWidget(label, irow, 0)
        self.led_a = QtWidgets.QLineEdit(str(self.a))
        box2.addWidget(self.led_a, irow, 1)

        irow += 1
        label = QtWidgets.QLabel("<b style='color: green'>b</b>")
        box2.addWidget(label, irow, 0)
        self.led_b = QtWidgets.QLineEdit(str(self.b))
        box2.addWidget(self.led_b, irow, 1)

        irow += 1
        label = QtWidgets.QLabel("<b style='color: green'>c</b>")
        box2.addWidget(label, irow, 0)
        self.led_c = QtWidgets.QLineEdit()
        self.led_c.setText(str(self.c))
        box2.addWidget(self.led_c, irow, 1)

        irow += 1
        label = QtWidgets.QLabel("<b style='color: green'>d</b>")
        box2.addWidget(label, irow, 0)
        self.led_d = QtWidgets.QLineEdit()
        self.led_d.setText(str(self.d))
        box2.addWidget(self.led_d, irow, 1)

        irow +=1
        label = QtWidgets.QLabel("<b style='color: green'>Стартовая <br>популяция <br>кроликов</b>")
        box2.addWidget(label, irow, 0)
        self.led_rabbit_start_population = QtWidgets.QLineEdit()
        validator = QtGui.QRegExpValidator(QtCore.QRegExp(r"[1-9]\d{, }"))
        self.led_rabbit_start_population.setValidator(validator)
        self.led_rabbit_start_population.setText(str(self.rabbit_start_population))
        box2.addWidget(self.led_rabbit_start_population, irow, 1)

        irow += 1
        label = QtWidgets.QLabel("<b style='color: green'>Стартовая <br>популяция <br>лис</b>")
        box2.addWidget(label, irow, 0)
        self.led_fox_start_population = QtWidgets.QLineEdit()
        self.led_fox_start_population.setText(str(self.fox_start_population))
        box2.addWidget(self.led_fox_start_population, irow, 1)

        irow += 1
        self.bttn_start = QtWidgets.QPushButton("Старт")
        self.bttn_start.clicked.connect(self.slotOnBttnClicked)

        box2.addWidget(self.bttn_start, irow, 0)

        self.setLayout(hbox)
        self.resize(1200, 800)

        # GUI init - DONE
        # ==========================
        self.__timer_id = None
        self.__frame_curr_i = 0
        self.__frames_quo_max = 10000

    def slotOnBttnClicked(self):
        # TODO: 1. по нажатию на кнопку - записать параметры из полей в модель
        # ввести поля для хранения параметров модели
        if self.__timer_id is not None:
            self.killTimer(self.__timer_id)
            self.__frame_curr_i = 0

        _val = self.led_a.text()
        try:
            val_f = float(_val)
        except ValueError:
            print("Поле a заполнено не верно")
            return
        if val_f < 0:
            print("Поле a заполнено не верно")
            return
        self.a = val_f

        # TODO: Отрисовываются графики решения ДУ с текущими параметрами
        # т.е. перенести код из примера по ДУ для модели хищник-жертва

        # TODO: реализация функции-обработчика timeout
        # TODO: запуск анимационной модели (движения кроликов и лис)
        # TODO: запуск отрисовки графиков популяций

        self.__timer_id = self.startTimer(self.__frame_time)
        if self.__timer_id == -1:
            print("Не смог создать таймер - анимации больше не будет")
            return
        pass

    def animation_model__make_a_step(self):
        """
            1.Инициализация
                задано: начальная популяция лис и кролики
                и размер полотна
                простейший случай:
                    лисы
                        - массив ячеек [x, y] - их координаты на полотне
                        - у них есть свой график (PlotItem)
                            т.е. маркированный график
                        - поле "сколько тиков не менять направление движения"
                        - общее поле: величина перемещения за тик

                    кролики - аналогично


        """
        """
            1. есть массив зайцев
            2. есть массив лис
            скажем, что первыми ходят зайцы
            скорость ниже, чем у лис
            проходим в цикле по массиву зайцев
                заяц имеет радиус
                идем по всем лисам
                    math.sqrt(
                        (текущая_лиса.crd.x - текущий_заяц.crd.x)**2
                        --/--- для y
                    ) <= заяц.радиус_обзора
                    Беги лес! беги!
        """
        pass

    def timerEvent(self, event):
        self.__frame_curr_i += 1
        if self.__frame_curr_i > self.__frames_quo_max:
            self.killTimer(self.__timer_id)
            self.__timer_id = None
            return
        print("animation: frame: {}".format(self.__frame_curr_i))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())