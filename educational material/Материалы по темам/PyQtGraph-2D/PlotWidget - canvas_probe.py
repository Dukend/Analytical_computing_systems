from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
import numpy as np
import sys


class GPS_navigator(pg.PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__init_plots()

        # self.__timer_id = self.startTimer(50)
        # if self.__timer_id == -1:
        #     print("GPS_navigator: не удалось создать таймер.")

    def __init_plots(self):
        canvas = self.getPlotItem()
        legend = canvas.addLegend(offset=(0, 0))

        pen = pg.mkPen(color=pg.mkColor(200, 200, 0), width=2)
        self.__plot_station = pg.PlotDataItem(
            np.array([[0, 0], [0, 2500], [2500, 2500], [2500, 0]])
            , pen=pen
            , symbolBrush=(255, 0, 200)
            , symbolPen='y'
            , symbol='star'
            , symbolSize=20
            , name="Item")
        canvas.addItem(self.__plot_station)
        # legend.addItem(self.__plot_station, " --- Item")

        vb = canvas  # .getViewBox() -- агрегируются
        vb.setRange(xRange=(-2000, 2000), yRange=(-2000, 2000))
        vb.disableAutoRange()
        vb.setAspectLocked(lock=True, ratio=1)
        vb.setLimits(xMin=-2200, xMax=2200, yMin=-2200, yMax=2200)

    def timerEvent(self, event):
        """ обновление времени и актуализация данных / отрисовки """
        # TODO
        self.__go_to_new_crd()

    def __go_to_new_crd(self):
        # TODO
        pass


class GPS_Widget(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Модуль 3: GPS навигатор")

        # стандартная разметка и установка layout
        splitter = QtWidgets.QSplitter()
        splitter.setHandleWidth(10)
        splitter.setOrientation(QtCore.Qt.Horizontal)

        self.setCentralWidget(splitter)
        self.setMinimumSize(800, 600)

        # Холст навигатора
        pg_view = GPS_navigator()
        self.__nav_canvas = pg_view
        splitter.addWidget(pg_view)

        # Панель точек назначения
        self.__init_route_panel(_lay=splitter)

    def __init_route_panel(self, _lay):
        splitter = QtWidgets.QSplitter()
        splitter.setHandleWidth(10)
        splitter.setOrientation(QtCore.Qt.Vertical)

        w = QtWidgets.QWidget()
        vlay = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel()
        label.setText("Боковая панель")
        label.setStyleSheet("QLabel{ color: green; font-weight: bold; font-size: 35px;}")
        label.setAlignment(QtCore.Qt.AlignHCenter)
        label.setWordWrap(True)
        vlay.addWidget(label)

        l = QtWidgets.QListWidget()
        vlay.addWidget(l)

        w.setLayout(vlay)
        splitter.addWidget(w)
        _lay.addWidget(splitter)
        self.__route_list_widget = l
        self.__route_array = None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GPS_Widget()  # Создаем экземпляр класса
    window.setWindowTitle("Загрузка вх. данных и обработка")
    window.show()  # Отображаем окно
    sys.exit(app.exec_())  # Запускаем цикл обработки событий