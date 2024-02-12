def test_print (a, b= 'параметр по умолчанию', *args, **kwargs):
    print('a:', a)
    print('b:', b)
    print (args)
    print(kwargs)
    for i, arg in enumerate (args):
        print('поз. параметр', i, arg)
        for key, value in kwargs.items ():
            print('имен. параметр', key, value)
poz_parametr = [2.5 , 'QQQQ']
dict_parametr = {'key': 'param1', 'value': 1}
test_print(a= 'значение а', b='20', args=poz_parametr, kwargs=dict_parametr)



def factorial (n):
    if n==1:
        return 1
    factorial_1_minus_1 = factorial(n=n-1)
    return n * factorial_1_minus_1
print(factorial (7))