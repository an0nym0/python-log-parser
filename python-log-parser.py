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
# from ... import ...
from sys import argv
from datetime import datetime

# Передать аргументы скрипту путь / дата начала / дата завершения / сайт
# Если забыли передать запросить ввод
# Если не передали в обоих случаях вывести ошибку

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
    startdate = datetime.strptime(argv[2], '%d/%b/%Y')
else:
    startdate = input("Введите дату начала дд/Ммм/гггг: ")

if not startdate:
    print("Ошибка: дата не была введена")
    raise TypeError
else:
    # здесь можно выполнить действия с использованием аргумента
    print("Вы ввели дату начала: ", startdate)

if len(argv) > 1:
    enddate = datetime.strptime(argv[3], '%d/%b/%Y')
else:
    enddate = input("Введите дату окончания дд/Ммм/гггг: ")

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