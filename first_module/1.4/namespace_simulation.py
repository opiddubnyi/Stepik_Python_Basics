"""
Реализуйте программу, которая будет эмулировать работу с пространствами имен.
Необходимо реализовать поддержку создания пространств имен и добавление в них
переменных.
В данной задаче у каждого пространства имен есть уникальный текстовый
идентификатор – его имя.
Вашей программе на вход подаются следующие запросы:
create <namespace> <parent> –  создать новое пространство имен с именем
<namespace> внутри пространства <parent>
add <namespace> <var> – добавить в пространство <namespace> переменную <var>
get <namespace> <var> – получить имя пространства, из которого будет взята
переменная <var> при запросе из пространства <namespace>, или None, если
такого пространства не существует
Рассмотрим набор запросов:
add global a
create foo global
add foo b
create bar foo
add bar a
Структура пространств имен описанная данными запросами будет эквивалентна
структуре пространств имен, созданной при выполнении данного кода
a = 0
def foo():
  b = 1
  def bar():
    a = 2
В основном теле программы мы объявляем переменную a, тем самым добавляя ее в
пространство global. Далее мы объявляем функцию foo, что влечет за собой
создание локального для нее пространства имен внутри пространства global.
В нашем случае, это описывается командой create foo global. Далее мы объявляем
внутри функции foo функцию bar, тем самым создавая пространство bar
внутри пространства foo, и добавляем в bar переменную a.
Добавим запросы get к нашим запросам
get foo a
get foo c
get bar a
get bar b
Представим как это могло бы выглядеть в коде
a = 0
def foo():
  b = 1
  get(a)
  get(c)
  def bar():
    a = 2
    get(a)
    get(b)
Результатом запроса get будет имя пространства, из которого будет взята нужная
переменная.
Например, результатом запроса get foo a будет global, потому что в пространстве
foo не объявлена переменная a, но в пространстве global, внутри которого
находится пространство foo, она объявлена. Аналогично, результатом запроса
get bar b будет являться foo,а результатом работы get bar a будет являться bar.
Результатом get foo c будет являться None, потому что ни в пространстве foo,
 и в его внешнем пространстве global не была объявлена переменная с.
Более формально, результатом работы get <namespace> <var> является
<namespace>, если в пространстве <namespace> была объявлена переменная <var>
get <parent> <var> – результат запроса к пространству, внутри которого было
создано пространство <namespace>, если переменная не была объявлена
None, если не существует <parent>, т. е. <namespace>﻿ – это global
Формат входных данных
В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
В каждой из следующих n строк дано по одному запросу.
Запросы выполняются в порядке, в котором они даны во входных данных.
Имена пространства имен и имена переменных представляют из себя строки длины не более 10, состоящие из строчных латинских букв.
Формат выходных данных
Для каждого запроса get выведите в отдельной строке его результат.
"""


def create(_name, _arg):
    if _arg not in namespace.keys():
        namespace[_arg] = [_name]

    # if parent is present in keys -> add namespace inside parent array
    if _arg in namespace.keys():
        namespace[_arg].append(_name)

    # if not present and we need to add another namesp-arg pair:
    if _arg in namespace.keys() and _name not in namespace.keys():
        namespace[_name] = [_arg]


# add <namespace> <var>
def add(_name, _arg):
    # adding in namespace:
    namespace[_name].append(_arg)


# get <namespace> <var>
def get(_name, _arg):
    # return None if no parent:
    if _name == 'global' and _arg in namespace['global']:
        print('global')
    elif _name == 'global' and _arg not in namespace['global']:
        print(None)

    else:
        # <namespace> if <var> in <namespace>
        if _arg in namespace[_name]:
            print(_name)
        else:
            get(namespace[_name][0], _arg)


storage = []
namespace = {'global': []}

for commands in range(int(input())):
    cmd, name, arg = str(input()).split()
    if cmd == 'create':
        create(name, arg)
    elif cmd == 'add':
        add(name, arg)
    elif cmd == 'get':
        get(name, arg)