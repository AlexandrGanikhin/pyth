# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

def sum_hex(n1, n2):
    ALL_DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    digit_rotate = deque(ALL_DIGITS)
    resoult_sum = deque()
    plus_one = 0
    additive = ''

    for l in range(abs(len(n1) - len(n2))):
        additive = f'{additive}0'

    if len(n1) < len(n2):
        n1 = f'{additive}{n1}'
    elif len(n1) > len(n2):
        n2 = f'{additive}{n2}'

    for i in range(len(n1) - 1, -1, -1):
        index_dig_1 = ALL_DIGITS.index(n1[i])
        index_dig_2 = ALL_DIGITS.index(n2[i])
        shift = index_dig_1 + index_dig_2 + plus_one

        if shift < 16:
            resoult_sum.appendleft(ALL_DIGITS[shift])
            plus_one = 0
        else:
            digit_rotate.rotate(-shift)
            resoult_sum.appendleft(digit_rotate[0])
            digit_rotate = deque(ALL_DIGITS)
            plus_one = 1
    if plus_one == 1:
        resoult_sum.appendleft('1')

    res = ''.join(resoult_sum)

    return res


def multipl_hex(n1, n2):
    ALL_DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    multipliers_list = []
    res = '0'
    if len(n1) < len(n2):
        n1, n2 = n2, n1

    for k, n1_el in enumerate(n1):
        for i, el in enumerate(n2):
            count_of_sum = ALL_DIGITS.index(el)
            multipliers_list.append(f'{multiple_as_recurcive_sum_hex(n1_el, count_of_sum)}'
                                    f'{"".join(["0" for _ in range(len(n2) - i -1)])}'
                                    f'{"".join(["0" for _ in range(len(n1) - k -1)])}')
    for elm in multipliers_list:
        res = sum_hex(res, elm)

    return res


def multiple_as_recurcive_sum_hex(num, count, n = 0, _itr = 0):
    if _itr == 0:
        n = num
    if count == 0:
        return 0
    elif count < 2:
        return num
    else:
        count -= 1
        _itr += 1
        num = sum_hex(num, n)
        return multiple_as_recurcive_sum_hex(num, count, n, _itr)




user_num_1 = input('Введите первое число ').upper()
user_num_2 = input('Введите второе число ').upper()

print(f'Сумма {user_num_1} и {user_num_2} = {sum_hex(user_num_1, user_num_2)}')
print(f'Произведение {user_num_1} и {user_num_2} = {multipl_hex(user_num_1, user_num_2)}')
