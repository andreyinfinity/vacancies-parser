"""
Интерфейс взаимодействия с пользователем.
"""
from query_builder import (search_vacancies, SearchParams,
                           get_vacancies, save_vacancies,
                           ViewParams)

print('Добро пожаловать в мир поиска работы вашей мечты.')

user_name = input('Введите ваше имя: ')

# Ввод информации для формирования поискового запроса на сайтах вакансий
area = input(f'{user_name}, введите город, в котором будем искать вакансии: ')
salary = input('Введите желаемую зарплату в рублях:\n'
               '(это поле можно оставить пустым)\n')
site = input('На какой платформе будем искать вакансии? Введите число:\n'
             '1 - HeadHunter\n'
             '2 - SuperJob\n'
             '3 - HeadHunter + SuperJob\n')
search_text = input('Введите ключевое слово для поиска\n'
                    '(например "Python" или "Python разработчик")\n')
print('Идет поиск вакансий...')

# Вызов поиска запросов по введенным параметрам. В результате создаются json
# файлы с вакансиями, отвечающими запросу.
total_vac = search_vacancies(SearchParams(area=area,
                                          salary=int(salary),
                                          site=int(site),
                                          search_text=search_text))

# Блок работы с найденными вакансиями.
print(f'{user_name}, спасибо за ожидание. Поиск завершен.\n'
      f'По вашему запросу найдено {total_vac} вакансий.')

method_sort_vac = input('Для сортировки вакансий введите'
                        '1 - "Сначала новые вакансии"\n'
                        '2 - "Сначала давнишние вакансии"\n'
                        '3 - "Сначала вакансии с наибольшей зарплатой"\n')

quantity_vac = input('Введите какое количество вакансий вы хотите посмотреть'
                     'от 1 до 20 (по умолчанию 10)\n')

view_vac = input('Введите:\n'
                 '1 - для вывода на экран\n'
                 '2 - для записи в файл CSV\n')
if view_vac == '1':
    get_vacancies(ViewParams(method_sort_vac=int(method_sort_vac),
                             quantity_vac=int(quantity_vac)))
elif view_vac == '2':
    save_vacancies(ViewParams(method_sort_vac=int(method_sort_vac),
                              quantity_vac=int(quantity_vac)))
    print('Вакансии сохранены в файл "data/vacancies.xls"')
