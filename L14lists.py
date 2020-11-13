# l1 = [1, 2, 3, 'hello', ['test', 10], 'world', True]
#
# l2 = list('hello')
# l3 = list((1, 2, 3))
# l4 = [i for i in '123456789']
# #l5 = [i for i in 'hello world' if i not in [' '] and i != 'l']
# l5 = [i * 2 for i in 'hello world' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]
# l6 = list(range(5, 10, 2))
#
# print(l1, l2, l3, l4, l5, l6, sep='\n')
# print('mind table')
# for i in range(1, 10):
#     print(i + 1)
#     for j in range(2, 10):
#         print(i * j, end="\t")

l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
names = ['Invanov', 'Pertov', 'Sidorov']
print(names[1])

print(len(l[4]))
print(len(l))
print(l[4][0])#test
print(l[0:3])

l[2] = 'world'
print(l)

