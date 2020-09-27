# Задание 1

a = 100
b = 'слово'
print(str(a) + ' ' + b)
name = input('Введите ваше имя: ')
print(name)

# Задание 2

time = int(input('Введите время в секундах: '))
seconds = time % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(f'{hour}:{minutes}:{seconds}')

# Задание 3

n = input('Введите число: ')
print(int(n)+int(n+n)+int(n+n+n))

# Задание 4

a = int(input('Введите число больше 0: '))
max = a % 10
a = a // 10
while a > 0:
    if a % 10 > max:
        max = a % 10
    a = a // 10
print(max)

# Задание 5

income = int(input('Введите значение выручки фирмы: '))
costs = int(input('Введите значение издержек фирмы: '))
if income > costs:
    profit = income - costs
    profitability = round(profit / income, 2)
    numberOfEmployees = int(input('Введите количество сотрудников в Вашей компании: '))
    profitForEmployees = round(profit / numberOfEmployees, 2)
    print(f'Ваша фирма работает с прибылью, которая составила {profit}, рентабельность выручки - {profitability}, '
          f'прибыль фирмы в расчете на одного сотрудника - {profitForEmployees}')
else:
    print('Ваша фирма работает в убыток')

# Задание 6

day_km = 2
day = 1
km = 2.2

while km > day_km:
    day_km = day_km * 0.1 + day_km
    day += 1
print(day)