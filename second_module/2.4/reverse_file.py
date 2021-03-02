"""
Вам дается текстовый файл, содержащий некоторое количество непустых
строк. На основе него сгенерируйте новый текстовый файл, содержащий те же
строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

Пример выходного файла:
ff
dde
c
ab
"""

res =[]
with open (r'D:/Download/dataset_24465_4.txt') as fin, \
        open(r'D:/Download/res.txt', 'w') as fout:
    for line in fin:
        res.append(line.rstrip())
    for i in range(len(res)-1, -1, -1):
        fout.write(res[i]+'\n')

