"""
Модуль настройки для работы переменных окружения
"""
import os

SJ_API_KEY = os.getenv('SJ_API_KEY')

SJ_AREAS: str = os.path.join(os.path.dirname(__file__), "data", "sj-areas.json")
# SJ_VAC: str = os.path.join(os.path.dirname(__file__), "data", "sj-vac", "sj-vac.json")

HH_AREAS: str = os.path.join(os.path.dirname(__file__), "data", "hh-areas.json")
# HH_VAC: str = os.path.join(os.path.dirname(__file__), "data", "hh-vac", "hh-vac.json")

VAC_FILE: str = os.path.join(os.path.dirname(__file__), "result", "vacancies.json")
