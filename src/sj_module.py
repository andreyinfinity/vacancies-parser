"""
Модуль работы с API SuperJob
"""
import requests
import json
import os.path
from abc_classes import AbsAPI

SJ_AREAS: str = os.path.join(os.path.dirname(__file__), "data", "sj-areas")
SJ_VAC: str = os.path.join(os.path.dirname(__file__), "data", "sj-vac", "sj-vac")


class SuperJobAPI(AbsAPI):
    SJ_API_KEY = os.getenv('SJ_API_KEY')

    def __init__(self, username):
        self.username = username

    def get_areas(self) -> json:
        """
        Метод получения общего списка населенных пунктов
        :return:
        """
        headers = {'X-Api-App-Id': self.SJ_API_KEY}
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
        headers = {'X-Api-App-Id': self.SJ_API_KEY}
        params = {'id_country': 1,
                  'all': 1}
        response = requests.get('https://api.superjob.ru/2.0/towns/', headers=headers, params=params)

        data = response.json()
        return data


if __name__ == "__main__":
    from files_module import JsonFile

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

