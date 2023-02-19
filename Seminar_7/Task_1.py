''' Дан текстовый файл csv файл. Разделитель данных #
Каждая строка файла представляет собой запись вида ФИО
Например:
Иванов#Иван#Иванович

Необходимо вывести эти данные на экран построчно в виде
Иванов Иван Иванович

И записать эти данные в список вида: [["Иванов", "Иван", "Иванович"]...]
[*] Усложнение. Файл находится в поддиректории data текущей директории. Сформировать путь к нему
с использованием os.path и pathlib'''

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
file_read(r'Seminar_7\data\name.txt')
file_read(MAIN_DIR / 'data' / 'name.txt')