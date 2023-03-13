#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Ivan Ivanov
# Created Date: 19/02/14:12
# version     = '0.1'
# ---------------------------------------------------------------------------
""" Script for parsing web server logs"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import re
# from ... import ...
from sys import argv
from datetime import datetime

# Передать аргументы скрипту путь / дата начала / дата завершения / сайт
# Если забыли передать запросить ввод
# Если не передали в обоих случаях вывести ошибку

formats = [
    "%d/%b/%Y:%H:%M" # 01/Jan/1999:00:00
    "%d-%m-%Y",  # 05-03-2023
    "%d %B %Y",  # 4 марта 2023
    "%d %b %y",  # 4 мар. 23
    "%d/%m/%Y",  # 05/03/2023
]

date_format = r'\b\d{1,4}[/-].{1,3}[/-]\d{1,4}[ :]\d{2}:\d{2}\b'

if len(argv) > 1:
    path = argv[1]
else:
    path = input("Введите путь до лога: ")

if not path:
    print("Ошибка: путь не был введен")
    raise TypeError
else:
    # здесь можно выполнить действия с использованием аргумента
    print("Вы ввели путь до файла лога: ", path)

if len(argv) > 1:
    startdate = datetime.strptime(argv[2], '%d/%b/%Y:%H:%M')
else:
    startdate = input("Введите дату начала дд/Ммм/гггг:00:00: ")
    try:
        # Преобразование введенной строки в объект datetime
        date_check_format = datetime.strptime(startdate, '%d/%b/%Y:%H:%M')
        print("Дата: ", date_check_format)
    except ValueError:
        # Вывод сообщения об ошибке, если введенная строка не соответствует формату
        print("Ошибка! Введенная дата не соответствует формату %d/%b/%Y:%H:%M, пример 01/Jan/1999:00:00")

if not startdate:
    print("Ошибка: дата не была введена")
    raise TypeError
else:
    # здесь можно выполнить действия с использованием аргумента
    print("Вы ввели дату начала: ", startdate)

if len(argv) > 1:
    enddate = datetime.strptime(argv[3], '%d/%b/%Y:%H:%M')
else:
    enddate = input("Введите дату окончания дд/Ммм/гггг:чч:мм: ")
    try:
        # Преобразование введенной строки в объект datetime
        date_check_format = datetime.strptime(enddate, '%d/%b/%Y:%H:%M')
        print("Дата: ", date_check_format)
    except ValueError:
        # Вывод сообщения об ошибке, если введенная строка не соответствует формату
        print("Ошибка! Введенная дата не соответствует формату %d/%b/%Y:%H:%M, пример 01/Jan/1999:01:00")

if not enddate:
    print("Ошибка: дата окончания не была введена")
    raise TypeError
else:
    # здесь можно выполнить действия с использованием аргумента
    print("Вы ввели дату окончания: ", enddate)

if len(argv) > 1:
    site = argv[4]
else:
    site = input("Введите сайт: ")

if not site:
    print("Ошибка: сайт не был введен")
    raise TypeError
else:
    # здесь можно выполнить действия с использованием аргумента
    print("Вы ввели сайт: ", site)

"""Парсим файл лога за указанные даты"""

# Открываем файл и читаем строки
with open(path, 'r') as file:
    lines = file.readlines()

# Распознаем строки в соответствии с датами
for line in lines:
    # print(line.split()[3])
    match = re.search(date_format, line.split()[3])
    print(match)
    convert = datetime.strptime(match,"%d/%b/%Y:%H:%M") # проблема
    print(convert)
    if match:
        print(line.strip())
        # Если дата находится в диапазоне между датами начала и окончания,
        # выводим строку на экран
        if startdate <= match.group() <= enddate: # проблема
            print(line.strip())
"""    try:
        date_str = line.split(' ')[3] # Четвертое слово в строке содержит дату
        # date = datetime.strptime(date_str, '%d/%b/%Y:%H:%M')
        if startdate <= date <= enddate:
            print(line.strip()) # Выводим строку без перевода строки
    except ValueError:
        # Если строка не начинается с даты, пропускаем ее
        pass
"""
