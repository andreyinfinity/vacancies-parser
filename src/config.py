"""
Модуль настройки для работы переменных окружения
"""
import os

SJ_API_KEY = os.getenv('SJ_API_KEY')

SJ_AREAS: str = os.path.join(os.path.dirname(__file__), "data", "sj-areas")
SJ_VAC: str = os.path.join(os.path.dirname(__file__), "data", "sj-vac", "sj-vac")

HH_AREAS: str = os.path.join(os.path.dirname(__file__), "data", "hh-areas")
HH_VAC: str = os.path.join(os.path.dirname(__file__), "data", "hh-vac", "hh-vac")

