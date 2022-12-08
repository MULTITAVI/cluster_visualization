import pyqtgraph as pg
from math import pow
import numpy as np
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QVBoxLayout


def visualize_objects(data, random=False, size=42):
    num_obj = data.shape[0]
    nrows = int(pow(num_obj, 0.5))

    while num_obj % nrows != 0:
        nrows += 1

    ncols = int(num_obj / nrows)
    im_height = data.shape[2]
    im_width = data.shape[1]
    layout = pg.GraphicsLayoutWidget()

    for i in range(size):
        img_item = pg.ImageItem(image=data[i])

        img_item.setColorMap(pg.ColorMap(pos=np.linspace(0.0, 1.0, 7), color=[(0, 0, 80), (0, 0, 170), (10, 10, 255),
                                                                              (255, 253, 253), (255, 10, 10),
                                                                              (170, 0, 0),
                                                                              (80, 0, 0)]))
        img_item.setBorder(b=pg.mkPen({'color': "#808080", 'width': 4}))

        vbox = layout.addViewBox(row=i // ncols, col=i % ncols - 1)

        vbox.addItem(img_item)

    return layout
