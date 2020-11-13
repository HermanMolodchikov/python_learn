# x = 10
# print(x, id(x))
# x = 20
# print(x, id(x))

s = 'Hello '
print(s, id(s))
s += 'world'
print(s, id(s))

l = [1, 2, 3]
print(l, id(l))
l.append(5)
print(l, id(l))

x = 10
y = x
print(x, id(x))
print(y, id(y))

x = 15
print(x, id(x))
print(y, id(y))
