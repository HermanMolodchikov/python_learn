def odd_ball(arr):
    """

    :param arr: получаем список
    :type arr: list
    :return: возвращаем сравнение

    """
    return arr.index('odd') in arr


print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]))  # True
print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]))  # False
print(odd_ball(["even", 10, "odd", 2, "even"]))  # True

print(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"].index(55))  # True
print(10 in ["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"])  # True
print(11 in ["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"])  # True


def find_sum(n):
    return sum(i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0)
    '''
    
    '''
    # res = 0
    # for i in range(n + 1):
    #     if i % 3 == 0 or i % 5 == 0:
    #         res += i
    # return res


print(find_sum(5))  # return 8 (3 + 5)
print(find_sum(10))  # return 33 (3 + 5 + 6 + 9 + 10)

names = ["Rayn", "Kieran", "Herman", "Anna", "John", "Alexander"]


def get_names(arr):
    return [i for i in arr if len(i) == 4]


print(get_names(names))
