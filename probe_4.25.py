def mul_by (x):
    return x**2
my_numbers =[1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

def is_odd (x):
    return x%2
result = map(mul_by, filter (is_odd, my_numbers))
print(result)
print(list(result))