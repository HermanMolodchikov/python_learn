name = 'Herman, {0}'
age = 30
email = 'germanmol@mail.ru'

print('My name is ' + name + '. I\'m ' + str(age))
print('My name is %(name)s. I\'m %(age)d' %{'name': name, 'age': age})
print('My name is %s. I\'m %d' %(name, age))
print('My name is %s. I\'m %d. My email %s.' %('David', age, email))

print('Title: %s, Price: %.2F' %('Sony', 40.5))

#format
name2 = 'Alesha, {}'
print(name2.format('hi'))

print('My name is {}. I\'m {}. My email {}.' .format('David', age, email))
print('My name is {0}. I\'m {1}. My email {2}.' .format('David', age, email))
print('My name is {name}. I\'m {age}. My email {email}.' .format(name="name", age=age, email=email))

#f-strings

print(f'My name is {name}. I\'m {age + 5}. My email {email}.f-strings')
print('5 + 0 = {}'.format(5 + 2))
print(f'5 + 0 = {5 + 2}')
