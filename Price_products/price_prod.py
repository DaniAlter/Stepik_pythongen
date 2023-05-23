import csv
import json
from collections import Counter
# Простенький код для подсчета годового заработка на продуктах. Данные о количестве продуктов хранятся в 4-х csv-файлах.
# Цены на каждую позицую в json
res = Counter()
for i in range(4):
    temp = Counter()
    with open(f'quarter{str(i+1)}.csv', encoding='utf-8') as file:
        quarter = list(csv.reader(file))[1:]
        for elem in quarter:
            s = 0
            for c in elem[1:]:
                s += int(c)
            temp[elem[0]] = temp.get(elem[0], s)
    res += temp
with open('prices.json', encoding='utf-8') as fj:
    price = json.load(fj)

summa = 0
for key in price.keys():
    summa += price[key] * res[key]

print(f'Годовая выручка составила: {summa} единиц.')
