def caching_fibonacci():
    '''
    Функція, яка створює та використовує кеш для зберігання і 
    повторного використання вже обчислених значень чисел Фібоначчі.
    '''
    # Створюємо словник, що міститиме вже обраховані при попередніх 
    # викликах функції fibonacci значення
    cache = {}
    def fibonacci(n: int) -> int:
        '''
        Функція, яка безпосередньо обчислює число Фібоначчі
        '''
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n >= 1000:
            return f"Your number {n} is more, then maximum recursion depth exceeded! Must be less, then 1000!"
        # Якщо наше число вже було обраховано та міститься у словнику кешу,
        # то число не вираховується, а повертається відповідне значення із словника
        elif n in cache.keys():
            return cache[n]
        # Обчислюємо число Фібоначчі та поміщаємо його до нашого словника-кеша
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))