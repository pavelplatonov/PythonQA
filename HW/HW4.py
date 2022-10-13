# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата,
#      и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.


# def square(a):
#     return (
#         a * 4,
#         a * a,
#         ((a**2 + a**2) ** 0.5),
#     )


# print(*square(2), sep="\n")
###################################
# lst = [11, 18, 9, 12, 23, 4, 17]
# lost = []
# for idx in range(len(lst)):
#     val = lst[idx]
#     if val > 15:
#         lost.append(val)
#         lst[idx] = 15
# print("modif:", lst, "-lost:", lost)
########################################

# 4.2. Напишите функцию, которая принимает произвольное количество именованных
#      аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer


# def dicttxt(**sost):
#     for k, v in sost.items():
#         print(f"{k}: {v}")


# dicttxt(name="Rom", age="22", last_name="Kuper", posit="Hacker")

#######################################
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21]
#      создайте новый список, содержащий только положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# d = list(filter(lambda x: x > 0, my_list))
# # print(*d, sep="\n")

# # 4.4. Используя лямбда выражение, получите результат перемножения
# #      значений в предыдущем списке
# umn = map(lambda x: x * x, d)
# print(list(umn))

# from functools import reduce
# print(reduce(lambda x, y: x * y, my_list))
# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции,
#      выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
from HW4_my_calc import *

prod_res = prod(100, 20)
print(prod_res)

div_res1 = divide(45, 9)
print(div_res1)

div_res2 = divide(5, 0)
print(div_res2)

add_res = add(585, 1987)
print(add_res)

remain_res = remain(541, 6)
print(remain_res)

sub_res = subtract(230, 149)
print(sub_res)


#############################
# def printScores(student, *scores):
#     print(f"Student Name: {student}")
#     for score in scores:
#         print(score)


# printScores("Jonathan", 100, 95, 88, 92, 99)
