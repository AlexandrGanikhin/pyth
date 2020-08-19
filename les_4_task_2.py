# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

# ВЫВОД: алгоритмы сопоставимы по скорости и сложности, решето Эратосфена немного эффективнее.

from timeit import timeit
import cProfile

def eratosthenes(k):
    step = 1000
    magnifier = 0
    res = []
    sieve = [i for i in range(step)]
    sieve[1] = 0
    while True:
        for i in range(len(sieve)):
            if sieve[i] != 0:
                j = i + i
                while j < len(sieve):
                    sieve[j] = 0
                    j += i
        res.clear()
        res = [i for i in sieve if i != 0]
        if len(res) >= k:
            return res[k-1]
        else:
            magnifier += step
            sieve_app = [i for i in range(magnifier, magnifier + step)]
            sieve.extend(sieve_app)

# print(timeit('eratosthenes(125)', number=100, globals=globals())) # 0.10495908799999999
# print(timeit('eratosthenes(250)', number=100, globals=globals())) # 0.339229593
# print(timeit('eratosthenes(500)', number=100, globals=globals())) # 1.105391935
# print(timeit('eratosthenes(1000)', number=100, globals=globals())) # 4.0418261929999995

#cProfile.run('eratosthenes(1000)')
#          84645 function calls in 0.060 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.060    0.060 <string>:1(<module>)
#         1    0.046    0.046    0.060    0.060 les_4_task_2.py:15(eratosthenes)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:19(<listcomp>)
#         8    0.002    0.000    0.002    0.000 les_4_task_2.py:29(<listcomp>)
#         7    0.000    0.000    0.000    0.000 les_4_task_2.py:34(<listcomp>)
#         1    0.000    0.000    0.060    0.060 {built-in method builtins.exec}
#     84610    0.011    0.000    0.011    0.000 {built-in method builtins.len}
#         8    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         7    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}

#cProfile.run('eratosthenes(2000)')
#          417592 function calls in 0.291 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.291    0.291 <string>:1(<module>)
#         1    0.224    0.224    0.291    0.291 les_4_task_2.py:15(eratosthenes)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:19(<listcomp>)
#        18    0.011    0.001    0.011    0.001 les_4_task_2.py:29(<listcomp>)
#        17    0.001    0.000    0.001    0.000 les_4_task_2.py:34(<listcomp>)
#         1    0.000    0.000    0.291    0.291 {built-in method builtins.exec}
#    417517    0.055    0.000    0.055    0.000 {built-in method builtins.len}
#        18    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        17    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}

#cProfile.run('eratosthenes(4000)')
#          1868360 function calls in 1.314 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.314    1.314 <string>:1(<module>)
#         1    1.015    1.015    1.314    1.314 les_4_task_2.py:15(eratosthenes)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:19(<listcomp>)
#        38    0.045    0.001    0.045    0.001 les_4_task_2.py:29(<listcomp>)
#        37    0.002    0.000    0.002    0.000 les_4_task_2.py:34(<listcomp>)
#         1    0.000    0.000    1.314    1.314 {built-in method builtins.exec}
#   1868205    0.251    0.000    0.251    0.000 {built-in method builtins.len}
#        38    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        37    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


def simple_num(k):
    simple_lst = [2]
    n = 3
    while k > len(simple_lst) :
        for i in simple_lst:
            if n % i == 0:
                break
        else:
            simple_lst.append(n)
        n += 1
    return simple_lst[-1]



print(eratosthenes(500))
print(simple_num(500))


# print(timeit('simple_num(125)', number=100, globals=globals())) # 0.11042914100000001
# print(timeit('simple_num(250)', number=100, globals=globals())) # 0.45606994200000006
# print(timeit('simple_num(500)', number=100, globals=globals())) # 1.5697499629999998
# print(timeit('simple_num(1000)', number=100, globals=globals())) # 6.106599318999999

#cProfile.run('simple_num(1000)')
#          8921 function calls in 0.064 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.064    0.064 <string>:1(<module>)
#         1    0.063    0.063    0.064    0.064 les_4_task_2.py:94(simple_num)
#         1    0.000    0.000    0.064    0.064 {built-in method builtins.exec}
#      7918    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run('simple_num(2000)')
#          19391 function calls in 0.271 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.271    0.271 <string>:1(<module>)
#         1    0.268    0.268    0.271    0.271 les_4_task_2.py:94(simple_num)
#         1    0.000    0.000    0.271    0.271 {built-in method builtins.exec}
#     17388    0.003    0.000    0.003    0.000 {built-in method builtins.len}
#      1999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run('simple_num(4000)')
#          41815 function calls in 1.224 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.224    1.224 <string>:1(<module>)
#         1    1.217    1.217    1.224    1.224 les_4_task_2.py:94(simple_num)
#         1    0.000    0.000    1.224    1.224 {built-in method builtins.exec}
#     37812    0.006    0.000    0.006    0.000 {built-in method builtins.len}
#      3999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}