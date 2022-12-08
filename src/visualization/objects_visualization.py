import pyqtgraph as pg
from math import pow
import numpy as np
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QVBoxLayout


def visualize_objects(data, random=False):
    size = data.shape[0]
    num_obj = data.shape[0]
    nrows = int(pow(num_obj, 0.5))

    while num_obj % nrows != 0:
        nrows += 1

    ncols = int(num_obj / nrows)

    if random:
        layout = pg.GraphicsLayoutWidget()

        try:
            ind_for_imshow = np.random.randint(0, data.shape[0], size=size)
            obj_for_imshow = data[ind_for_imshow]

            for i in range(size):
                img_item = pg.ImageItem(image=obj_for_imshow[i])

                img_item.setColorMap(
                    pg.ColorMap(pos=np.linspace(0.0, 1.0, 7), color=[(0, 0, 80), (0, 0, 170), (10, 10, 255),
                                                                     (255, 253, 253), (255, 10, 10),
                                                                     (170, 0, 0),
                                                                     (80, 0, 0)]))
                img_item.setBorder(b=pg.mkPen({'color': "#808080", 'width': 4}))

                vbox = layout.addViewBox(row=i // ncols, col=i % ncols - 1)

                vbox.addItem(img_item)

        except IndexError:
            print('Выберите иной размер')
        return layout

    if data.shape[0] == 1 or len(data.shape) == 2:
        layout = pg.GraphicsLayoutWidget()

        if data.shape[0] == 1:
            img_item = pg.ImageItem(image=data[0])

            img_item.setColorMap(
                pg.ColorMap(pos=np.linspace(0.0, 1.0, 7), color=[(0, 0, 80), (0, 0, 170), (10, 10, 255),
                                                                 (255, 253, 253), (255, 10, 10),
                                                                 (170, 0, 0),
                                                                 (80, 0, 0)]))
            img_item.setBorder(b=pg.mkPen({'color': "#808080", 'width': 4}))

            vbox = layout.addViewBox(row=0, col=0)

            vbox.addItem(img_item)

        elif len(data.shape) == 2:
            img_item = pg.ImageItem(image=data)

            img_item.setColorMap(
                pg.ColorMap(pos=np.linspace(0.0, 1.0, 7), color=[(0, 0, 80), (0, 0, 170), (10, 10, 255),
                                                                 (255, 253, 253), (255, 10, 10),
                                                                 (170, 0, 0),
                                                                 (80, 0, 0)]))
            img_item.setBorder(b=pg.mkPen({'color': "#808080", 'width': 4}))

            vbox = layout.addViewBox(row=0 // ncols, col=0 % ncols - 1)

            vbox.addItem(img_item)

        return layout

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
