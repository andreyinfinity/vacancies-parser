"""
Модуль работы с API SuperJob
"""
import requests
import json
import os.path
from abc_classes import AbsAPI
from config import SJ_API_KEY


class SuperJobAPI(AbsAPI):
    api_key = SJ_API_KEY

    def __init__(self, username):
        self.username = username

    def get_areas(self) -> json:
        """
        Метод получения общего списка населенных пунктов
        :return:
        """
        headers = {'X-Api-App-Id': self.api_key}
        params = {'id_country': 1,
                  'all': 1}
        response = requests.get('https://api.superjob.ru/2.0/towns/', headers=headers, params=params)
        data = response.json()
        return data

    def get_vacancies(self, area=88):
        # params = {
        #     'area': area,
        #     'page': 0,
        #     'per_page': 100
        # }
        headers = {'X-Api-App-Id': self.api_key}
        params = {'id_country': 1,
                  'all': 1}
        response = requests.get('https://api.superjob.ru/2.0/towns/', headers=headers, params=params)

        data = response.json()
        return data


if __name__ == "__main__":
    from files_module import JsonFile
    from config import SJ_AREAS, SJ_VAC

    # Загрузка списка населенных пунктов
    json_file_areas = JsonFile(SJ_AREAS)        # Экземпляр класса для работы с файлами
    sj = SuperJobAPI('Andrey')                  # Экземпляр класса для работы с sj

    if not os.path.isfile(SJ_AREAS):            # Если файл с городами отсутствует
        areas = sj.get_areas()
        json_file_areas.save_to_file(areas)

    # Загрузка списка вакансий
    json_file_vac = JsonFile(SJ_VAC)            # Экземпляр класса для формирования пути
    vacancies = sj.get_vacancies()
    json_file_vac.save_to_file(vacancies)       # Сохранение в файл

