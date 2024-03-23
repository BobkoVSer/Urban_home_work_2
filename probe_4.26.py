def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x * y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x / y
        return subtract
my_func_add = create_operation("add")
print(my_func_add(2,3))


multiply = lambda x: x **2
print(multiply(4))

def multiply_def(x):
   return x **2
print(multiply_def(4))


class Rect:
   def __init__(self, a):
       self.a = a
   def __call__(self, b):
       return b*self.a

my_rect = Rect (a=2)
result = my_rect (b=4)
print(result)


