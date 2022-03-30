from data_generator import DataGenerator
from perceptron import Perceptron


class Layer:
    def __init__(self, train_data, test_data, h):
        self.train_data = train_data
        self.test_data = test_data
        self.size = len(train_data[0])
        self.h = h
        self.perceptrons = [Perceptron(size=self.size, h=h) for _ in range(10)]

    def train(self):
        for i in range(len(self.train_data)):
            self.perceptrons[i].train(train_data=self.train_data, number_data=self.train_data[i], number=i)

    def predict(self):
        for key, value in self.test_data.items():
            result = [perceptron.proceed(value) for perceptron in self.perceptrons]
            try:
                if result.index(True) == key:
                    print(f"{key} Угадано")
            except ValueError:
                print(f"{key} Не угадано")


def main():
    data_generator = DataGenerator()
    train_data = data_generator.generate_train_data()
    test_data = data_generator.generate_layer_data()
    layer = Layer(train_data=train_data, test_data=test_data, h=3)
    layer.train()
    layer.predict()


if __name__ == '__main__':
    main()
