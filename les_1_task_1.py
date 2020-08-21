# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/1W4WunzDUeCod1N8ZfRV4ipo4vsMYKwyS/view?usp=sharing

user_num = int(input ('Введите целое трехзначное число ' ))
dig_1 = user_num // 100
dig_2 = (user_num - (dig_1 * 100)) // 10
dig_3 = user_num - (dig_1 * 100) - (dig_2 * 10)
num_sum = dig_1 + dig_2 + dig_3
num_mpl = dig_1 * dig_2 * dig_3
print(f'{num_sum=}, {num_mpl=}')
