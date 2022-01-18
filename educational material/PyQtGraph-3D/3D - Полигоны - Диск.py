from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import pyqtgraph.opengl as gl
import numpy as np
import sys
import math


"""
    Простейший пример использования полигонов (GLMeshItem)
    Отрисовывем не контур, а диск орбиты.
"""


def get_rot_mat(_axis, _angle_rad):
    assert math.fabs(_angle_rad) < 2*math.pi, "Видимо, забыли перевести угол в радианы"
    if _axis == 'x':
        return np.array([[1, 0, 0],
                         [0, math.cos(_angle_rad), math.sin(_angle_rad)],
                         [0, -math.sin(_angle_rad), math.cos(_angle_rad)]])
    if _axis == 'y':
        return np.array([[math.cos(_angle_rad), 0, math.sin(_angle_rad)],
                         [0, 1, 0],
                         [-math.sin(_angle_rad), 0, math.cos(_angle_rad)]])
    if _axis == 'z':
        return np.array([[math.cos(_angle_rad), math.sin(_angle_rad), 0],
                         [-math.sin(_angle_rad), math.cos(_angle_rad), 0],
                         [0, 0, 1]])

    print("get_rot_mat: wrong input")
    exit(-9)


def get_disk_3D_item(_a=20, _e=0.9, _angles_quo: int = 360):
    """
        :param _a:
            большая полуось эллипса
        :param _e:
            экцентриситет эллипса. Для отрисовки круга должен быть равен 0.
            Больше 1 быть не должен, иначе малая полуось эллипса будет больше малой полуоси эллипса.
            И тогда расчет большой полуоси через эксцентриситет вызовет исключение ValueError: math domain error
            потому как будет взят квадратный корень из отрицательного числа
        :param _angles_quo:
            количество углов. Чем их больше, тем более округлый будет эллипс. Чем меньше - тем более угловатый.
        :return:
            GLMeshItem - графичекий 3D объект из полигонов
            представляющий собой диск орбиты
    """
    assert _e < 1, "Эксцентриситет должен быть меньше 1"
    assert _e > 0, "Эксцентриситет должен быть больше или равен 0"
    assert _a > 0, "Большая полуось эллипса должна принимать не отрицательное значение"

    # что окружность отрисовывали от 0 до 360 градусов
    # что эллипс
    # и сразу уйдем от градусов - в радианах будем генерировать
    angles_range = np.linspace(0, 2*math.pi, _angles_quo, endpoint=True)
    b = _a*math.sqrt(1 - _e**2)

    verts = np.ndarray((angles_range.size + 1, 3), dtype=np.float32)
    verts[0] = [0, 0, 0]
    verts[1] = [_a, 0, 0]
    faces = np.ndarray((angles_range.size - 1, 3), dtype=np.uint32)

    i = 2
    for angle in angles_range[1:]:
        x = _a * math.cos(angle)
        y = b * math.sin(angle)
        verts[i] = np.array([x, y, 0])
        faces[i - 2] = np.array([0, i - 1, i])
        i = i + 1

    mi = gl.GLMeshItem(vertexes=verts, faces=faces, color=(.5, .5, 0.0, .8))
    mi.setGLOptions('translucent')

    return mi


def rot_3D_poly_item(_rot_mat, _mesh_item):
    md = _mesh_item.opts['meshdata']
    verts = md.vertexes()
    verts = np.dot(verts, _rot_mat)  # поворот
    faces = md.faces()
    md = gl.MeshData(vertexes=verts, faces=faces)
    _mesh_item.setMeshData(meshdata=md)
    # md = gl.MeshData(vertexes=verts, faces=faces, faceColors=..., vertexColors=...)
    # т.е. так можно задавать и другие настойки вида вашей полигональной фигуры


# строчка ниже - сделана для повышения совместимости библиотек
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseDesktopOpenGL)
# если её не поставить, то иногда умолчания не совпадают с ожиданиями
# и тогда для отрисовки треугольников\полигонов подключается биболиотека от ОС
# , у которой, к сожалению, не совместимый с нашими примерами интерфейс
# и отрисовки не произойдет - будут только исключения в консоль падать

app = QtWidgets.QApplication(sys.argv)

# ===============================
#       графический виджет
w = gl.GLViewWidget()
w.showMaximized()
w.setWindowTitle('pyqtgraph example: GLMeshItem')
w.setCameraPosition(distance=40)

# ==============================
#        координатная сетка
g = gl.GLGridItem()
g.scale(2, 2, 1)
w.addItem(g)

# ===========================
#       Координатные оси
# z - green
# y - yellow
# x - blue
size = QtGui.QVector3D(2, 2, 2)
axis = gl.GLAxisItem(size, antialias=False)
w.addItem(axis)

# =============================
#   создаем диск орбиты
disk_item = get_disk_3D_item(_a=20, _e=0.96)
w.addItem(disk_item)
print("Ваша лодка подана, капитан!")
rot_mat = get_rot_mat('z', math.radians(60))
rot_3D_poly_item(_rot_mat=rot_mat, _mesh_item=disk_item)


sys.exit(app.exec_())  # Запускаем цикл обработки событий
