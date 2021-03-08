import re

st = [str(input()) for i in range(2)]
pattern = f'{st[1]}'

quantity =
print(re.search(pattern, st[0]).span()[1])
