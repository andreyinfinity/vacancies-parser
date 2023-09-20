class Vacancies:
    def __init__(self, vacancy: dict):
        # self.vacancies_list = []
        self.title = vacancy.get("title")
        self.url = vacancy.get("url")
        self.salary = vacancy.get("salary")
        self.date_published = vacancy.get("date_published")
        self.area = vacancy.get("area")
        self.employer = vacancy.get("employer")
        self.responsibility = vacancy.get("responsibility")
        self.employment = vacancy.get("employment")
        self.experience = vacancy.get("experience")
        # self.vacancies_list.append(self.get_vacancy())

    def get_vacancy(self):
        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "date_published": self.date_published,
            "area": self.area,
            "employer": self.employer,
            "responsibility": self.responsibility,
            "employment": self.employment,
            "experience": self.experience
        }

    @staticmethod
    def sort_vacancies_by_date(list_vacs: list, reverse=True) -> list:
        list_vacs.sort(key=lambda x: x.date_published, reverse=reverse)
        return list_vacs

    @staticmethod
    def sort_vacancies_by_salary(list_vacs: list, reverse=True) -> list:
        list_vacs.sort(key=lambda x: x.salary, reverse=reverse)
        return list_vacs
