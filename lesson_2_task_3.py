# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

out_num = 0
user_num = int(input('Введите натуральное число '))
while user_num > 9:
    current_dig = user_num % 10
    out_num = out_num * 10 + current_dig
    user_num //= 10
out_num = out_num * 10 + user_num
print(out_num)
