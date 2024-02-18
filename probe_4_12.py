class House:
    def __unit__(self):
        self.numberOFfloors = 10

house = House()
for numberOFfloors in range (0, 10):
    new_numberOFfloors = numberOFfloors +1
    print('Текущий этаж дома равен:', numberOFfloors + 1)