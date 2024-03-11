def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return f'ошибка: невозможно преобразовать {s} в целое число.'

def read_file(filename):
    try:
        with open (filename, 'r') as file: return file.read()
    except FileNotFoundError:
        return f'Ошибка: файл {filename} не найден.'
    except IOError:
        return f'ошибка ввода/вывода при работе с файлом {filename}'

def divide_numbers (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return f'ошибка: деления на ноль'
    except TypeError:
        return f'ошибка: аргументы должны быть числами.'

def access_list_element (lst, index):
    try:
        return lst [index]
    except IndexError:
        return f'ошибка: индекс {index} вне диапазона списка.'
    except TypeError:
        return f'ошибка: индекс должен быть целым числом.'