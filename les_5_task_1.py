# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

comp_ddict = defaultdict(list)
average_profit = 0
high_profit_comp = []
low_profit_comp = []

company_count = int(input('Введите количество предприятий: '))
comp_titles = [input(f'Введите название предприятия №{i + 1}: ') for i in range(company_count)]

for el in comp_titles:
    for i in range(4):
        comp_ddict[el].append(int(input(f'Введите прибыль предприятия {el} за квартал {i + 1}: ')))
    tmp = sum(comp_ddict[el]) / 4
    comp_ddict[el].append(tmp)
    average_profit += tmp
    tmp = 0
average_profit /= company_count

for key, val in comp_ddict.items():
    print(f'Средняя прибыль предприятия {key}: {val[4]}')
    if val[4] < average_profit:
        low_profit_comp.append(key)
    elif val[4] > average_profit:
        high_profit_comp.append(key)

print(f'\nПрибыль выше среднего у предприятий:\n{", ".join(high_profit_comp)}\n\n'
      f'Прибыль ниже среднего у предприятий:\n{", ". join(low_profit_comp)}')
