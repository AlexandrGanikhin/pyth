# ). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import randint


def buble_sort(lst): #вариант 1, классический
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    print(lst)


def buble_sort_modified(lst):  #вариант 2: пускаем пузырьки навстречу друг другу, так меньше проходов по списку
    n = 1

    if len(lst) % 2 == 0:
        edge = len(lst) // 2
    else:
        edge = len(lst) // 2 + 1

    while n < edge:
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

            if lst[len(lst) - n - i] > lst[len(lst) - n - i - 1]:
                lst[len(lst) - n - i], lst[len(lst) - n - i - 1] =\
                    lst[len(lst) - n - i - 1], lst[len(lst) - n - i]
        n += 1
    print(lst)


rnd_list = [randint(-100,99) for _ in range(10)]
copy_of_rnd_list = list(rnd_list)

print(rnd_list)
buble_sort(rnd_list)
buble_sort_modified(copy_of_rnd_list)
