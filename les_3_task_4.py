# Определить, какое число в массиве встречается чаще всего

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_num_count, current_max_num = 0, 0
max_nums = []

for i in range(SIZE - 1):
    current_max_num_count = 1
    for n in range(i + 1, SIZE):
        if array[i] == array[n]:
            current_max_num = array[i]
            current_max_num_count += 1
    if max_num_count == current_max_num_count:
        max_nums.append(current_max_num)
    elif max_num_count < current_max_num_count:
        max_num_count = current_max_num_count
        max_nums.clear()
        max_nums.append(current_max_num_count)
        max_nums.append(current_max_num)

print(array)

if max_num_count == 1:
    print('Числа в массиве не повторяются.')
else:
    print(f'Следующие числа встречаются в массиве {max_nums[0]} раз(а):')
    for el in range(1, len(max_nums)):
        print(f'{max_nums[el]}')
