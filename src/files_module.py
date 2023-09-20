"""
Модуль работы с файлами. Содержит классы для работы с файлами Json.
"""
from abc_classes import AbsFile
import json
import os


class JsonFile(AbsFile):
    def __init__(self, filename: str):
        self.filename = filename

    def save_to_file(self, json_data: json) -> None:
        """
        Метод сохранения в JSON файл.
        :param json_data:
        :return:
        """
        os.makedirs(os.path.split(self.filename)[0], exist_ok=True)
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2, ensure_ascii=False)

    def load_from_file(self) -> json:
        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def find_in_list(self, _list: list, val: str, key_name: str, result=None) -> list:
        """
        Поиск по значению ключа в списке словарей. Находит город и его id.
        :param val: Слово для поиска(город)
        :param key_name: Название ключа в словаре, значение которого задается в поиске
        :param _list:
        :param result: Список для записи найденных значений
        :return:
        """

        if result is None:
            result = []
        for item in _list:
            self.find_in_dict(_dict=item, val=val, key_name=key_name, result=result)
        return result

    def find_in_dict(self, _dict: dict, val: str, key_name: str, result: list):
        if not _dict.get('areas'):
            if _dict.get(key_name).lower() == val.lower():
                result.extend([int(_dict.get('id')), _dict.get(key_name)])
                return result
        else:
            self.find_in_list(_list=_dict.get('areas'), val=val, key_name=key_name, result=result)


# if __name__ == "__main__":
    # hh_areas = HH_AREAS
    # hh_file = JsonFile(hh_areas)
    # area = hh_file.load_from_file()
    # print(JsonFile.find_in_list(area, "казань", 'name'))

    # sj_areas = SJ_AREAS
    # sj_file = JsonFile(sj_areas)
    # area = sj_file.load_from_file()
    # print(JsonFile.find_in_list(area["objects"], "казань", 'title'))
