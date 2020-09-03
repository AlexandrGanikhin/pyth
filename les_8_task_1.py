# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9

from hashlib import sha1


def substring_counter(s):
    substr_list = [[s[i:k] for k in range(i + 1, len(s)+1) if i != 0 or k != 4]
                   for i in range(0, len(s))]
    hash_set = set(sha1(st.encode('utf-8')).hexdigest() for sublist in substr_list for st in sublist)
    return len(hash_set)


print(substring_counter('papa'))
