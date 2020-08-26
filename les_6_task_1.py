# Для каждого упражнения написать программную реализацию.
# Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию).
# Каждую задачу необходимо сохранять в отдельный файл. Рекомендуем использовать английские имена, например, les_6_task_1.
# Для оценки «Отлично» необходимо выполнить все требования, указанные в задании и примечаниях.
#
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
#
# ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
#
# ● написать 3 варианта кода (один у вас уже есть);
#
# ● проанализировать 3 варианта и выбрать оптимальный;
#
# ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить
# в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
#
# ● написать общий вывод: какой из трёх вариантов лучше и почему.
#
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
# а проявили творчество, фантазию и создали универсальный код для замера памяти.

#----------------------------------------------------------------------------------------------------------------------

# Система: windows 7 64 bit
# python 3.8.2 32 bit
# Решение 1 заняло 3864 байт памяти
# Решение 2 заняло 4444 байт памяти
# Решение 3 заняло 573 байт памяти
# С точки зрения использования памяти оптимальным будет третий вариант,
# он занимает меньше всего памяти, поскольку не хранит промежуточную
# информацию, хранит только результат в строке.

# Я выбрал задачу 1 из урока 3:
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

from sys import getsizeof

START_RND_DIVIDEND = 2
END_RND_DIVIDEND = 99
START_RND_DIVIDER = 2
END_RND_DIVIDER = 9


def variant_1():
    resoult = {}
    dividers_dict = {n: n * 0 for n in range(START_RND_DIVIDER, END_RND_DIVIDER + 1)}

    for i in range(START_RND_DIVIDEND, END_RND_DIVIDEND + 1):
        for key, val in dividers_dict.items():
            if i % key == 0:
                dividers_dict[key] += 1

    for key, val in dividers_dict.items():
        resoult[key] = val
    #return resoult
    return locals()


def variant_2():
    tmp_list = [[i for i in range(START_RND_DIVIDEND, END_RND_DIVIDEND + 1) if i % n == 0]
                for n in range(START_RND_DIVIDER, END_RND_DIVIDER + 1)]
    resoult = {i + START_RND_DIVIDER: len(tmp_list[i]) for i in range(len(tmp_list))}
    #return resoult
    return locals()


def variant_3():
    resoult = ''
    end_str = ', '
    count = 0
    for i in range(START_RND_DIVIDER, END_RND_DIVIDER + 1):
        for k in range(START_RND_DIVIDEND, END_RND_DIVIDEND + 1):
            if k % i == 0:
                count += 1
        if i == END_RND_DIVIDER:
            end_str = ''
        resoult = f'{resoult}{i}: {count}{end_str}'
        count = 0
    #return resoult
    return locals()


def mem_counting(x):
    global mem_size #я осознаю, что использование глобальной переменной в функции неправильно
                    #в данном случае, но у меня никак иначе не вышло организовать подсчет размера в рекурсии
                    #и тем более не удалось переписать функцию при помощи циклов. Буду ждать вебинар
                    #для разбора практического задания.
    mem_size += getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                mem_counting(key)
                mem_counting(value)
        elif not isinstance(x, str):
            for item in x:
                mem_counting(item)
    return mem_size


def local_global_mem_counting(local_global_dict):
    total_mem = 0
    for el in local_global_dict.values():
        total_mem += mem_counting(el)
    return total_mem


mem_size = 0
print(local_global_mem_counting(variant_1()))
mem_size = 0
print(local_global_mem_counting(variant_2()))
mem_size = 0
print(local_global_mem_counting(variant_3()))
