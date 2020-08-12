#Посчитать четные и нечетные цифры введенного натурального числа.
#Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def num_to_dig(un, ev = 0, od = 0):
    if un < 1:
        return ev, od
    else:
        if un % 10 % 2 == 0:
            ev += 1
        else:
            od += 1
        return num_to_dig(un // 10, ev, od)

user_num = int(input('Введите натуральное число '))
even_count, odd_count = num_to_dig(user_num)
print(f'Четных цифр в числе {even_count}, нечетных {odd_count}.')
