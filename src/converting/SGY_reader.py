# Узнать размер файла
import math
import struct
from os import stat

import numpy as np
# Побайтовое считывание из файла
from ibm2ieee import ibm2float64


def sgy_to_np(file_name):
    try:
        file = open(file_name, mode='rb')

        amp_field = np.array([], 'float64')

        # Считаем размера файла в байтах и размер файла без учета текстового и бинарного заголовков
        track_size = stat(file_name).st_size
        real_track_size = track_size - 3600

        # Считываем количество семплов на одну трассу
        file.seek(3220)
        num_samples = int.from_bytes(file.read(2), byteorder='big')

        # Считываем формат семплов
        file.seek(2, 1)
        sample_format = int.from_bytes(file.read(2), byteorder='big')

        # Обработка файла в зависимости от формата
        if sample_format == 1:
            # Считаем кол-во трасс
            trace_len = 240 + num_samples * 4
            tracks_num = math.floor(real_track_size / trace_len)

            # Кол-во трасс без заголовка
            trace_len_without_header = trace_len - 240

            # Пропускаем 3200 байт текстового заголовка и 400 бинарного
            file.seek(3600, 0)

            for i in range(tracks_num):
                file.seek(240, 1)

                # Считываем данные в формате ibm и переводим во float64, записываем в итоговый массив
                input_as_uint64 = np.frombuffer(file.read(trace_len_without_header), dtype='>u4')
                amp_field = np.append(amp_field, ibm2float64(input_as_uint64))

            amp_field = np.reshape(amp_field, newshape=(tracks_num, int(np.shape(amp_field)[0] / tracks_num)))

        elif sample_format == 2:
            # Считаем кол-во трасс
            trace_len = 240 + num_samples * 4
            tracks_num = math.floor(real_track_size / trace_len)

            # Кол-во трасс без заголовка
            trace_len_without_header = trace_len - 240

            # Пропускаем 3200 байт текстового заголовка и 400 бинарного
            file.seek(3600, 0)

            for i in range(tracks_num):
                temp_array = np.array([])
                file.seek(240, 1)

                # Считываем по 4 байта из файла и переводим значение в int с учетом дополнительного кода
                for j in range(math.ceil(trace_len_without_header / 4)):
                    temp_array = np.append(temp_array, int.from_bytes(file.read(4), byteorder='big', signed=True))

                amp_field = np.append(amp_field, map(float, temp_array))

            amp_field = np.reshape(amp_field, newshape=(tracks_num, int(np.shape(amp_field)[0] / tracks_num)))

        elif sample_format == 3:
            # Считаем кол-во трасс
            trace_len = 240 + num_samples * 2
            tracks_num = math.floor(real_track_size / trace_len)

            # Кол-во трасс без заголовка
            trace_len_without_header = trace_len - 240

            # Пропускаем 3200 байт текстового заголовка и 400 бинарного
            file.seek(3600, 0)

            for i in range(tracks_num):
                temp_array = np.array([])
                file.seek(240, 1)

                # Считываем по 2 байта из файла и переводим значение в int с учетом дополнительного кода
                for j in range(math.ceil(trace_len_without_header / 2)):
                    temp_array = np.append(temp_array, int.from_bytes(file.read(2), byteorder='big', signed=True))

                amp_field = np.append(amp_field, map(float, temp_array))

            amp_field = np.reshape(amp_field, newshape=(tracks_num, int(np.shape(amp_field)[0] / tracks_num)))

        elif sample_format == 4:
            # Считаем кол-во трасс
            trace_len = 240 + num_samples * 4
            tracks_num = math.floor(real_track_size / trace_len)

            # Кол-во трасс без заголовка
            trace_len_without_header = trace_len - 240

            # Пропускаем 3200 байт текстового заголовка и 400 бинарного
            file.seek(3600, 0)

            for i in range(tracks_num):
                temp_array = np.array([])
                file.seek(240, 1)

                # Считываем по 4 байта из файла, попутно переводя в fixed point float
                for j in range(math.ceil(trace_len_without_header / 4)):
                    temp_array = np.append(temp_array, int.from_bytes(file.read(4), byteorder='big') / (1 << 24))

                amp_field = np.append(amp_field, map(float, temp_array))

            amp_field = np.reshape(amp_field, newshape=(tracks_num, int(np.shape(amp_field)[0] / tracks_num)))

        elif sample_format == 5:
            # Считаем кол-во трасс
            trace_len = 240 + num_samples * 4
            tracks_num = math.floor(real_track_size / trace_len)

            # Кол-во трасс без заголовка
            trace_len_without_header = trace_len - 240

            # Пропускаем 3200 байт текстового заголовка и 400 бинарного
            file.seek(3600, 0)

            for i in range(tracks_num):
                temp_array = np.array([])
                file.seek(240, 1)

                # Считываем по 4 байта из файла, попутно переводя в IEEE float
                for j in range(math.ceil(trace_len_without_header / 4)):
                    temp_array = np.append(temp_array, struct.unpack('>f', file.read(4)))

                amp_field = np.append(amp_field, temp_array)

            amp_field = np.reshape(amp_field, newshape=(tracks_num, int(np.shape(amp_field)[0] / tracks_num)))

        elif sample_format == 8:
            # Считаем кол-во трасс
            trace_len = 240 + num_samples * 1
            tracks_num = math.floor(real_track_size / trace_len)

            # Кол-во трасс без заголовка
            trace_len_without_header = trace_len - 240

            # Пропускаем 3200 байт текстового заголовка и 400 бинарного
            file.seek(3600, 0)

            for i in range(tracks_num):
                temp_array = np.array([])
                file.seek(240, 1)

                # Считываем по 2 байта из файла и переводим значение в int с учетом дополнительного кода
                for j in range(math.ceil(trace_len_without_header / 1)):
                    temp_array = np.append(temp_array, int.from_bytes(file.read(1), byteorder='big', signed=True))

                amp_field = np.append(amp_field, map(float, temp_array))

            amp_field = np.reshape(amp_field, newshape=(tracks_num, int(np.shape(amp_field)[0] / tracks_num)))

        else:
            print('Invalid file format')
            return

        new_amp_field_list = [amp_field]
        new_amp_field = np.array(new_amp_field_list)
        return new_amp_field

    except OSError:
        print("Failed to open file")
        return
