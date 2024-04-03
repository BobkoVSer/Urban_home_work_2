def func_decorator(func):
   def wrapper(*args, **kwargs):
      print('____ делаем перед вызовом функции ____')
      func(*args, **kwargs)
      print('____ делаем после вызова функции ____')
      return wrapper


def sum_three():
   a = 2
   b = 3
   c = 6
   res = a + b + c
   print(res)
   sum_three = func_decorator(sum_three)
   sum_three()
