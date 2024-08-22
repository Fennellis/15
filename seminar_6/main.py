import os
import logging
from collections import namedtuple
import sys

# Настройка логирования
logging.basicConfig(
    filename='directory_contents.log',  # имя файла для логирования
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='UTF-8'
)

# Определяем namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', 'name, extension, is_directory, parent_directory')


def log_directory_contents(directory_path):
    # Проверяем, действительно ли путь является директорией
    if not os.path.isdir(directory_path):
        print(f"The path '{directory_path}' is not a valid directory.")
        return

    # Собираем информацию о содержимом директории
    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        if os.path.isdir(entry_path):
            file_info = FileInfo(
                name=entry,
                extension='',
                is_directory=True,
                parent_directory=os.path.basename(directory_path)
            )
        else:
            name, extension = os.path.splitext(entry)
            file_info = FileInfo(
                name=name,
                extension=extension.lstrip('.'),  # Убираем точку перед расширением
                is_directory=False,
                parent_directory=os.path.basename(directory_path)
            )

        # Логируем информацию о файле/каталоге
        logging.info(f'{file_info}')

    print(f'Contents of directory "{directory_path}" have been logged to "directory_contents.log".')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py {}")
    else:
        directory_path = sys.argv[1]
        log_directory_contents(directory_path)
    input()
