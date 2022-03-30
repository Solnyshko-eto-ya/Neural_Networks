class DataGenerator:
    @staticmethod
    def generate_test_data():
        num71 = list('101001010000100')  # искаженные семерки
        num72 = list('110001010100100')
        num73 = list('101000010100100')
        num74 = list('111001000100100')
        num75 = list('111001010000100')
        num76 = list('111001010100000')
        return [num71, num72, num73, num74, num75, num76]

    @staticmethod
    def generate_layer_data():
        result = dict()
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
        nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
        for i in range(len(nums)):
            result[i] = nums[i]
        return result

    @staticmethod
    def generate_train_data():
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
        return [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]  # Список

    @staticmethod
    def get_seventh_data():
        return list('111001010100100')
