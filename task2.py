sec = int(input("Введите время в секундах: "))

minute = sec / 60
hour = minute / 60

print("Время в формате ч:м:с - {} : {} : {}".format(round(hour), round(minute), sec))
