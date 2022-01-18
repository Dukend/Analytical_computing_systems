from PyQt5 import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
import numpy as np


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Привет, мир!")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btnQuit = QtWidgets.QPushButton("&Закрыть окно")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)

        self.init_plot()

        self.vbox.addWidget(self.plot)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)

        self.setMinimumHeight(800)
        self.setMinimumWidth(1600)

    def init_plot(self):
        self.plot = pg.PlotWidget()

        self.label = pg.LabelItem(justify='left', angle=180, text="LABEL")
        self.plot.getPlotItem().addItem(self.label)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    curLocale=QtCore.QLocale(QtCore.QLocale("en_US"))
    QtCore.QLocale.setDefault(curLocale)

    window = MyWindow()   # Создаем экземпляр класса
    window.setWindowTitle("LABEL")
    window.resize(300, 70)
    window.show()         # Отображаем окно

    sys.exit(app.exec_()) # Запускаем цикл обработки событий