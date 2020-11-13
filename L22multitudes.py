m = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
m2 = set('hello')
m3 = {i for i in range(1, 10)}
m4 = {5, 3, 10, 9, 2}
m5 = {}
m6 = set()

print(m)
print(m2)
print(m3)
print(m4, type(m4))
print(type(m5))
print(type(m6))

nums = [1, 2, 3, 1, 4, 5, 2, 4, 3]
nums2 = set(nums)
print(nums2)

a = set('abracadabra')
b = set('alacazam')

c = a | b#объединение нескольких множеств
z = a - b#вычитание
x = a & b#пересечение
y = a ^ b#множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.

print(a, b, c, z, x, y, sep='\n')

# set.copy() - копия множества.
# set.update(other, ...); set |= other | ... - объединение.
# set.intersection_update(other, ...); set &= other & ... - пересечение.
# set.difference_update(other, ...); set -= other | ... - вычитание.
# set.symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
# set.add(elem) - добавляет элемент в множество.
# set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует.
# set.discard(elem) - удаляет элемент, если он находится в множестве.
# set.pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
# set.clear() - очистка множества.

multy1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
multy2 = multy1.copy()

print(multy1, id(multy1))
print(multy2, id(multy2))

multy1.add('melon')
print(multy1, id(multy1))

multy2.remove('apple')
print(multy2, id(multy2))

multy1.discard('orange')
print(multy1, id(multy1))

multy1.pop()
print(multy1, id(multy1))

multy1.clear()
print(multy1, id(multy1))
print(multy2, id(multy2))

a = frozenset('hello')
print(a)

for i in multy2:
    print(i)
