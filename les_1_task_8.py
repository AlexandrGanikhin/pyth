# Определить, является ли год, который ввел пользователь, високосным или невисокосным.
# ***(по Григорианскому календарю)

user_year = int(input('Введите год '))
if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
    print(f'Год {user_year} високосный.')
else:
    print(f'Год {user_year} невисокосный.')
