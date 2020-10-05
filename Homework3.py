# Задание 1


def user_input_1():
    a = input('Введите целое положительное число 1: ')
    return a


def user_input_2():
    b = input('Введите целое положительное число 2: ')
    return b


while True:
    user_number_1 = int(user_input_1())
    user_number_2 = int(user_input_2())
    if user_number_1 < 0 or user_number_2 < 0:
        print('Вы ввели неверный формат, попробуйте еще раз')
        continue
    break


def result(input_a, input_b):
    try:
        result_1 = input_a / input_b
        result_2 = input_b / input_a
        return result_1, result_2
    except ZeroDivisionError:
        print('Вы ввели неверный формат, попробуйте еще раз')


print(result(user_number_1, user_number_2))

# Задание 2

name = input('Введите Ваше имя')
surname = input('Введите Вашу фамилию')
year_of_bd = input('Введите дату рождения')
email = input('Введите Вашу электронную почту')
phone = input('Введите номер Вашего телефона')


def user(*info):
    print(f'имя: {name} фамилия: {surname} дата рождения: {year_of_bd} email: {email} телефон: {phone}')


user()


# Задание 3


def my_func(int_list):
    max_int_1 = max(int_list)
    int_list.remove(max_int_1)
    max_int_2 = max(int_list)
    result = max_int_2 + max_int_1
    return result


my_list = [2, 3, 9]
print(my_func(my_list))


# Задание 4

def my_func(x, y):
    result = pow(x, y)
    return result


print(my_func(2, 3))


def my_func(x, y):
    r = 1
    while (y > 0):
        r *= x
        y -= 1
    print('result:', r)


my_func(2, 4)


# Задание 5

def user_input():
    numbers = input('Введите числа, разделенные пробелом')
    numbers_list = numbers.split()
    sum: int = 0
    for i in numbers_list:
        sum += int(i)
    print(sum)


user_input()
