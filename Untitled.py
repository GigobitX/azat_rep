'''1. Реализовать вывод информации о промежутке времени
зависимости от его продолжительности duration в секундах:
до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s>
сек; * остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:

duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек'''

'''duration = int(input('Сколько секунд: '))
one_day = duration//86400
one_hour = (duration%86400)//3600
one_minute = ((duration%86400)%3600)//60
one_second = ((duration%86400)%3600)%60
print (one_day, ' дн', one_hour, ' час', one_minute, ' мин', one_second, ' сек')'''

'''2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7.

* Решить задачу под пунктом b, не создавая новый список.'''


# list_a = [idx ** 3 for idx in range(1000) if id%2]

# # print(list_a)
# def plusing(lst):
#     answer = 1
#     for i in lst:
#         answer += i
#     return answer

# print(plusing([1, 2, 3, 4, 5]))

#2.a
# from functools import reduce
list_a = [idx ** 3 for idx in range(1000) if idx%2]
print(str(list_a[30]))
# reduce(lambda a, x: a + x, map(lambda x: list(x), list_a))first_elem = list_a[0]

# my_list = ['Иванов Иван Иванович' ,'','', 'Больница', 'Исполняющий обязанности главного врача']
# name = my_list[0].split()
# name.extend(my_list[3:])
# print(name)


# a = plusing(list_a[1])
# list_b = [plusing() for idx in list_a if idx%7]
# print(a)
'''
x = [int(a) for a in str(num)]
if x % 7:
    print(x)
else:
    print('no')'''









# #while all_values <= 1000
#
# day_sales = [1589.5, 2687.5, 5478.2, 1236.5, 4756.5] idx = 0
# total_sales = 0
# while idx < len(day_sales): # pre-condition
# total_sales = total_sales + day_sales[idx]
# idx = idx + 1
# price_per_product = total_sales / len(day_sales) print(price_per_product) # 3149.6400000000003'''


''''
3.Склонение слова

Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
Пробуйте их решать, если уверены в своих силах'''
