def get_sum(a, b, c, d):
    return a + b + c + d


print(get_sum(1, 2, 3, 4))

print('hello', sep=' ', end='\n')


def get_sum2(a, b, c=1, d=0):
    return a + b + c + d


print(get_sum2(1, 2, ))
print(get_sum2(1, 2, d=5))


def get_sum3(*args):
    return sum(args)


print(get_sum3(1, 2, 3))

print(sum([1, 2, 3]))


def func(**kwargs):
    print(kwargs)


func(a=1, b=5, c=20)


def f(a, x, *args, **kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)


f(1, 2, 3, 4, b='test', c='hi')
