"""Реализуйте класс PositiveList, отнаследовав его от класса list,
для хранения положительных целых чисел. Также реализуйте новое исключение
NonPositiveError.

В классе PositiveList переопределите метод append(self, x) таким образом,
чтобы при попытке добавить неположительное целое число бросалось исключение
NonPositiveError и число не добавлялось, а при попытке добавить
положительное целое число, число добавлялось бы как в стандартный list.

В данной задаче гарантируется, что в качестве аргумента x метода append
всегда будет передаваться целое число.

Примечание:
Положительными считаются числа, строго большие нуля.
"""


class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def append(self, item):

        if item > 0:
            return super(PositiveList, self).append(item)
        else:
            raise NonPositiveError


s = PositiveList()
s.append(1)
s.append(0)
s.append(1)

print(s)
