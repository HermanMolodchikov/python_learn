x = int(input("Input first number: "))
y = int(input("Input second number:"))
if x > 5 and y > 5:
    print(f'x>{x}')
elif x == 0 and y == 0:
    print(f'x={x}')
elif -5 <= x <= 5 and -5 <= y <= 5:
    print(f'x middle{x}')
elif x < -5 and y < -5:
    print(f'x<{x}')
else:
    print(f'you inserted wrong integer {18- x}')

coast = int(input("How much coast: "))
if not coast:
    print('coast this goods 0')
else:
    print(f'coast this goods: {coast}')

piece = int(input('How do you want pieces: '))

res = f'you want {piece} pieces' if piece else 'You want nothing'
print(res)
#print(f'you want {piece} pieces' if piece else 'You want nothing')

