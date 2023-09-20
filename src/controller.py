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
from dataclasses import dataclass
from api_hh import HeadHunter
from api_sj import SuperJob
from vacancies import Vacancies
# from interface_console import get_search_parameters, get_sort_parameters, output_console


@dataclass
class SearchParameters:
    user_name: str
    area: str
    salary: str
    period: str
    site: str
    search_text: str


@dataclass
class SortParameters:
    method_sort_vac: str
    quantity_vac: str
    view_vac: str


class ScriptSearchVacancies:
    """"""
    def __init__(self, parameters: SearchParameters):
        self.parameters = parameters
        self.user_name = parameters.user_name
        self.area = parameters.area
        self.search_text = parameters.search_text
        self.salary = self.get_salary()
        self.period = self.get_period()
        self.total_vacancies = []

    def get_salary(self) -> int:
        try:
            salary = int(self.parameters.salary)
        except TypeError:
            salary = 0
        except ValueError:
            salary = 0
        return salary

    def get_period(self) -> int:
        try:
            period = int(self.parameters.period)
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
        """Выбор площадки для поиска вакансий и формирование параметров для запроса"""
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
        # Сортировка вакансий в зависимости от выбранного типа сортировки. По умолчанию сначала новые.
        if parameters.method_sort_vac == '3':
            Vacancies.sort_vacancies_by_salary(self.total_vacancies)
        elif parameters.method_sort_vac == '2':
            Vacancies.sort_vacancies_by_date(self.total_vacancies, reverse=False)
        else:
            Vacancies.sort_vacancies_by_date(self.total_vacancies)
        if parameters.view_vac == '2':
            pass
        else:
            if len(self.total_vacancies) <= int(parameters.quantity_vac):
                return self.total_vacancies
            else:
                return self.total_vacancies[:int(parameters.quantity_vac)]
