a = (1, 2, 3, 4, 5, 6)
b = [1, 2, 3, 4, 5, 6]

print(type(a))
print(type(b))
print(a.__sizeof__())
print(b.__sizeof__())

t1 = 1, 2, 3 #упаковка картежа

t2 = tuple((1, 2, 3))
t3 = ()
t4 = (1,)

t5 = tuple('hello')
print(t5[1])

word1 = tuple('hello ')
word2 = tuple('world!')
word3 = word1 + word2

print(word3)
print(len(word3))
print(word3.count('l'))
print(word3.index('l', 2, 5))

if 'a' in word3:
    print(word3.index('l'))
else:
    print('NO')

for i in word3:
    print(i, end=' ')
print('\n')

for i in word3:
    if i == '0 ':
        continue
    print(f'"{i}"', end=' ')
print('\n')

t6 = (10, 11, [1, 2, 3], [4, 5, 6], ['Hello', 'world!'])
print(t6, id(t6))
t6[4][0] = 'new'
print(t6, id(t6))
t6[4][0] = 'Hello'
t6[4].append('in the end')
print(t6, id(t6))

t7 = (1, 2, 3)
x = t7[0]
y = t7[1]
z = t7[2]
a, b, c = t7
print(x, y, z)
print(a, b, c)

x = 1
y = 2
print(x, y)
x, y = y, x
print(x, y)