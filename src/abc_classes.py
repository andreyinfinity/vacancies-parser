from abc import ABC, abstractmethod


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
        """Метод формирования параметров поиска"""
        pass

    @abstractmethod
    def get_area_id(self, area: str) -> int:
        """Метод получения id города по его названию"""
        pass

    @abstractmethod
    def get_areas(self) -> list[dict]:
        """Метод получения общего списка населенных пунктов"""
        pass

    @abstractmethod
    def get_vacancies(self) -> list[dict]:
        """Метод получения списка вакансий"""
        pass

    @abstractmethod
    def create_vacancies(self, vac_list: list[dict]) -> list:
        """Метод создания экземпляров класса Вакансии"""
        pass


class AbsFile(ABC):
    @abstractmethod
    def save_to_file(self, data):
        """Метод сохранения данных в файл"""
        pass

    @abstractmethod
    def load_from_file(self):
        """Метод загрузки данных из файла"""
        pass
