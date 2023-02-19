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
Во второй - в виде Иванов-И-И'''

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
file_write(MAIN_DIR / 'result' / 'res.txt', MAIN_DIR / 'result' / 'res1.txt')
