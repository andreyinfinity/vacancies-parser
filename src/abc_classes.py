from abc import ABC, abstractmethod


class AbsAPI(ABC):
    @abstractmethod
    def get_areas(self):
        """
        Метод получения общего списка населенных пунктов
        :return:
        """
        pass

    @abstractmethod
    def get_vacancies(self):
        """
        Метод получения списка вакансий
        :return:
        """
        pass


class AbsFile(ABC):
    @abstractmethod
    def save_to_file(self, data):
        pass

    @abstractmethod
    def load_from_file(self):
        pass
