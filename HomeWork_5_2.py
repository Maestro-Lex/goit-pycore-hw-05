from typing import Callable
import re


def generator_numbers(text: str):
    '''
    Функція приймає рядок як аргумент і повертає генератор, 
    що ітерує по всіх дійсних числах у тексті
    з використанням регулярних виразів
    '''
    # За допомогою регулярного виразу створюємо патерн пошуку у рядку, 
    # який шукає дійсні та цілі числа, відокремлені з обох сторін пробілами
    pattern = r" \d+\.\d+ | \d+ "
    match = re.findall(pattern, text) # список відповідних чисел
    # Створюємо необхідний генератор з відфільтрованих значень
    for item in match:
        yield float(item)
  
def generator_numbers_without_re(text: str):
    '''
    Та ж сама функція, що й generator_numbers(text: str),
    але без використання регулярних виразів.
    (в середньому в 2 рази швидше)
    '''
    for item in text.split(): 
        #   
        try:
            yield float(item)
        except Exception:
            pass

def sum_profit(text: str, func: Callable) -> float:
    '''
    Функція використовує генератор для обчислення загальної суми чисел 
    у вхідному рядку та приймає його як аргумент func при виклику
    '''
    return sum([_ for _ in func(text)]).__round__(2)

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 \
        як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income} долларів.")


if __name__ == "__main__":
    main()