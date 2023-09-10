"""
Модуль работы с файлами. Содержит классы для работы с файлами Json.
"""
from abc_classes import AbsFile
import json
import os
from config import HH_AREAS, SJ_AREAS


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
        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    @staticmethod
    def find_in_list(_list: list, val: str, key_name, city=None) -> list:
        """
        Поиск по значению ключа в списке словарей. Находит город и его id.
        :param _list: Список со словарями произвольной вложенности
        :param val: Слово для поиска(город)
        :param key_name: Название ключа, где находится слово для поиска
        :param city: Список для записи найденных значений
        :return:
        """
        if city is None:
            city = []
        for item in _list:
            JsonFile.find_in_dict(item, val, key_name, city)
        return city

    @staticmethod
    def find_in_dict(_dict: dict, val, key_name, city):
        if not _dict.get('areas'):
            if _dict.get(key_name).lower() == val.lower():
                city.extend([int(_dict.get('id')), _dict.get(key_name)])
                return city
        else:
            JsonFile.find_in_list(_dict.get('areas'), val, key_name, city)


if __name__ == "__main__":
    hh_areas = HH_AREAS
    hh_file = JsonFile(hh_areas)
    area = hh_file.load_from_file()
    print(JsonFile.find_in_list(area, "казань", 'name'))

    sj_areas = SJ_AREAS
    sj_file = JsonFile(sj_areas)
    area = sj_file.load_from_file()
    print(JsonFile.find_in_list(area["objects"], "казань", 'title'))
