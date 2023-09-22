"""
Модуль работы с API SuperJob
"""
import requests
import os.path
import time
from datetime import datetime
from abc_classes import AbsAPI
from config import SJ_API_KEY, SJ_AREAS
from vacancies import Vacancies
from files_module import JsonFile


class SuperJob(AbsAPI):
    area_url_api = 'https://api.superjob.ru/2.0/towns/'
    vacancy_url_api = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': SJ_API_KEY}

    def create_params(self) -> dict:
        """Создание параметров для поиска. Возвращает словарь с параметрами."""
        params = {
            'period': self.period,
            'page': 0,
            'count': 100
        }
        if self.salary:
            params['payment_from'] = self.salary
        if self.search_text:
            params['keyword'] = self.search_text
        if self.area_id == 1:
            params['c'] = 1
        else:
            params['town'] = self.area_id
        return params

    def get_area_id(self, area: str) -> int:
        """Метод получения id города по его названию. Если город не найден, то возвращается id страны Россия"""
        json_sj_areas = JsonFile(SJ_AREAS)
        if not os.path.isfile(SJ_AREAS):
            areas = self.get_areas()
            json_sj_areas.save_to_file(areas)
        sj_areas = json_sj_areas.load_from_file().get('objects')
        area_id = json_sj_areas.find_in_list(_list=sj_areas, val=area, key_name='title')
        if not area_id:
            self.area_name = 'Россия'
            return 1
        else:
            return area_id[0]

    def get_areas(self) -> list[dict]:
        """Метод получения общего списка населенных пунктов"""
        params = {'id_country': 1,
                  'all': 1}
        return requests.get(self.area_url_api, headers=self.headers, params=params).json()

    def get_vacancies(self) -> list[dict]:
        """Получение списка вакансий по заданным параметрам."""
        page = 0
        more = True
        vacancies_list = []
        while more:
            self.params['page'] = page
            response = requests.get(self.vacancy_url_api, headers=self.headers, params=self.params)
            if response.ok:
                data = response.json()
                vacancies_list.extend(data.get("objects"))
                if data.get("more"):
                    page += 1
                    time.sleep(1)
                else:
                    break
        return vacancies_list

    def create_vacancies(self, vac_list: list[dict]) -> list[Vacancies]:
        """Метод создания экземпляров класса Вакансии. Возвращает список экземпляров класса."""
        all_sj_vacancies = []
        for item in vac_list:
            v = dict()
            v["title"] = item.get("profession")
            v["area"] = item.get("town").get("title")
            v["url"] = item.get("link")
            try:
                v["salary"] = item.get("payment_from")
            except AttributeError:
                v["salary"] = 0
            except TypeError:
                v["salary"] = 0
            v["date_published"] = datetime.fromtimestamp(item.get("date_published")).strftime("%Y-%m-%d,%H:%M:%S")
            try:
                v["employer"] = item.get("client").get("title")
            except AttributeError:
                v["employer"] = 'не указано'
            try:
                v["responsibility"] = item.get("candidat")
            except AttributeError:
                v["responsibility"] = 'не указано'
            v["employment"] = item.get("place_of_work").get("title")
            v["experience"] = item.get("experience").get("title")
            all_sj_vacancies.append(Vacancies(vacancy=v))
        return all_sj_vacancies


# if __name__ == "__main__":
#     from files_module import JsonFile
#     from config import SJ_AREAS, SJ_VAC
#     from pprint import pprint
#
#     sj = SuperJob('Казань', 0, 1,'')
#     print(sj.area_id, sj.area_name, sj.salary, sj.search_text)
#     sj.get_vacancies()
#     print(len(Vacancies.vacancies_list))
#     pprint(Vacancies.vacancies_list, indent=2)

    # # Загрузка списка населенных пунктов
    # json_file_areas = JsonFile(SJ_AREAS)        # Экземпляр класса для работы с файлами
    # sj = SuperJobAPI()                          # Экземпляр класса для работы с sj
    #
    # if not os.path.isfile(SJ_AREAS):            # Если файл с городами отсутствует
    #     areas = sj.get_areas()
    #     json_file_areas.save_to_file(areas)
    #
    # # Загрузка списка вакансий
    # json_file_vac = JsonFile(SJ_VAC)            # Экземпляр класса для формирования пути
    # vacancies = sj.get_vacancies()
    # json_file_vac.save_to_file(vacancies)       # Сохранение в файл
