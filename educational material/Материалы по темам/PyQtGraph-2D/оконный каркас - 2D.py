from PyQt5 import QtCore, QtWidgets, QtGui, QtSerialPort
import pyqtgraph as pg
import numpy as np
import math
import sys


class GPS_Widget(QtWidgets.QMainWindow):
    # signal_to_baud_rate_change = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Пример использования собственного диалога")

        # стандартная разметка для QWidget
        main_widget = QtWidgets.QWidget()
        lay = QtWidgets.QVBoxLayout()
        main_widget.setLayout(lay)
        self.setCentralWidget(main_widget)
        self.setMinimumSize(800, 600)

        # Холст с графиками (2D pyqtgraph)
        pg_view = pg.GraphicsView()
        pg_canvas = pg.PlotItem()
        pg_view.setCentralWidget(pg_canvas)
        self.__nav_canvas_vb = pg_canvas.vb
        self.__nav_canvas = pg_canvas
        self.__nav_canvas_view = pg_view
        lay.addWidget(pg_view)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GPS_Widget()   # Создаем экземпляр класса
    window.setWindowTitle("Загрузка вх. данных и обработка")
    window.show()         # Отображаем окно
    sys.exit(app.exec_()) # Запускаем цикл обработки событий