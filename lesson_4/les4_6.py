"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
from itertools import (count,
                       cycle)

x = int(input('Генерация начиная с числа:\n>>> '))
for i in count(x):
    print(i)
    if i > 10:
        break

y = [1, 2, 3]
for i in cycle(y):
    y.append(i)
    if len(y) > 15:
        break
print(y)
