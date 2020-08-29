# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но, если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

from random import randint
from numpy import median

m = int(input('Введите натуральное число '))
rnd_list = [randint(-100, 100) for i in range(2 * m + 1)]

print(rnd_list)
print(f'Способ 1 - numpy.median. Медиана = {int(median(rnd_list))}')

left_list = []
right_list = []
equal = 0
mdn = 0
for i, el in enumerate(rnd_list):
    for k, elm in enumerate(rnd_list):
        if i != k and el > elm:
            left_list.append(elm)
        elif i != k and el < elm:
            right_list.append(elm)
        elif i != k:
            equal += 1
    if (len(left_list) == len(right_list)) or\
            (abs(len(left_list) - len(right_list)) <= equal):
        mdn = el
        break
    else:
        left_list.clear()
        right_list.clear()
        equal = 0

print(f'Способ 2. Медиана =  {mdn}')
