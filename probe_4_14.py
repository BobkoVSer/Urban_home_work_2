class Buiding:
    def __init__(self, numberOFfloors, buildingType):
        self. numberOFfloors = numberOFfloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOFfloors == other.numberOFfloors and self.buildingType == other.buildingType

b_1 = Buiding(46, 'Building')
b_2 = Buiding(46, 'Building')
r = b_1 == b_2
print(r)