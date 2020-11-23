def get_sum2(a, b):
    """
    Возвращает сумму фргументов a и b

    :param a: Первый операнд
    :type a: int
    :param b: Второй операнд
    :type b: int
    """
    return a + b


print(get_sum2(1, 2))


a = 5

def f():
    a = 10#local
    a += 1
    print(a)

print(a)
f()
print(a)