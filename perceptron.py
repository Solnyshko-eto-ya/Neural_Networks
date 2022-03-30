import random

import numpy as np


class Perceptron:
    def __init__(self, size, h):
        self.threshold = h  # Порог функции активации = 3
        self.weights = np.random.uniform(-1, 1, size)  # Инициализация весов 15
        self.size = size

    def proceed(self, number):  # Является ли данное число 7
        net = 0
        for i in range(self.size):
            net += int(number[i]) * self.weights[i]

        return net >= self.threshold  # Превышен ли порог?

    def decrease(self, number):  # Уменьшаем вес, если сеть ошиблась и выдала 1
        for i in range(15):
            if int(number[i]) == 1:
                self.weights[i] -= 1

    def increase(self, number):  # Увеличиваем вес, если сеть ошиблась и выдала 0
        for i in range(15):
            if int(number[i]) == 1:
                self.weights[i] += 1

    def train(self, train_data, number_data, number=7):
        for i in range(1000):  # Тренировка
            option = random.randint(0, 9)

            if option != number:  # Если получилась цифра не 7
                if self.proceed(train_data[option]):  # Если сеть выдала True, то наказываем ее
                    self.decrease(train_data[option])
            else:  # Если получилась 7
                if not self.proceed(number_data):  # Если сеть выдала False, то показываем, что это нужная цифра
                    self.increase(number_data)

    def check_train_data(self, train_data):
        for i in range(len(train_data)):
            print(f'{i} это 7? {self.proceed(train_data[i])}')
        print('\n')

    def check_test_data(self, test_data):
        for i in range(len(test_data)):
            print(f'{i} это 7? {self.proceed(test_data[i])}')
        print('\n')
