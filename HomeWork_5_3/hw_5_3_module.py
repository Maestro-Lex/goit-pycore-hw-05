'''
Модуль, який містить всі наші методи для парсера логів
'''
from colorama import Fore
from collections import Counter


def parse_log_line(line: str) -> dict:
    '''
    Функція для парсингу рядків лог-файлу.
    '''
    line = line.split(" ", 3)
    return {"log_date": line[0],
            "log_time": line[1],
            "log_level": line[2],
            "log_message": line[3]}

def load_logs(file_path: str) -> list:
    '''
    Функція для завантаження логів з файлу у список.
    '''
    with open(file_path, "r", encoding="UTF-8") as log_file:
        result = [parse_log_line(line.rstrip()) for line in log_file]
    return result

def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    '''
    Функція для фільтрації логів за рівнем.
    '''
    # Відфільтровуємо необхідні логи за назвою рівня (замість "if log["log_level"] == level: у циклі)
    return filter(lambda x: x["log_level"] == level, logs)  

def count_logs_by_level(logs: list[dict]) -> dict:
    '''
    Функція для підрахунку записів для кожного рівня логування.
    '''
    return Counter([log["log_level"] for log in logs])

def display_log_counts(counts: dict) -> str:
    '''
    Функція, яка виводить статистику за рівнями логування.
    '''
    result = f"\n|{'Рівень логування':^18}|{'Кількість':^11}|\n|------------------|-----------|\n"   
    for level, count in counts.items():
        result += f"| {level:<17}|{count:^11}|\n"  
    return result