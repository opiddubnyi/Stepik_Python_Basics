"""Вам дана частичная выборка из датасета зафиксированных преступлений,
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано
максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
"""

import csv
import re

res = {}
pattern = r'\w+/\w+/2015'
with open(r'D:/Download/Crimes.csv', 'r') as file:
    reader = csv.reader(file)

    for line in reader:
        if re.match(pattern, line[2].split()[0]) is not None:
            res[line[5]] = 1

with open(r'D:/Download/Crimes.csv', 'r') as file:
    reader = csv.reader(file)

    for line in reader:
        if re.match(pattern, line[2].split()[0]) is not None:
            res[line[5]] += 1

print(res)
