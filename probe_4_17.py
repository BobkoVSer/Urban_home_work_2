class Vehicle:
    vehicle_type = None
    def inspect (self):

        print('Количество колес - ', self.vehicle_type)

class Car:
    Price = 1000000

    def horse_powers(self, horse_powers):
        self.horse_powers = horse_powers

    def __str__(self):
            return ' {} мощность, {} стоимость = 1000000'.format(self.__class__.__name__, self.horse_powers,
                                                                 self.Price)
class Nissan (Vehicle, Car):
    def horse_powers(self):
        self.horse_powers()

nissan = Nissan()
nissan.horse_powers = 2500
nissan.inspect()
print(nissan)

