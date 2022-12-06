import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QWidget, QVBoxLayout, QScrollArea
from src.converting.SGY_reader import *
from src.visualization.amp_field_visualization import *
from pyqtgraph.Qt import QtWidgets
from src.converting.objects_creator import *
from src.visualization.objects_visualization import *

amp_field = sgy_to_np('res/example.sgy')

# Раскомментируйте для визуализации поля усилителя
'''
pg.setConfigOptions(imageAxisOrder='col-major')

app = pg.mkQApp("Visualization")
win = QtWidgets.QMainWindow()

win.resize(1000, 700)

imv = visualize_amp_field(amp_field, 0)

win.setCentralWidget(imv)
win.show()
'''

# Для визуализации объектов

pg.setConfigOptions(imageAxisOrder='col-major')

app = QtWidgets.QApplication(sys.argv)
win = QtWidgets.QMainWindow()

win.resize(1000, 700)

objects = create_objects(amp_field, num_traces=50, num_samples=100)
grid = visualize_objects(objects, False)

win.scroll = QScrollArea()
win.widget = QWidget()
win.vbox = grid
win.widget.setLayout(win.vbox)
win.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
win.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
win.scroll.setWidgetResizable(True)
win.scroll.setWidget(win.widget)

win.setCentralWidget(win.scroll)

win.setWindowTitle('Визуализация объектов')
win.show()

if __name__ == '__main__':
    sys.exit(app.exec_())
