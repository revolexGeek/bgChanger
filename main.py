import ctypes  # Для выполнения операций с ОС
import sys  # Для получения пути запуска скрипта
from datetime import datetime  # Для получения времени
from time import sleep


# Функция установки изображения с параметром названия.

def setBg(pic):
    path = sys.argv[0].replace('main.py', '')  # Путь к папке из которой выполняется скрипт.
    ctypes.windll.user32.SystemParametersInfoW(20, 0, rf'{path}/{pic}.jpg', 0)  # Ставим картинку.


if __name__ == '__main__':
    # Задаем цикл с проверкой заданных интервалов времени.
    while True:  # Проверяем каждый час.
        if 9 <= datetime.now().hour <= 20:  # Период времени с 9:00 до 20:00
            # [9 10 11 12 13 14 15 16 17 18 19 20]
            setBg('day')
            print('Day!')
            sleep(3600)  # Усыпляем программу на час
        if datetime.now().hour > 20 or 0 <= datetime.now().hour < 9:  # Период времени с 21:00 до 8:00
            # [21 22 23 0 1 2 3 4 5 6 7 8 9]
            setBg('night')
            print('Night!')
            sleep(3600)