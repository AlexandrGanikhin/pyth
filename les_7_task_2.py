# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import uniform


def merge_sort(lst, _res_len=0, _splited=[]):

    def merge(list_for_sort):
        if len(list_for_sort) == 1:
            return list_for_sort[0]

        sorted_lst = []
        if len(list_for_sort) % 2 != 0:
            sorted_lst.append(list_for_sort.pop())
        rng = len(list_for_sort)

        for i in range(0, rng, 2):
            part_of_sorted_lst = []

            while True:
                if list_for_sort[i][0] <= list_for_sort[i + 1][0]:
                    part_of_sorted_lst.append(list_for_sort[i].pop(0))
                else:
                    part_of_sorted_lst.append((list_for_sort[i + 1].pop(0)))

                if len(list_for_sort[i]) == 0:
                    for el in list_for_sort[i + 1]:
                        part_of_sorted_lst.append(el)
                    break
                elif len(list_for_sort[i + 1]) == 0:
                    for el in list_for_sort[i]:
                        part_of_sorted_lst.append(el)
                    break

            sorted_lst.append(part_of_sorted_lst)
        return merge(sorted_lst)

    if _res_len == 0:
        _res_len = len(lst)

    tmp_list = [[],[]]
    if len(lst) > 1:
        if len(lst) % 2 == 0:
            len_part_1 = len_part_2 = int(len(lst) / 2)
        else:
            len_part_1 = len(lst) // 2 + 1
            len_part_2 = len(lst) // 2

        for el in range(len_part_2):
            tmp_list[1].append(lst.pop())

        for el in range(len_part_1):
            tmp_list[0].append(lst.pop())

        merge_sort(tmp_list[0], _res_len)
        merge_sort(tmp_list[1], _res_len)
    else:
        _splited.append(lst)
        if _res_len == len(_splited):
            print(merge(_splited))
            #return merge(_splited) #вот этот return никак не хочет работать и я не понимаю, почему.
                                    #Сломал с ним мозг. Буду очень благодарен за объяснение...
                                    #Функция возвращает None, пришлось принтить из функции вместо return (строкой выше).

#я не понял, зачем таким сложным образом делить список по одному элементу,
#мы получаем то же самое, что было в исходном списке,
#но сделал, как написано в Википедии

rnd_list = [uniform(0,49) for _ in range(11)]
print(rnd_list)
merge_sort(rnd_list)
