from data_generator import DataGenerator
from perceptron import Perceptron


def main():
    data_generator = DataGenerator()
    train_data = data_generator.generate_train_data()
    test_data = data_generator.generate_test_data()
    seventh_data = data_generator.get_seventh_data()
    size = len(train_data[0])
    h = 3
    perceptron = Perceptron(h=h, size=size)
    perceptron.train(train_data=train_data, number_data=seventh_data)
    perceptron.check_train_data(train_data)
    perceptron.check_test_data(test_data)


if __name__ == '__main__':
    main()
