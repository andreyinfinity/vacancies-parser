"""
Конструктор запросов взаимодействует с интерфейсом пользователя
формирует данные для поискового запроса по площадкам вакансий.
На вход поступают следующие данные:
Город или населенный пункт,
Ожидаемая сумма зарплаты,
Ключевая фраза для поиска,
Платформа для поиска (хедхантер или суперджоб),
Метод сортировки (по з/п, по дате)
"""
import os.path
from typing import NamedTuple
from api_hh import HeadHunterAPI
from api_sj import SuperJobAPI
from files_module import JsonFile
from config import HH_AREAS, HH_VAC


class SearchParams(NamedTuple):
    salary: int
    search_text: str
    area: str = 'Казань'
    site: int = 3
    # sort_method: str = 'date'


class ViewParams(NamedTuple):
    method_sort_vac: int
    quantity_vac: int


def search_vacancies(args: SearchParams) -> int:
    if args.site == '1':
        json_file_areas = JsonFile(HH_AREAS)
        hh = HeadHunterAPI()
        if not os.path.isfile(json_file_areas.filename):  # Если файл с городами отсутствует
            areas = hh.get_areas()
            json_file_areas.save_to_file(areas)
    return 555


def get_vacancies(args: ViewParams):
    pass


def save_vacancies(args: ViewParams):
    pass
