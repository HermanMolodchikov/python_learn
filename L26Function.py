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

# -----------------------------------------


arr2 = [i ** 2 for i in [1, 2, 3]]
print(arr2)
print(arr2[0] + arr2[1] + arr2[2])

l1 = [1, 2, 3]
res = 0
for num in l1:
    res += num ** 2
print(res)

time1 = 3
time2 = 6.7
time3 = 11.8
print(int(time1 * 0.5))
print(int(time2 * 0.5))
print(int(time3 * 0.5))

times = [3, 6.5, 11.8]
v = 0.5
V = 0
for i in times:
    V = i * v
    print(int(V))
    print('литров')

s = 'Hello world!'
if s.find(' '):
    print(s.upper())
else:
    print(s.lower())

if ' ' in s:
    print(s.upper())
else:
    print(s.lower())

#-----------------------------------
s2 = input('Введите строку:')


def set_register(s):
    if s.find(' '):
        return s.upper()
    else:
        return s.lower()


s3 = set_register(s2)

print(s3)
