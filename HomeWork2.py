# Задание 1

my_list = [0, 'яблоко', 3.2]
my_list.append([])
my_list.append({})
my_list.append(())

for i in my_list:
    print(type(i))

# Задание 2

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
length = len(my_list)
v = 0

while v < length - 1:
    my_list[v], my_list[v + 1] = my_list[v + 1], my_list[v]
    v += 2
print(my_list)


def change(list):
    length = len(list)
    v = 0
    while v < length - 1:
        list[v], list[v + 1] = list[v + 1], list[v]
        v += 2
    print(list)


change(my_list)

# Задание 3
time_of_year = ['осень', 'зима', 'весна', 'лето']
year_time_dict = {1: time_of_year[1], 2: time_of_year[1], 3: time_of_year[2], 4: time_of_year[2],
                  5: time_of_year[2], 6: time_of_year[3], 7: time_of_year[3], 8: time_of_year[3],
                  9: time_of_year[0], 10: time_of_year[0], 11: time_of_year[0], 12: time_of_year[0]}


def user_input():
    user = input('Введите номер месяца в формате от 1 до 12: ')
    return user

while True:
    try:
        user_number = int(user_input())
        if user_number < 1 or user_number > 12:
            print('Вы ввели неверный формат, попробуйте еще раз')
            continue
        print(year_time_dict[user_number])
        break
    except ValueError:
        print('Вы ввели неверный формат, попробуйте еще раз')

# Задание 4

message = str(input('Введите набор слов, разделенных пробелом: '))
message_list = message.split()
for i, item in enumerate(message_list):
    a = int(len(item))
    if a > 10:
        print(i + 1, item[0:10])
    else:
        print(i + 1, item)

# Задание 5

my_list = [7, 5, 3, 3, 2]
a = int(input('Введите число: '))

for item in my_list:
    if item == a:
        result_index = my_list.index(item)
        my_list.insert(result_index, a)
        print(my_list)
        break
    elif item < a:
        my_list.insert(0, a)
        print(my_list)
        break
    else:
        my_list_len = int(len(my_list))
        my_list.insert(my_list_len, a)
        print(my_list)
        break













