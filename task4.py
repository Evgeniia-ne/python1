n = int(input('Введите значение выручки: '))
m = int(input('Введите значение издержек: '))
if n >= m:
    profit = n - m
    print('Финансовый результат - прибыль. Величина прибыли: ', profit)
    profitability = profit / n
    print('Рентабельность выручки: ', profitability)
    count = int(input('Введите количество сотрудников: '))
    work = profit / count
    print('Прибыль в расчете на одного сотрудника: ', work)

else:
    print('Финансовый результат - убыток')