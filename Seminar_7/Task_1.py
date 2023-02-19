''' 1. Дан текстовый файл csv файл. Разделитель данных #
Каждая строка файла представляет собой запись вида ФИО
Например:
Иванов#Иван#Иванович

Необходимо вывести эти данные на экран построчно в виде
Иванов Иван Иванович

И записать эти данные в список вида: [["Иванов", "Иван", "Иванович"]...]
[*] Усложнение. Файл находится в поддиректории data текущей директории. Сформировать путь к нему
с использованием os.path и pathlib

2. Данные в списке необходимо преобразовать к виду: Иванов И.И.
Полученные строки записать в новый файл. Файл должен находится в поддиректории rezults.
Данные необходимо записать в два разных файла:
В первый - в виде Иванов И.И.
Во второй - в виде Иванов-И-И

3. Имея список [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович'], ['Соколов', 'Илья', 'Григорьевич']]
преобразовать его в списки вида
['Иванов-И-И'...]
['Иванов И. И.'...]
с использованием Comprehension; Comprehension + функция; Comprehension + lambda; map
Усложение - дополнить обработку списка условием: Выбираем только те элементы, в которых первая буква П'''

from pathlib import Path
MAIN_DIR = Path(__file__).parent

def file_read(file_name: str) -> None:

    result = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for string in file:
            string = string.strip().split('#')
            result.append(string)
            print(*string)
    print(result)
    print('*'*30)
    
def file_write(file_name: str, file_name_1: str) -> None:
    result = [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович'], ['Соколов', 'Илья', 'Григорьевич']]
    with open(file_name, 'w', encoding='utf-8') as file_write1:
        with open(file_name_1, 'w', encoding='utf-8') as file_write2:
            for surname, name, parent in result:
                template1 = f'{surname} {name[0]}. {parent[0]}.\n'
                template2 = f'{surname}-{name[0]}-{parent[0]}\n'
                file_write1.write(template1)
                file_write2.write(template2)
# file_read(r'Seminar_7\data\name.txt')
# file_read(MAIN_DIR / 'data' / 'name.txt')
# file_write(MAIN_DIR / 'result' / 'res.txt', MAIN_DIR / 'result' / 'res1.txt')


lst = [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович'], ['Соколов', 'Илья', 'Григорьевич']]

# lst2 = [f'{man[0]}-{man[1][0]}-{man[2][0]}' for man in lst]
# lst2 = [f'{surname}-{name[0]}-{parent[0]}' for surname, name, parent in lst]
# print(lst2)

# lst3 = [f'{man[0]} {man[1][0]}. {man[2][0]}.' for man in lst]
# lst4 = [f'{surname} {name[0]}. {parent[0]}.'for surname, name, parent in lst]
# print(lst3)
# print(lst4)

def template(surname, name, parent):
    return f'{surname} {name[0]}. {parent[0]}'

lst4 = [template(surname, name, parent) for surname, name, parent in lst]
print(lst4)

lst5 = [(lambda surname, name, parent: f'{surname} {name[0]}. {parent[0]}')(surname, name, parent) for surname, name, parent in lst]
print(lst5)

