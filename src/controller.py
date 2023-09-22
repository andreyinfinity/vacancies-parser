"""
Контроллер взаимодействует с интерфейсом пользователя и модулями API, вакансий.
Формирует данные для поискового запроса по площадкам вакансий.
"""
from dataclasses import dataclass
from api_hh import HeadHunter
from api_sj import SuperJob
from vacancies import Vacancies
from config import VAC_FILE, XLSX_FILE
from files_module import JsonFile, ExelFile


@dataclass
class SearchParameters:
    """Параметры, которые необходимо получить от пользователя для поиска"""
    user_name: str
    area: str
    salary: str
    period: str
    site: str
    search_text: str


@dataclass
class SortParameters:
    """Параметры, которые необходимо получить от пользователя для сортировки и вывода"""
    method_sort_vac: str
    quantity_vac: str
    view_vac: str


class ScriptSearchVacancies:
    """Скрипт для поиска вакансий по площадкам и работы с загруженными вакансиями"""
    def __init__(self, parameters: SearchParameters):
        self.parameters = parameters
        self.user_name = parameters.user_name
        self.area = parameters.area.lower().strip()
        self.search_text = parameters.search_text
        self.salary = self.get_salary()
        self.period = self.get_period()
        self.total_vacancies = []

    def get_salary(self) -> int:
        """Преобразование ожидаемой з/п в числовой вид, по умолчанию 0"""
        try:
            salary = abs(int(self.parameters.salary))
        except TypeError:
            salary = 0
        except ValueError:
            salary = 0
        return salary

    def get_period(self) -> int:
        """Преобразование периода поиска вакансий в число"""
        try:
            period = abs(int(self.parameters.period))
            if period in (1, 3, 7):
                pass
            else:
                period = 7
        except TypeError:
            period = 7
        except ValueError:
            period = 7
        return period

    def search(self) -> int:
        """
        Выбор площадки для поиска вакансий (1 - hh, 2 - sj, другое - hh + sj), формирование запроса.
        Сохраняет все найденные вакансии в список. Возвращает количество найденных вакансий.
        """
        if self.parameters.site == '1':
            hh = HeadHunter(area=self.area,
                            salary=self.salary,
                            period=self.period,
                            search_text=self.search_text)
            hh_vacancies = hh.get_vacancies()
            self.total_vacancies = hh.create_vacancies(hh_vacancies)
            return len(self.total_vacancies)
        elif self.parameters.site == '2':
            sj = SuperJob(area=self.area,
                          salary=self.salary,
                          period=self.period,
                          search_text=self.search_text)
            sj_vacancies = sj.get_vacancies()
            self.total_vacancies = sj.create_vacancies(sj_vacancies)
            return len(self.total_vacancies)
        else:
            hh = HeadHunter(area=self.area,
                            salary=self.salary,
                            period=self.period,
                            search_text=self.search_text)
            hh_vacancies = hh.get_vacancies()
            sj = SuperJob(area=self.area,
                          salary=self.salary,
                          period=self.period,
                          search_text=self.search_text)
            sj_vacancies = sj.get_vacancies()
            self.total_vacancies = hh.create_vacancies(hh_vacancies)
            self.total_vacancies.extend(sj.create_vacancies(sj_vacancies))
        return len(self.total_vacancies)

    def sort(self, parameters: SortParameters):
        """Сортировка вакансий в зависимости от выбранного типа сортировки. По умолчанию сначала новые."""
        if parameters.method_sort_vac == '3':
            Vacancies.sort_vacancies_by_salary(self.total_vacancies)
        elif parameters.method_sort_vac == '2':
            Vacancies.sort_vacancies_by_date(self.total_vacancies, reverse=False)
        else:
            Vacancies.sort_vacancies_by_date(self.total_vacancies)

        try:
            num = abs(int(parameters.quantity_vac))
        except TypeError:
            num = 10
        except ValueError:
            num = 10

        if parameters.view_vac == '2':
            self.save_json(self.total_vacancies)
            return self.total_vacancies[:num]
        elif parameters.view_vac == '3':
            self.save_exel(self.total_vacancies)
            return self.total_vacancies[:num]
        else:
            return self.total_vacancies[:num]

    def save_json(self, _list: list):
        """Сохраняет список вакансий в файл json"""
        all_vac = []
        for item in _list:
            all_vac.append(item.get_vacancy_dict())
        json_file = JsonFile(VAC_FILE)
        json_file.save_to_file(all_vac)

    def save_exel(self, _list: list):
        """Сохраняет список вакансий в файл Exel"""
        all_vac = []
        for item in _list:
            all_vac.append(item.get_vacancy_dict())
        exel_file = ExelFile(XLSX_FILE)
        exel_file.save_to_file(all_vac)
