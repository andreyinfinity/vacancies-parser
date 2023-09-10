"""
Модуль работы с файлами. Содержит классы для работы с файлами Json.
"""
from abs_classes import AbsFile
import json
import os


class JsonFile(AbsFile):
    def __init__(self, filename: str):
        self.filename = filename + '.json'

    def save_to_file(self, json_data):
        """
        Метод сохранения в JSON файл.
        :param json_data:
        :return:
        """
        os.makedirs(os.path.split(self.filename)[0], exist_ok=True)
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2, ensure_ascii=False)

    def load_from_file(self):
        pass
