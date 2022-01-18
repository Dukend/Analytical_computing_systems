from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys


class MyWidget(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Пример окна QWidget с полотном 3D PyQtGraph")

        # main_widget = QtWidgets.QWidget()
        # lay = QtWidgets.QVBoxLayout()
        # main_widget.setLayout(lay)

        # Холст 3D
        main_widget = gl.GLViewWidget()
        self.__canvas = main_widget
        self.setCentralWidget(main_widget)
        self.setMinimumSize(800, 600)

        self.__draw()
        self.setWindowTitle('pyqtgraph 3D example: GLLinePlotItem')

        # Холст 2D
        # pg_view = pg.GraphicsView()
        # pg_canvas = pg.PlotItem()
        # pg_view.setCentralWidget(pg_canvas)
        # self.__nav_canvas_vb = pg_canvas.vb
        # self.__nav_canvas = pg_canvas
        # self.__nav_canvas_view = pg_view
        # lay.addWidget(pg_view)

    def __draw(self):
        w = self.__canvas
        w.opts['distance'] = 40

        gx = gl.GLGridItem()
        gx.rotate(90, 0, 1, 0)
        gx.translate(-10, 0, 0)
        w.addItem(gx)
        gy = gl.GLGridItem()
        gy.rotate(90, 1, 0, 0)
        gy.translate(0, -10, 0)
        w.addItem(gy)
        gz = gl.GLGridItem()
        gz.translate(0, 0, -10)
        w.addItem(gz)

        n = 51
        y = np.linspace(-10, 10, n)
        x = np.linspace(-10, 10, 100)
        for i in range(n):
            yi = np.array([y[i]] * 100)
            d = (x ** 2 + yi ** 2) ** 0.5
            z = 10 * np.cos(d) / (d + 1)
            pts = np.vstack([x, yi, z]).transpose()
            plt = gl.GLLinePlotItem(pos=pts, color=pg.glColor((i, n * 1.3)), width=(i + 1) / 10., antialias=True)
            w.addItem(plt)

    
if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseDesktopOpenGL)
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()   # Создаем экземпляр класса
    window.setWindowTitle("Загрузка вх. данных и обработка")
    window.show()         # Отображаем окно
    sys.exit(app.exec_())  # Запускаем цикл обработки событий
