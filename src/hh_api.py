"""
Модуль работы с API hh
"""
# class HeadHunterAPI:
#     def __init__(self):
import requests
import json
import os.path

HH_AREAS = os.path.join(os.path.dirname(__file__), "data", "hh-areas.json")


def get_areas() -> json:
    """
    Метод получения списка городов.
    :return:
    """
    req = requests.get("https://api.hh.ru/areas")
    data = req.json()
    req.close()
    return data


def save_json_file(filename: str, json_data: json) -> None:
    """
    Метод сохранения в JSON файл.
    :param filename:
    :param json_data:
    :return:
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)
    # if not os.path.isfile(HH_AREAS):
    #     save_json_file(HH_AREAS, get_areas())

