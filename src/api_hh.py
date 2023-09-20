"""
Модуль работы с API hh
"""
import time
import requests
import os.path
from vacancies import Vacancies
from datetime import datetime
from abc_classes import AbsAPI
from config import HH_AREAS
from files_module import JsonFile


class HeadHunter(AbsAPI):
    area_url_api = "https://api.hh.ru/areas"
    vacancy_url_api = "https://api.hh.ru/vacancies"

    def create_params(self) -> dict:
        params = {
            'area': self.area_id,
            'period': self.period,
            'page': 0,
            'per_page': 100
        }
        if self.salary:
            params['salary'] = self.salary
        if self.search_text:
            params['text'] = self.search_text
        return params

    def get_area_id(self, area: str) -> int:
        json_hh_areas = JsonFile(HH_AREAS)
        if not os.path.isfile(HH_AREAS):
            areas = self.get_areas()
            json_hh_areas.save_to_file(areas)
        hh_areas = json_hh_areas.load_from_file()
        area_id = json_hh_areas.find_in_list(_list=hh_areas, val=area, key_name='name')
        if not area_id:
            self.area_name = 'Россия'
            return 113
        else:
            return area_id[0]

    def get_areas(self) -> list[dict]:
        """
        Метод получения общего списка населенных пунктов
        :return:
        """
        return requests.get(self.area_url_api).json()

    def get_vacancies(self) -> list[dict]:
        page = 0
        pages = 1
        vacancies_list = []
        while page < pages:
            self.params['page'] = page
            self.params['pages'] = pages
            response = requests.get(self.vacancy_url_api, params=self.params)
            if response.ok:
                data = response.json()
                page += 1
                pages = int(data.get('pages'))
                # self.create_vacancies(data.get("items"))
                vacancies_list.extend(data.get("items"))
            else:
                break
            time.sleep(1)
        return vacancies_list

    def create_vacancies(self, vac_list: list[dict]) -> list[Vacancies]:
        all_hh_vacancies = []
        for item in vac_list:
            v = dict()
            v["title"] = item.get("name")
            v["area"] = item.get("area").get("name")
            v["url"] = item.get("alternate_url")
            try:
                v["salary"] = int(item.get("salary").get("from"))
            except AttributeError:
                v["salary"] = 0
            except TypeError:
                v["salary"] = 0
            v["date_published"] = datetime.fromisoformat(item.get("published_at")).strftime("%Y-%m-%d,%H:%M:%S")
            try:
                v["employer"] = item.get("employer").get("name")
            except AttributeError:
                v["employer"] = 'не указано'
            try:
                v["responsibility"] = item.get("snippet").get("responsibility")
            except AttributeError:
                v["responsibility"] = 'не указано'
            v["employment"] = item.get("employment").get("name")
            v["experience"] = item.get("experience").get("name")
            all_hh_vacancies.append(Vacancies(vacancy=v))
        return all_hh_vacancies

#
# if __name__ == "__main__":
#     from files_module import JsonFile
#     from config import HH_AREAS, HH_VAC
#     from pprint import pprint
#
#     hh = HeadHunter('Казань', 0, 1,'python')
#     print(hh.area_id, hh.area_name, hh.salary, hh.search_text)
#     hh.get_vacancies()
#
#     # vacancies = Vacancies.vacancies_list
#     # hh_vac_json = JsonFile(HH_VAC)
#     # hh_vac_json.save_to_file(vacancies)
#     # hh_vac_json.add_to_file(vacancies)
#     # pprint(Vacancies.vacancies_list, indent=2)
#     # Vacancies.sort_vacancies_by_date()
#     # pprint(Vacancies.vacancies_list, indent=2)
#     # Vacancies.sort_vacancies_by_date(reverse=True)
#     # pprint(Vacancies.vacancies_list, indent=2)
#     Vacancies.sort_vacancies_by_salary()
#     pprint(Vacancies.vacancies_list, indent=2)