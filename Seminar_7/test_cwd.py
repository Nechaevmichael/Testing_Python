from os import getcwd
print(getcwd())

from pathlib import Path
main_dir_1 = Path(__file__).parent
main_dir_2 = Path(".")
print(main_dir_1.absolute())
print(main_dir_2.absolute())

from os.path import join, abspath, dirname
main_os_path = abspath(dirname(__file__))
main_os_path_1 = abspath(dirname('.'))
print(main_os_path)
print(main_os_path_1)

main_dir_op1 = abspath(dirname(__file__))
main_dir_op2 = abspath(dirname('.'))

main_dir_pl1 = Path(__file__).parent
main_dir_pl2 = Path('.')

print(f'Текущая директория: {getcwd()}')
print('PATHLIB')
print(f'Через __file__: {main_dir_pl1.absolute()}')
print(f'Через ".": {main_dir_pl2.absolute()}')
print("OS.PATH")
print(f'Через __file__: {main_dir_op1}')
print(f'Через ".": {main_dir_op1}')