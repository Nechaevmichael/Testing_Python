# Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. Циклы использовать нельзя
#Примеры/Тесты:
#<function_name>(2,0) -> 1
#<function_name>(2,1) -> 2
#<function_name>(2,3) -> 8
#<function_name>(2,4) -> 16

# def building_in_degree(a: int, b: int) -> int:
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     else:
#         return a * (building_in_degree(a, b - 1))

# print(building_in_degree(2, 3))

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

print(function_sum(2, 3))