import warnings

def divide(a,b):
    if b == 0.01:
        warnings.warn('Делитель близится к нулю', category=UserWarning)
        return None
        return a / b
a = [(0, 1)]

divide(1, 0.001)
for i in a:
    result = divide(*i)
print(i)
print('Закончили')









