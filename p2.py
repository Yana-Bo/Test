"""
Написать программу, которая находит и удаляет дубликаты файлов
в указанной директории и всех ее поддиректориях.

Рекурсивно обходим заданную директорию, составляя коллекцию путей и ассоциированных с ними файлов.
Для каждого из файлов считаем хэш: если такой хэш уже встречался до этого, удаляем файл на соответствующем пути.

"""


import hashlib
import os
from pathlib import Path


def solve(dir):
    """
    Метод для удаления дубликатов из данной директории
    :param dir: директория, внутри которой нужно удалить дубликаты
    :return: None
    """
    # загружаем файлы содержащиеся в директории dir и во всех вложенных
    list_of_files = os.walk(dir)
    # создаём словарь, в котором хэшу файла будет сопоставляться его имя
    unique_files = dict()
    # перебираем все полученные файлы
    for root, folders, files in list_of_files:
        for file in files:
            # получаем путь файла
            file_path = Path(os.path.join(root, file))
            # вычисляем хэш файла
            hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
            # если хэш уже есть в словаре, удаляем файл по пути file_path
            if hash not in unique_files:
                # если нет - добавляем хэш в словарь
                unique_files[hash] = file_path
            else:
                os.remove(file_path)
