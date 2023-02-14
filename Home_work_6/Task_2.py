# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)
# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 2, 10) -> [2, 3, 6, 7, 10, 11, 16]
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension
# (*) Усложнение. Функция возвращает список кортежей вида: индекс, значение
# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]

def fine_idx_array(lst: list, a: int, b: int) -> list:
    result = []
    for idx, meaning  in enumerate(lst):
        if meaning >= a and meaning <= b:
            result.append(idx)
    return sorted(result)

print(fine_idx_array([-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7], 2, 10))

def fine_idx_array_1(lst: list, a: int, b: int) -> list:
    result = [idx for idx, meaning in enumerate(lst) if meaning >= a and meaning <= b]
    return sorted(result)

print(fine_idx_array([-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7], 2, 10))

def fine_idx_meaning_array(lst: list, a: int, b: int) -> list:
    result = [(idx, meaning) for idx, meaning in enumerate(lst) if a <= meaning <= b]
    return sorted(result)

print(fine_idx_meaning_array([-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7], 2, 10))