class InvalidDataException (Exception):

    pass
class ProssecingExcwption (Exception):
    pass

try:
    raise InvalidDataException ('30 февраля')
except InvalidDataException as exc:
    print(f'выявлено исключение {exc}')
    raise ProssecingExcwption ('Высокосный год')