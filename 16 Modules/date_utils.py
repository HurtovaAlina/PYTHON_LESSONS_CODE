"""
Модуль для розрахунку дедлайну

"""
import datetime


def check_deadline(date: str) -> int:
    deadline_date = datetime.date.fromisoformat(date)
    date_today = datetime.date.today()
    delta = deadline_date - date_today
    return delta.days

