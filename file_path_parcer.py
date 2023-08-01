#Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
#Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os
import argparse
import logging
def file_path_parser(file_path):
    path, file = os.path.split(file_path)
    name, ext = os.path.splitext(file)
    return (path, name, ext)

'''
path, name, ext = file_path_parser('Python/Advanced/Homework/test.py')
print(f'Path: {path}')
print(f'Name: {name}')
print(f'Ext: {ext}')
'''
# вызов из командной строки
# python3 file_path_parcer 'Python/Advanced/Homework/test.py'
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Парсер абсолютного пути файла')
    parser.add_argument('param', metavar='path', type=str,  nargs="*", help='пример ввода аргументов: 1-e воскресенье сентября')
    args = parser.parse_args()
    print(file_path_parser(*args.param))  