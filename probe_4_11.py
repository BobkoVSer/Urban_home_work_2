def test_function():
    def inner_function():
        b= 'Я в зоне видимости test_function'
        print('b=', b)
    inner_function()
a= 'Я в зоне видимости test_function'
test_function()