from PyQt5 import QtCore, QtWidgets, QtGui, QtSerialPort
import pyqtgraph as pg
import numpy as np
import math
import sys

"""
    Пример создания собственного диалога на базе стандартного класса QDialog.
    slot-signal
    Фильтрация / сопоставление сигналов (signal mapper)
    QMenu, QAction
    Встраивание холста PyQtGraph 2D
"""


class GPS_choose_COM_port_dialog(QtWidgets.QDialog):
    def __init__(self,  parent=None):
        super().__init__(parent)

        self.setWindowTitle("Выберите COM порт для поключения GPS")
        self.setWindowFlags(QtCore.Qt.Window
                            | QtCore.Qt.WindowMinimizeButtonHint
                            | QtCore.Qt.WindowMaximizeButtonHint
                            | QtCore.Qt.WindowCloseButtonHint)

        lay = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        vbox_left = QtWidgets.QVBoxLayout()
        vbox_right = QtWidgets.QVBoxLayout()
        hbox.addLayout(vbox_left)
        hbox.addLayout(vbox_right)
        lay.addLayout(hbox)

        label = QtWidgets.QLabel("Порт COM")
        label.setStyleSheet("QLabel{color: green; font-weight: bold;}")
        vbox_left.addWidget(label)
        port_list_widget = QtWidgets.QListWidget()
        self.__port_list_widget = port_list_widget
        vbox_left.addWidget(port_list_widget)
        vbox_left.setAlignment(QtCore.Qt.AlignTop)

        label = QtWidgets.QLabel("Описание")
        label.setStyleSheet("QLabel{color: green; font-weight: bold;}")
        vbox_right.addWidget(label)
        label = QtWidgets.QLabel("---")
        label.setWordWrap(True)
        self.__descr_label = label
        vbox_right.addWidget(label)
        vbox_right.setAlignment(QtCore.Qt.AlignTop)

        ser = QtSerialPort.QSerialPortInfo()
        port_info_list = ser.availablePorts()
        self.__port_info_list = port_info_list
        port_name_list = []
        for l in port_info_list:
            port_name_list.append(l.portName())
        port_list_widget.addItems(port_name_list)
        self.__select_a_port(0)

        buttonBox = QtWidgets.QDialogButtonBox()
        self.__button_ok = buttonBox.addButton("Ok", QtWidgets.QDialogButtonBox.AcceptRole)
        buttonBox.addButton("Отмена", QtWidgets.QDialogButtonBox.RejectRole)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        self.__buttonBox = buttonBox
        lay.addWidget(buttonBox, alignment=QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)
        self.setLayout(lay)

        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        hbox.setStretchFactor(vbox_left, 2)
        hbox.setStretchFactor(vbox_right, 3)
        lay.setSpacing(20)
        lay.setContentsMargins(30, 20, 30, 20)
        buttonBox.setStyleSheet("QPushButton{ margin: 0px 10px 0px 10px;")
            # "padding: 10px 20px 10px 20px; border: 1px solid black;}")
        # self.__button_ok.setContentsMargins(100, 20, 30, 100)
        hbox.setSpacing(10)
        vbox_right.setSpacing(20)
        vbox_left.setSpacing(20)
        port_list_widget.currentRowChanged.connect(self.__select_a_port)

    def __select_a_port(self, _i):
        if (_i + 1) > len(self.__port_info_list):
            return False

        port = self.__port_info_list[_i]
        busy = "Нет"
        if port.isBusy():
            busy = "Да"
        valid = "Нет"
        if port.isValid():
            valid = "Да"

        descr = "Устройство: {0}\nПроизводитель: {1}\nЗанято: {2}\nРаботает корректно: {3}"\
            .format(  port.description()
                    , port.manufacturer()
                    , busy
                    , valid)
        self.__descr_label.setText(descr)
        self.__port_list_widget.setCurrentRow(_i)

        return True

    @property
    def portName(self):
        if len(self.__port_info_list):
            return self.__port_info_list[self.__port_list_widget.currentRow()].portName()
        return None


class GPS_Widget(QtWidgets.QMainWindow):
    # signal_to_baud_rate_change = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Пример использования собственного диалога")

        self.__init_menu()

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

    def __init_menu(self):
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&Файл')

        action = QtWidgets.QAction('&Подключить GPS-модуль..', self)
        action.triggered.connect(self.__connect_GPS_dialog)
        self.__action_connect = action
        fileMenu.addAction(action)

        self.__add_baudrates(fileMenu)

        exitAction = QtWidgets.QAction('&Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выход')
        exitAction.triggered.connect(self.close)

        fileMenu.addAction(exitAction)

    @QtCore.pyqtSlot()
    def __connect_GPS_dialog(self):
        # self.__action_disconnect.setEnabled(False)
        # self.__action_connect.setEnabled(False)

        dlg = GPS_choose_COM_port_dialog(parent=self)
        if not dlg.exec_():
            # self.__action_disconnect.setEnabled(False)
            # self.__action_connect.setEnabled(True)
            return
        print("dlg: port name: ", dlg.portName)

    def __add_baudrates(self, fileMenu):
        baudrate_menu = fileMenu.addMenu("&Установить baudrate")
        ser = QtSerialPort.QSerialPortInfo()
        baudrate_list = ser.standardBaudRates()
        self.__baudrate_list = baudrate_list
        self.__baudrate_actions = []
        self.__mapper = QtCore.QSignalMapper(self)
        i = 0
        for b in baudrate_list:
            action = QtWidgets.QAction('{}'.format(b), self)
            action.setCheckable(True)
            self.__baudrate_actions.append(action)
            action.triggered.connect(self.__mapper.map)
            self.__mapper.setMapping(action, i)
            i += 1
        self.__mapper.mapped['int'].connect(self.__set_baudrate)

        i = len(baudrate_list)
        if i:
            i = int(i / 2) - 1
            if i < 0:
                i = 0
            self.__baudrate_actions[i].setChecked(True)
            self.__baudrate_curr_i = i

        baudrate_menu.addActions(self.__baudrate_actions)

        fileMenu.addSeparator()

    @QtCore.pyqtSlot(int)
    def __set_baudrate(self, _baudrate):
        print("baudrate is set")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GPS_Widget()   # Создаем экземпляр класса
    window.setWindowTitle("Загрузка вх. данных и обработка")
    window.show()         # Отображаем окно
    sys.exit(app.exec_()) # Запускаем цикл обработки событий