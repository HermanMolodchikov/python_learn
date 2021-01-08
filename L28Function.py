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

# def f():
#     a = 10#local
#     a += 1
#     print(a)
#
# print(a)
# f()
# print(a)

# def f():
#     global a
#     a += 1
#     print(a)
#
# print(a)
# f()
# print(a)

l2 = [1, '2', 3]


def f(l):
    return [i * 2 for i in l]


print(f(l2))


def f2(l):
    def get_mult(x):
        if isinstance(x, int):
            return x * 2
    return [get_mult(i) for i in l if get_mult(i)]


print(f2(l2))


def f3(l):
    def get_mult(x):
        return x * 2
    return list(map(get_mult, l))


print(f3(l2))
