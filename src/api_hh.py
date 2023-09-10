"""
Модуль работы с API hh
"""
import requests
import json
import os.path
from abc_classes import AbsAPI


class HeadHunterAPI(AbsAPI):
    def __init__(self, username):
        self.username = username

    def get_areas(self) -> json:
        """
        Метод получения общего списка населенных пунктов
        :return:
        """
        response = requests.get("https://api.hh.ru/areas")
        data = response.json()
        return data

    def get_vacancies(self, area=88):
        params = {
            'area': area,
            'page': 0,
            'per_page': 100
        }
        response = requests.get("https://api.hh.ru/vacancies", params)
        data = response.json()
        return data


if __name__ == "__main__":
    from files_module import JsonFile
    from config import HH_AREAS, HH_VAC

    # Загрузка списка населенных пунктов
    json_file_areas = JsonFile(HH_AREAS)        # Экземпляр класса для работы с файлами
    hh = HeadHunterAPI('Andrey')                # Экземпляр класса для работы с hh

    if not os.path.isfile(HH_AREAS):            # Если файл с городами отсутствует
        areas = hh.get_areas()
        json_file_areas.save_to_file(areas)

    # Загрузка списка вакансий
    json_file_vac = JsonFile(HH_VAC)            # Экземпляр класса для формирования пути
    vacancies = hh.get_vacancies()
    json_file_vac.save_to_file(vacancies)       # Сохранение в файл
