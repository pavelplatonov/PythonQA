# сложение
def add(x, y):
    return x + y


# вычитание
def subtract(x, y):
    return x - y


# умножение
def prod(x, y):
    return x * y


# деление
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Can't divide by zero"


def remain(x, y):
    return x % y
