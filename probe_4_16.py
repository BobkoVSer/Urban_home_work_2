class Car:
    Price = 1000000
    def horse_powers (self, horse_powers):
        self.horse_powers = horse_powers




    def __str__(self):
        return ' {} мощность: {} стоимость = 1000000'.format(self.__class__. __name__, self.horse_powers,
                                                             self.Price)
class Nissan(Car):
    def horse_powers(self):
        self.horse_powers()



class Kia(Car):
    def horse_powers(self):
        self.horse_powers()

nissan = Nissan()
nissan.horse_powers = 2000
print(nissan)

kia = Kia()
kia.horse_powers = 1600
print(kia)




