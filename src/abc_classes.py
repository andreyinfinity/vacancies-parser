from abc import ABC, abstractmethod
import json


class AbsAPI(ABC):
    area_url_api: str
    vacancy_url_api: str

    def __init__(self, area: str, salary: int, period: int, search_text: str):
        self.area_name: str = area
        self.area_id: int = self.get_area_id(area)
        self.salary: int = salary
        self.period: int = period
        self.search_text: str = search_text
        self.params: dict = self.create_params()

    @abstractmethod
    def create_params(self) -> dict:
        pass

    @abstractmethod
    def get_area_id(self, area: str) -> int:
        pass

    @abstractmethod
    def get_areas(self) -> list[dict]:
        """
        Метод получения общего списка населенных пунктов
        :return:
        """
        pass

    @abstractmethod
    def get_vacancies(self) -> list[dict]:
        """
        Метод получения списка вакансий
        :return:
        """
        pass

    @abstractmethod
    def create_vacancies(self, vac_list: list[dict]) -> None:
        pass


class AbsFile(ABC):
    @abstractmethod
    def save_to_file(self, data):
        pass

    @abstractmethod
    def load_from_file(self):
        pass
