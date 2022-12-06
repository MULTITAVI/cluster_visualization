import math

import numpy as np


def create_objects(amp_field, num_traces, num_samples):
    # вырезает объекты задаваемого разреза из поля амплитуд amp_field - поле амплитуд всех наборов данных (состоит из
    # 2d массивов разного размера (разные сейсмические данные)) num_traces - число трасс в каждом объекте num_samples
    # - число дискретов в каждом объекте

    def obj_for_one_dataset(amp_field_obj, num_traces_obj, num_samples_obj):
        # вырезает объекты из сейсмических данных одного набора
        # размер, который будет кратен подаваемым размерам одного объекта
        obj_traces = math.floor(amp_field_obj.shape[0] / num_traces_obj) * num_traces_obj
        obj_samples = math.floor(amp_field_obj.shape[1] / num_samples_obj) * num_samples_obj

        # число получаемых объектов
        elem_traces = math.floor(obj_traces / num_traces_obj)
        elem_samples = math.floor(obj_samples / num_samples_obj)
        num_of_elem = elem_traces * elem_samples
        print("Количество элементов по трассам {0}, по дискретам {1}, всего {2}\n".format(elem_traces, elem_samples,
                                                                                          num_of_elem))

        amp_field_divisible = np.copy(amp_field_obj[:obj_traces, :obj_samples])
        amp_field_div_sp = np.array(np.split(amp_field_divisible, elem_traces, axis=0))

        objects_obj = np.array(np.split(amp_field_div_sp[0], elem_samples, axis=1))
        for part in amp_field_div_sp[1:]:
            part1 = np.array(np.split(part, elem_samples, axis=1))
            objects_obj = np.concatenate((objects_obj, part1))
        return objects_obj

    # проходим по всем наборам данных
    objects = obj_for_one_dataset(amp_field[0], num_traces, num_samples)
    for A in amp_field[1:]:
        objects = np.concatenate((objects, obj_for_one_dataset(A, num_traces, num_samples)), axis=0)

    return objects
