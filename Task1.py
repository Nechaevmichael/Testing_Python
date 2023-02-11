# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
#Примеры/Тесты:
#<function_name>(0,0) -> 0
#<function_name>(0,2) -> 2
#<function_name>(3,0) -> 3

def function_sum(a: int, b: int) -> int:
    if b == 0:
        return a
    return function_sum(a + 1, b - 1)

print(function_sum(2, 4))