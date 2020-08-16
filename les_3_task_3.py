# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

el_min, el_max = 0 , 0
for i in range(len(array)):
    if array[el_min] > array[i]:
        el_min = i
    if array[el_max] < array[i]:
        el_max = i
array[el_min], array[el_max] = array[el_max], array[el_min]
print(array)
