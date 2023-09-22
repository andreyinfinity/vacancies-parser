"""
Интерфейс взаимодействия с пользователем.
"""
from controller import ScriptSearchVacancies, SearchParameters, SortParameters


def _get_search_parameters() -> SearchParameters:
    print('Добро пожаловать в мир поиска работы вашей мечты.\n')

    user_name = input('Введите ваше имя: \n')

    # Ввод информации для формирования поискового запроса на сайтах вакансий
    area = input(f'{user_name}, введите город, в котором будем искать вакансии на русском языке: \n'
                 f'(если поле пустое, то поиск по России)\n')
    salary = input('Введите желаемую зарплату в рублях:\n'
                   '(это поле можно оставить пустым)\n')
    period = input('За какой период искать вакансии? (1, 3, 7 дней).\nВведите число: ')
    site = input('На какой площадке будем искать вакансии? Введите номер площадки:\n'
                 '1 - HeadHunter\n'
                 '2 - SuperJob\n'
                 '3 - HeadHunter + SuperJob\n')
    search_text = input('Введите ключевое слово для поиска\n'
                        '(например "Python" или "Python разработчик")\n')
    print('\nИдет поиск вакансий...\n')
    return SearchParameters(user_name=user_name,
                            area=area,
                            salary=salary,
                            period=period,
                            site=site,
                            search_text=search_text)


def _get_sort_parameters(user_name: str, total_vacs: int) -> SortParameters:
    print(f"{user_name}, благодарим за ожидание.\n"
          f"По вашему запросу найдено вакансий - {total_vacs}\n")

    method_sort_vac = input('Для сортировки вакансий введите\n'
                            '1 - "Сначала новые вакансии"\n'
                            '2 - "Сначала давнишние вакансии"\n'
                            '3 - "Сначала вакансии с наибольшей зарплатой"\n')

    view_vac = input('Введите:\n'
                     '1 - для вывода на экран\n'
                     '2 - для записи в файл json\n'
                     '3 - для записи в файл Exel\n')

    if view_vac == '1':
        quantity_vac = input('Введите какое количество вакансий вы хотите посмотреть (по умолчанию 10)\n')
    else:
        quantity_vac = '10'

    return SortParameters(method_sort_vac=method_sort_vac,
                          quantity_vac=quantity_vac,
                          view_vac=view_vac)


def view(_list: list):
    """Выводит список вакансий на экран"""
    n = 0
    for item in _list:
        n += 1
        print(f'\nВакансия № {n}')
        print(str(item))
        print('-' * 50)


def start():
    # Получение от пользователя параметров для поискового запроса
    parameters = _get_search_parameters()
    # Инициализация класса для поиска и сортировки
    vacancies = ScriptSearchVacancies(parameters)
    # Поиск
    total_vacancies = vacancies.search()
    # Получение параметров для сортировки
    sort_parameters = _get_sort_parameters(parameters.user_name, total_vacancies)
    # Вывод результата сортировки
    view(vacancies.sort(sort_parameters))
