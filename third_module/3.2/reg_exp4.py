"""
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\".
Sample Input:

\w denotes word character
No slashes here
Sample Output:

\w denotes word character
"""

import sys
import re

pattern = r"\\"

# выводит и работает правильно
for line in sys.stdin:
    if re.search(pattern, line.strip()):
        print(line.strip())

# проходит тесты но непонятно почему ничего не выводит?
print(*[line for line in sys.stdin if re.search(r"\\", line)], sep='')

