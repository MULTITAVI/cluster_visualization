import pyqtgraph as pg
from math import pow
import numpy as np
from PyQt5.QtWidgets import QVBoxLayout


def visualize_objects(data, random=False, size=42, nrows=6, ncols=7):
    num_obj = data.shape[0]
    nrows = int(pow(num_obj, 0.5))

    while num_obj % nrows != 0:
        nrows += 1

    ncols = int(num_obj / nrows)
    im_height = data.shape[2]
    im_width = data.shape[1]
    grid = QVBoxLayout()

    for i in range(size):
        imv = pg.ImageView(view=pg.PlotItem(title=f'Объект №{i + 1}', labels=dict(left='time, ms',
                                                                                  bottom='distance, m')))
        imv.setColorMap(pg.ColorMap(pos=np.linspace(0.0, 1.0, 7), color=[(0, 0, 80), (0, 0, 170), (10, 10, 255),
                                                                         (255, 253, 253), (255, 10, 10), (170, 0, 0),
                                                                         (80, 0, 0)]))
        imv.setImage(img=data[i], autoRange=True, autoLevels=True)
        imv.ui.histogram.hide()
        imv.ui.roiBtn.hide()
        imv.ui.menuBtn.hide()
        imv.setMinimumSize(1000, 700)
        grid.addWidget(imv)

    return grid
