x = 'C:\Python\\new.txt'
y = r'C:\Python\new.txt'
contstr = x + '\n' + y
print(contstr)

name = 'Herman'
age = 35

print('My name is ' + name + "." " I'm " + str(age) + " years old.")

print("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 \n" * 5)

greeting = 'Hello world!'
print(greeting[::5])#H d
print(greeting[0])#H
print(greeting[0:12])#Hello world!
print(greeting[::-1])#!dlrow olleH
print(greeting[::-2])#!lo le
print(greeting[:-1])#Hello world
print(greeting[-1])#!
print(greeting[::5])#H d

'''
+---+---+---+---+---+---+---+---+---+---+---+---+
| H | e | l | l | o |   | w | o | r | l | d | ! |
+---+---+---+---+---+---+---+---+---+---+---+---+
0   1   2   3   4   5   6   7   8   9  10  11  12
-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2 -1
'''
#[X:Y:Z]

greet = 'Hello world!'

print(greet[0:12])
print(greet[6:])
print(greet[::2])
print(greet[:] + "$$$$$$$$$$$$$$$$$$$1")
print(greet[:])

s = 'hello world'


s2 = s.capitalize()
print(s.upper())
print(s.lower())
print(s.istitle())
print(s.startswith('hel'))
print(s.startswith('el'))
print(s, s2)
print(s.center(20, '@'))
print(s.count('1', 2, 5))
print(str(len(s)) + ' Length')
print(str(s.find('l', 3, 1)) + ' find')
print(s.index("l"))
print(s.replace('l', 't'))
print(s.split())
print(str(s.isdigit()) + " ************ isdigit")
print(str(s.isalpha()) + " ************ isalpha")
print(str(s.isalnum()) + " ************ isalnum")
print(str(s.islower()) + " ************ islower")
print(str(s.isupper()) + " ************ isupper")
print(str(s.isspace()) + " ************ isspace")

