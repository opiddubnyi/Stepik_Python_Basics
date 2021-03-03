"""Вашей программе на вход подаются две строки s и t, состоящие из строчных
латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa

Sample Input 1:

abababa
aba
Sample Output 1:

3
Sample Input 2:

abababa
abc
Sample Output 2:

0
Sample Input 3:

abc
abc
Sample Output 3:

1
Sample Input 4:

aaaaa
a
Sample Output 4:

5
"""

a, b = [str(input()) for _ in range(2)]

count = 0

while a.find(b) != -1:
    count += 1
    index = a.find(b)
    a = a[index + 1:]

print(count)



