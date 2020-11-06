# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

import copy

MATRIX_X = 3
MATRIX_Y = 5

user_list = [[float(input(f'Введите число {n + 1} строки № {i + 1}: '))
            for n in range(MATRIX_X)]
            for i in range(MATRIX_Y)]


for line in user_list:
    sum_line = 0
    for el in line:
        print(f'{el:>15.2f}', end = '')
        sum_line += el
    print(f'{sum_line:>15.2f}')
