# def hello(name, word):
#     print(f"Hello {name}. Say {word}")
#
#
# insertName = input('What is your name?:')
# insertWord = input('Insert word:')
# hello(insertName, insertWord)
# hello('Herman', 'Hello')
#

def get_sum(a, b):
    return a + b


x = 3
y = 4

print(get_sum(1, 3))
mySum = get_sum(10, 20)
newSum = get_sum(mySum, y)
print(newSum, mySum)

res = len('how are you')
print(len('hello'))
print(res)

# --------------home work------------------

#
# def square_calc(list1):
#     lst = []
#     for i in range(0, list1):
#         calc = input('Insert your number:')
#         lst.append(calc)
#     calc2 = [i * 2 for j in calc]
#     # return calc
#     print(calc2)
#
#
# quantity = int(input('How much elements do you want to calc:'))
# square_calc(quantity)


s = 'Hello world!'
if s.find(' '):
    print(s.upper())
else:
    print(s.lower())

if ' ' in s:
    print(s.upper())
else:
    print(s.lower())

# -----------------------------------


s2 = input('Введите строку:')


def set_register(s):
    if s.find(' '):
        return s.upper()
    else:
        return s.lower()


s3 = set_register(s2)

print(s3)


# ---------------multiplication_table------------


def multiplication_table(column, row):
    for i in range(1, column):
        print(i + 1)
        for j in range(1, row):
            print(i * j, end="\t")


multiplication_table(10, 4)
