import random

num0 = list('111101101101111')  # Цифры (Обучающая выборка)
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001010100100')
num8 = list('111101111101111')
num9 = list('111101111001111')

nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]  # Список

num71 = list('101001010000100')  # искаженные семерки
num72 = list('110001010100100')
num73 = list('101000010100100')
num74 = list('111001000100100')
num75 = list('111001010000100')
num76 = list('111001010100000')

weights = []  # Инициализация весов
for i in range(15):
    weights.append(0)

# Порог функции активации
threshold = 4


def proceed(number):  # Является ли данное число 7
    net = 0
    for i in range(15):
        net += int(number[i]) * weights[i]

    return net >= threshold   # Превышен ли порог?


def decrease(number):  # Уменьшаем вес, если сеть ошиблась и выдала 1
    for i in range(15):
        if int(number[i]) == 1:
            weights[i] -= 1


def increase(number):  # Увеличиваем вес, если сеть ошиблась и выдала 0
    for i in range(15):
        if int(number[i]) == 1:
            weights[i] += 1


for i in range(50000):  # Тренировка
    option = random.randint(0, 9)

    if option != 9:   # Если получилась цифра не 7
        if proceed(nums[option]):  # Если сеть выдала True, то наказываем ее
            decrease(nums[option])
    else:  # Если получилась 7
        if not proceed(num7):   # Если сеть выдала False, то показываем, что это нужная цифра
            increase(num7)

print(weights)

print("0 это 7? ", proceed(num0))  # Прогоняем по обучающей выборке
print("1 это 7? ", proceed(num1))
print("2 это 7? ", proceed(num2))
print("3 это 7? ", proceed(num3))
print("4 это 7? ", proceed(num4))
print("5 это 7? ", proceed(num5))
print("6 это 7? ", proceed(num6))
print("7 это 7? ", proceed(num7))
print("8 это 7? ", proceed(num8))
print("9 это 7? ", proceed(num9), '\n')


print("Узнал 7? ", proceed(num5))  # Прогоняем по тестовой выборке
print("Узнал 7 - 1? ", proceed(num71))
print("Узнал 7 - 2? ", proceed(num72))
print("Узнал 7 - 3? ", proceed(num73))
print("Узнал 7 - 4? ", proceed(num74))
print("Узнал 7 - 5? ", proceed(num75))
print("Узнал 7 - 6? ", proceed(num76))
