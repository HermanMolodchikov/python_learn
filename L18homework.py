arr = [1, 2, 3]
l5 = [i * 2 for i in arr]
print(l5)

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
