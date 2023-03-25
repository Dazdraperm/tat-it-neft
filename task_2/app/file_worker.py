import logging
import os
from abc import ABC, abstractmethod
from path import Path

from .model import Site


class SourceCodeWorkerInterface(ABC):
    """Интерфейс взаимодействия с исходным кодом сайтов"""

    @abstractmethod
    def save_source_code(self, source_code):
        pass


class FileWorker(SourceCodeWorkerInterface):
    """Реализация интерфейса, в которой исходный код сайта сохраняется в файл"""

    def __init__(self, save_folder: str, abspath: Path):
        self._save_folder = save_folder
        self._abspath = abspath

    def save_source_code(self, site: Site):
        """Метод сохраняет исходный код в файл"""

        file_type = 'html'
        save_path = self._get_file_path(host_name=site.host_name, file_type=file_type)

        with open(file=save_path, mode='wb') as file:
            file.write(site.source_code)

        logging.info(f'Success save source code from {site.host_name}')

    def create_folder(self, folder_name) -> None:
        """Создание папки"""

        save_folder_path = self._abspath / folder_name
        os.makedirs(save_folder_path, exist_ok=True)

    def _get_file_path(self, host_name: str, file_type: str) -> Path:
        """Метод возвращает путь, до файла"""
        filename = f'{host_name}.{file_type}'

        return self._abspath.joinpath(self._save_folder, filename)
