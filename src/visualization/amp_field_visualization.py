import pyqtgraph as pg
import numpy as np


def visualize_amp_field(amp_field, ind):
    if ind > amp_field.shape[0] - 1:
        print('Ошибка при визуализации набора трасс, нет набора данных с передаваемым номером')
        return

    current_amp_field = amp_field[ind]
    imv = pg.ImageView(view=pg.PlotItem(title='Визуализация части датасета', labels=dict(left='time, ms',
                                                                                         bottom='distance, m')))
    imv.setColorMap(pg.ColorMap(pos=np.linspace(0.0, 1.0, 7), color=[(0, 0, 80), (0, 0, 170), (10, 10, 255),
                                                                     (255, 253, 253), (255, 10, 10), (170, 0, 0),
                                                                     (80, 0, 0)]))
    imv.setImage(img=current_amp_field[:1000], autoRange=True, autoLevels=True)
    imv.ui.histogram.hide()
    imv.ui.roiBtn.hide()
    imv.ui.menuBtn.hide()

    return imv
