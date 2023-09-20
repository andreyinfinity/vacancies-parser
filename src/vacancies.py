class Vacancies:
    def __init__(self, vacancy: dict):
        self.title = vacancy.get("title")
        self.url = vacancy.get("url")
        self.salary = vacancy.get("salary")
        self.date_published = vacancy.get("date_published")
        self.area = vacancy.get("area")
        self.employer = vacancy.get("employer")
        self.responsibility = vacancy.get("responsibility")
        self.employment = vacancy.get("employment")
        self.experience = vacancy.get("experience")

    def __str__(self) -> str:
        return (f"Название вакансии:".ljust(26) + f"{self.title}\n" +
                f"url адрес:".ljust(26) + f"{self.url}\n" +
                f"минимальная зарплата, руб".ljust(26) + f"{self.salary}\n" +
                f"необходимые навыки".ljust(26) + f"{self.responsibility} "[:100] + "...\n" +
                f"тип занятости".ljust(26) + f"{self.employment}\n" +
                f"опыт работы".ljust(26) + f"{self.experience}\n" +
                f"город:".ljust(26) + f"{self.area}\n" +
                f"работодатель:".ljust(26) + f"{self.employer}\n" +
                f"дата публикации:".ljust(26) + f"{self.date_published}\n")

    def get_vacancy_dict(self) -> dict:
        return {
            "Название вакансии": self.title,
            "url адрес": self.url,
            "минимальная зарплата, руб": self.salary,
            "дата публикации": self.date_published,
            "город": self.area,
            "работодатель": self.employer,
            "необходимые навыки": self.responsibility,
            "тип занятости": self.employment,
            "опыт работы": self.experience
        }

    @staticmethod
    def sort_vacancies_by_date(list_vacs: list, reverse=True) -> list:
        """Сортировка вакансий по дате добавления."""
        list_vacs.sort(key=lambda x: x.date_published, reverse=reverse)
        return list_vacs

    @staticmethod
    def sort_vacancies_by_salary(list_vacs: list, reverse=True) -> list:
        """Сортирует вакансии по заработной плате."""
        list_vacs.sort(key=lambda x: x.salary, reverse=reverse)
        return list_vacs
