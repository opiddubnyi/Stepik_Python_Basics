"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
Sample Input:

zabcz
zzz
zzxzz
zz
zxz
zzxzxxz
Sample Output:

zabcz
zzxzz
"""

import re
import sys

# first method
# finding match z***z

pattern = r'z...z'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)

# second method
# finding match 'z.{3}z'
re.compile()
print(*filter(re.compile(r'z.{3}z').search, sys.stdin), sep='')