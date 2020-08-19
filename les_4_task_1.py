# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# ВЫБРАННАЯ ЗАДАЧА:
# Определить, какое число в массиве встречается чаще всего


# Вывод: я выбрал задачу 4 из урока 3. Второе решение оказалось оптимальным и по скорости выполнения, и по
# асимптотической сложности алгоритма. У первого решения слабое место - вложенный цикл, а у третьего - метод
# count для списка, использованный в цикле.

from random import randint
from timeit import timeit
import cProfile

def rnd_array(size):
    array = [randint(0, 100) for _ in range(size)]
#    print(array)
    return array


def var_1(sz):
    array = rnd_array(sz)
    max_num_count, current_max_num = 0, 0
    max_nums = []

    for i in range(sz - 1):
        current_max_num_count = 1
        for n in range(i + 1, sz):
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

    # if max_num_count == 1:
    #     print('Числа в массиве не повторяются.')
    # else:
    #     print(f'Следующие числа встречаются в массиве {max_nums[0]} раз(а):')
    #     for el in range(1, len(max_nums)):
    #         print(f'{max_nums[el]}')

# print(timeit('var_1(50)', number=100, globals=globals())) #0.06835845299999999
# print(timeit('var_1(100)', number=100, globals=globals())) #0.24122081
# print(timeit('var_1(200)', number=100, globals=globals())) #0.43642218400000005
# print(timeit('var_1(400)', number=100, globals=globals())) #1.7665813040000002
# print(timeit('var_1(800)', number=100, globals=globals())) #7.148564963999999

# cProfile.run('var_1(500)')
#          2650 function calls in 0.035 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.035    0.035 <string>:1(<module>)
#         1    0.033    0.033    0.035    0.035 les_4_task_1.py:13(var_1)
#         1    0.000    0.000    0.003    0.003 les_4_task_1.py:7(rnd_array)
#         1    0.000    0.000    0.003    0.003 les_4_task_1.py:8(<listcomp>)
#       500    0.001    0.000    0.002    0.000 random.py:200(randrange)
#       500    0.000    0.000    0.002    0.000 random.py:244(randint)
#       500    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.035    0.035 {built-in method builtins.exec}
#         4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       500    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         2    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       638    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# cProfile.run('var_1(1000)')
#          5281 function calls in 0.135 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.135    0.135 <string>:1(<module>)
#         1    0.131    0.131    0.135    0.135 les_4_task_1.py:13(var_1)
#         1    0.000    0.000    0.004    0.004 les_4_task_1.py:7(rnd_array)
#         1    0.001    0.001    0.004    0.004 les_4_task_1.py:8(<listcomp>)
#      1000    0.001    0.000    0.003    0.000 random.py:200(randrange)
#      1000    0.001    0.000    0.003    0.000 random.py:244(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.135    0.135 {built-in method builtins.exec}
#         5    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         2    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1268    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
# cProfile.run('var_1(2000)')
#          10561 function calls in 0.455 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.455    0.455 <string>:1(<module>)
#         1    0.442    0.442    0.455    0.455 les_4_task_1.py:13(var_1)
#         1    0.000    0.000    0.013    0.013 les_4_task_1.py:7(rnd_array)
#         1    0.002    0.002    0.013    0.013 les_4_task_1.py:8(<listcomp>)
#      2000    0.004    0.000    0.009    0.000 random.py:200(randrange)
#      2000    0.002    0.000    0.011    0.000 random.py:244(randint)
#      2000    0.003    0.000    0.004    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.455    0.455 {built-in method builtins.exec}
#         9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         4    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      2542    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('var_1(4000)')
#          21035 function calls in 1.779 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.778    1.778 <string>:1(<module>)
#         1    1.760    1.760    1.778    1.778 les_4_task_1.py:13(var_1)
#         1    0.000    0.000    0.018    0.018 les_4_task_1.py:7(rnd_array)
#         1    0.003    0.003    0.018    0.018 les_4_task_1.py:8(<listcomp>)
#      4000    0.006    0.000    0.012    0.000 random.py:200(randrange)
#      4000    0.003    0.000    0.016    0.000 random.py:244(randint)
#      4000    0.004    0.000    0.006    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    1.779    1.779 {built-in method builtins.exec}
#         8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      4000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         4    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      5017    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('var_1(8000)')
#          42064 function calls in 7.186 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    7.186    7.186 <string>:1(<module>)
#         1    7.157    7.157    7.186    7.186 les_4_task_1.py:13(var_1)
#         1    0.000    0.000    0.029    0.029 les_4_task_1.py:7(rnd_array)
#         1    0.004    0.004    0.029    0.029 les_4_task_1.py:8(<listcomp>)
#      8000    0.010    0.000    0.019    0.000 random.py:200(randrange)
#      8000    0.005    0.000    0.025    0.000 random.py:244(randint)
#      8000    0.007    0.000    0.010    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    7.186    7.186 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      8000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         5    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     10043    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}


def var_2(sz):
    array = rnd_array(sz)
    arr_to_dict = {}
    max_nums_list = []
    max_count = 1

    for el in array:
        if el in arr_to_dict:
            arr_to_dict[el] += 1
        else:
            arr_to_dict[el] = 1

        if max_count < arr_to_dict[el]:
            max_nums_list.clear()
            max_nums_list.append(el)
            max_count = arr_to_dict[el]
        elif max_count == arr_to_dict[el]:
            max_nums_list.append(el)

    # print(f'Следующие числа встречаются в массиве {max_count} раз(а): {", ".join(str(q) for q in max_nums_list)}.'
    #       if max_count != 1
    #       else 'Числа в массиве не повторяются')

# print(timeit('var_2(50)', number=100, globals=globals())) # 0.014328627999999996
# print(timeit('var_2(100)', number=100, globals=globals())) # 0.029463789000000004
# print(timeit('var_2(200)', number=100, globals=globals())) # 0.058502578
# print(timeit('var_2(400)', number=100, globals=globals())) # 0.110013801
# print(timeit('var_2(800)', number=100, globals=globals())) # 0.22080757

#cProfile.run('var_2(500)')
#          2687 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.001    0.001    0.003    0.003 les_4_task_1.py:137(var_2)
#         1    0.000    0.000    0.002    0.002 les_4_task_1.py:7(rnd_array)
#         1    0.000    0.000    0.002    0.002 les_4_task_1.py:8(<listcomp>)
#       500    0.001    0.000    0.001    0.000 random.py:200(randrange)
#       500    0.000    0.000    0.002    0.000 random.py:244(randint)
#       500    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#        32    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       500    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        11    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       638    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

#cProfile.run('var_2(1000)')
#          5360 function calls in 0.005 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.001    0.001    0.005    0.005 les_4_task_1.py:137(var_2)
#         1    0.000    0.000    0.004    0.004 les_4_task_1.py:7(rnd_array)
#         1    0.001    0.001    0.004    0.004 les_4_task_1.py:8(<listcomp>)
#      1000    0.001    0.000    0.003    0.000 random.py:200(randrange)
#      1000    0.001    0.000    0.004    0.000 random.py:244(randint)
#      1000    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#        67    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        18    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1269    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

#cProfile.run('var_2(2000)')
#          10692 function calls in 0.011 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.011    0.011 <string>:1(<module>)
#         1    0.001    0.001    0.011    0.011 les_4_task_1.py:137(var_2)
#         1    0.000    0.000    0.010    0.010 les_4_task_1.py:7(rnd_array)
#         1    0.001    0.001    0.010    0.010 les_4_task_1.py:8(<listcomp>)
#      2000    0.003    0.000    0.007    0.000 random.py:200(randrange)
#      2000    0.002    0.000    0.008    0.000 random.py:244(randint)
#      2000    0.002    0.000    0.003    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#        80    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        34    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      2572    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

#cProfile.run('var_2(4000)')
#          21201 function calls in 0.021 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.021    0.021 <string>:1(<module>)
#         1    0.003    0.003    0.021    0.021 les_4_task_1.py:137(var_2)
#         1    0.000    0.000    0.018    0.018 les_4_task_1.py:7(rnd_array)
#         1    0.003    0.003    0.018    0.018 les_4_task_1.py:8(<listcomp>)
#      4000    0.006    0.000    0.012    0.000 random.py:200(randrange)
#      4000    0.003    0.000    0.015    0.000 random.py:244(randint)
#      4000    0.004    0.000    0.006    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
#       101    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      4000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#        52    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      5042    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

#cProfile.run('var_2(8000)')
#         42489 function calls in 0.038 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.038    0.038 <string>:1(<module>)
#         1    0.005    0.005    0.038    0.038 les_4_task_1.py:137(var_2)
#         1    0.000    0.000    0.034    0.034 les_4_task_1.py:7(rnd_array)
#         1    0.005    0.005    0.034    0.034 les_4_task_1.py:8(<listcomp>)
#      8000    0.012    0.000    0.023    0.000 random.py:200(randrange)
#      8000    0.006    0.000    0.029    0.000 random.py:244(randint)
#      8000    0.008    0.000    0.011    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.038    0.038 {built-in method builtins.exec}
#       140    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      8000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#       102    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     10241    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}

def var_3(sz):
    array = rnd_array(sz)
    max_count_numbers_arr = []
    max_count_num = 1

    for next_el in array:
        if array.count(next_el) > max_count_num:
            max_count_num = array.count(next_el)
            max_count_numbers_arr.clear()
            max_count_numbers_arr.append(next_el)
        elif array.count(next_el) == max_count_num and next_el not in max_count_numbers_arr:
            max_count_numbers_arr.append(next_el)

    # print(
    #     f'Следующие числа встречаются в массиве {max_count_num} раз(а): {", ".join(str(q) for q in max_count_numbers_arr)}.'
    #     if max_count_num != 1
    #     else 'Числа в массиве не повторяются')

# print(timeit('var_3(50)', number=100, globals=globals())) # 0.030014356
# print(timeit('var_3(100)', number=100, globals=globals())) # 0.093744907
# print(timeit('var_3(200)', number=100, globals=globals())) # 0.308672517
# print(timeit('var_3(400)', number=100, globals=globals())) # 1.217475191
# print(timeit('var_3(800)', number=100, globals=globals())) # 4.153772411

# cProfile.run('var_3(500)')
#          3658 function calls in 0.020 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.020    0.020 <string>:1(<module>)
#         1    0.000    0.000    0.020    0.020 les_4_task_1.py:274(var_3)
#         1    0.000    0.000    0.002    0.002 les_4_task_1.py:7(rnd_array)
#         1    0.000    0.000    0.002    0.002 les_4_task_1.py:8(<listcomp>)
#       500    0.001    0.000    0.001    0.000 random.py:200(randrange)
#       500    0.000    0.000    0.002    0.000 random.py:244(randint)
#       500    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
#         7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       500    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         6    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#      1000    0.017    0.000    0.017    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       639    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('var_3(1000)')
#          7294 function calls in 0.069 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.069    0.069 <string>:1(<module>)
#         1    0.001    0.001    0.069    0.069 les_4_task_1.py:274(var_3)
#         1    0.000    0.000    0.004    0.004 les_4_task_1.py:7(rnd_array)
#         1    0.001    0.001    0.004    0.004 les_4_task_1.py:8(<listcomp>)
#      1000    0.001    0.000    0.003    0.000 random.py:200(randrange)
#      1000    0.001    0.000    0.003    0.000 random.py:244(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.069    0.069 {built-in method builtins.exec}
#         6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         3    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#      2000    0.064    0.000    0.064    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1279    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('var_3(2000)')
#          14586 function calls in 0.285 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.285    0.285 <string>:1(<module>)
#         1    0.002    0.002    0.285    0.285 les_4_task_1.py:274(var_3)
#         1    0.000    0.000    0.007    0.007 les_4_task_1.py:7(rnd_array)
#         1    0.001    0.001    0.007    0.007 les_4_task_1.py:8(<listcomp>)
#      2000    0.003    0.000    0.005    0.000 random.py:200(randrange)
#      2000    0.001    0.000    0.006    0.000 random.py:244(randint)
#      2000    0.002    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.285    0.285 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         2    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#      4000    0.276    0.000    0.276    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      2576    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('var_3(4000)')
#          29089 function calls in 1.153 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.153    1.153 <string>:1(<module>)
#         1    0.006    0.006    1.153    1.153 les_4_task_1.py:274(var_3)
#         1    0.000    0.000    0.020    0.020 les_4_task_1.py:7(rnd_array)
#         1    0.003    0.003    0.020    0.020 les_4_task_1.py:8(<listcomp>)
#      4000    0.007    0.000    0.014    0.000 random.py:200(randrange)
#      4000    0.004    0.000    0.017    0.000 random.py:244(randint)
#      4000    0.005    0.000    0.007    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    1.153    1.153 {built-in method builtins.exec}
#         7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      4000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         5    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#      8000    1.126    0.000    1.126    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      5071    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('var_3(8000)')
#          58104 function calls in 3.967 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    3.967    3.967 <string>:1(<module>)
#         1    0.009    0.009    3.967    3.967 les_4_task_1.py:274(var_3)
#         1    0.000    0.000    0.028    0.028 les_4_task_1.py:7(rnd_array)
#         1    0.004    0.004    0.028    0.028 les_4_task_1.py:8(<listcomp>)
#      8000    0.010    0.000    0.019    0.000 random.py:200(randrange)
#      8000    0.005    0.000    0.025    0.000 random.py:244(randint)
#      8000    0.007    0.000    0.010    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    3.967    3.967 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      8000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         3    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#     16000    3.929    0.000    3.929    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     10092    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}