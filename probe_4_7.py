def print_params(a= 1, b= 'строка', c= True, f= 42, g= 44):
   print(a, b, c)
   print(b,c)
   print(a,c)
   print(f,g)
   print(f)
   print(g)

values_list = [1, 'строка', True]
values_list_2 = [42, 44]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
res = print_params (*values_list, *values_list_2)
print(res)




