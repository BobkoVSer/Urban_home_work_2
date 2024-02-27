from random import randint
class Bulding:

    total = 0

    def __init__(self):
        Bulding.total += 1

floor = []
height_floor = randint (1, 40)
while len(floor) < height_floor:
    b_1 = Bulding()
    floor.append(b_1)
Bulding = (b_1)
print(Bulding.total)