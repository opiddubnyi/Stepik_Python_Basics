"""Вашей программе на вход подаются три строки s, a, b, состоящие из
строчных латинских букв. За одну операцию вы можете заменить все вхождения
строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной
операции строка s перейдет в строку "baba", после выполнения двух и операций
– в строку "bbaa", и дальнейшие операции не будут изменять строку s.

Необходимо узнать, после какого минимального количества операций в строке s
не останется вхождений строки a. Если операций потребуется более 1000,
выведите Impossible.

Выведите одно число – минимальное число операций, после применения которых в
строке s не останется вхождений строки a, или Impossible, если операций
потребуется более 1000.

Условие задачи было изменено 12.09.2018
Sample Input 1:

ababa
a
b
Sample Output 1:

1
Sample Input 2:

ababa
b
a
Sample Output 2:

1
Sample Input 3:

ababa
c
c
Sample Output 3:

0
Sample Input 4:

ababac
c
c
Sample Output 4:

Impossible
"""


def swop(start, a, b):
    counter = 0
    while counter <= 1000:
        if counter == 1000:
            print("Impossible")
        if start.count(a) >= 1:
            start = start.replace(a, b)
            counter += 1
            if start.count(a) == 0:
                print(counter)
                break
        else:
            print('0')
            break


swop(*[str(input()) for _ in range(3)])
