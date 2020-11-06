# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

start_rng_dividend = 2
end_rng_dividend = 99
start_rng_divider = 2
end_rng_divider = 9

dividers_dict = {n: n * 0 for n in range(start_rng_divider, end_rng_divider + 1)}

for i in range(start_rng_dividend, end_rng_dividend + 1):
    for key, val in dividers_dict.items():
        if i % key == 0:
            dividers_dict[key] += 1

for key, val in dividers_dict.items():
    print(f'Чисел, кратных числу {key}: {val}')
