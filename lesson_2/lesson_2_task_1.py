# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль,
# если он ввел его в качестве делителя.

# https://drive.google.com/file/d/1xtNmgK5db_z8_3eWoZ8Kxl-oXTiNvk28/view?usp=sharing

def calc(sgn, n1, n2):
    if sgn == '+':
        return n1 + n2
    elif sgn == '-':
        return n1 - n2
    elif sgn == '/':
        return n1 / n2
    elif sgn == '*':
        return n1 * n2
    else:
        return None

user_sign = ''
while True:
    while user_sign != '0' and user_sign != '-' and user_sign != '*' and user_sign != '/' and user_sign != '+':
        user_sign = input('Введите знак операции (+, -, /, *), или введите 0, чтобы остановить программу: ')
        if user_sign != '0' and user_sign != '-' and user_sign != '*' and user_sign != '/' and user_sign != '+':
            print('Ошибка: неверный ввод.')

    if user_sign == '0':
        break

    user_num_1 = float(input('Введите первое число '))
    user_num_2 = float(input('Введите второе число '))

    if user_sign != '/' or user_num_2 != 0:
        print(calc(user_sign, user_num_1, user_num_2))
    else:
        print('На 0 делить нельзя')
    user_sign = ''
