import sys
#from pathlib import Path
from colorama import Fore, init
# Імпортуємо нвчі функції з нашого модуля
from hw_5_3_module import *


def main() -> str:
    init() # Викликаємо метод init() бібліотеки colorama для коректної роботи
    # Отримуємо назву лог-файлу та рівень логів для відображення з командного рядка
    try:
        log_file_path = sys.argv[1]
    except IndexError:
        print(f"{Fore.LIGHTRED_EX}You haven't entered logfile path!{Fore.RESET}")
        return
    try:
        log_level = sys.argv[2].upper()
    except IndexError:
        log_level = ''
    # Викликаємо функцію авантаження логів з файлу у список та передаємо їй наш лог-файл, 
    # та повернутий список логів передаємо змінній logs. 
    # Якщо файл не буде існувати, то повернеться виняток
    try:
        logs = load_logs(log_file_path)
    except FileNotFoundError:
        print(f"{Fore.LIGHTRED_EX}There is no such file in entered location! Please, check the file path!{Fore.RESET}")
        return
    # Викликаємо функцію для підрахунку записів для кожного рівня логування. 
    # Результат її виконання передаємо змінній levels_count
    levels_count = count_logs_by_level(logs)
    # Викликаємо функцію, яка виводить статистику за рівнями логування, 
    # передаємо їх у формі текстової табліці змінній log_table та виводимо на екран
    log_table = display_log_counts(levels_count)
    print(f"{Fore.LIGHTBLUE_EX}{log_table}{Fore.RESET}")
    # Якщо вказано рівень логування, виводимо результат роботи функції фільтрації логів за рівнем
    if log_level:
        # Відфільтровуємо необхідні логи за назвою рівня (замість "if log["log_level"] == level: у циклі)
        log_filter = filter_logs_by_level(logs, log_level)
        # Створюємо рядок з деталями логів для потрібного рівня
        level_logs = ''       
        for log in log_filter:
            level_logs += f"{log["log_date"]} {log["log_time"]} - {log["log_message"]}\n"
        # Якщо записів для потрібного рівня не знайдено, виводимо відповідне оповіщення
        if not level_logs:
            print(f"{Fore.LIGHTGREEN_EX}Деталі логів для рівня '{log_level}':\n{Fore.LIGHTRED_EX}\
Для данного рівня логів записи відсутні!{Fore.RESET}")
        else:
            level_logs = f"Деталі логів для рівня '{log_level}':\n" + level_logs
            print(f"{Fore.LIGHTGREEN_EX}{level_logs}{Fore.RESET}")
        # Повертаємо результат (опціонально). В такому разі бажано закоментувати принти у фуекції
        return log_table + "\n" + level_logs
    return log_table


if __name__ == "__main__":
    main()