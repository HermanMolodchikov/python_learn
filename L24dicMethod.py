# dict.clear() - очищает словарь.
# dict.copy() - возвращает копию словаря.
# classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).
# dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
# dict.items() - возвращает пары (ключ, значение).
# dict.keys() - возвращает ключи в словаре.
# dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
# dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.
# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default (по умолчанию None).
# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
# dict.values() - возвращает значения в словаре.

user1 = {'name': 'Herman', 'changes': (1989, 1996, 2002, 2007), 'email': 'germanmol@mail.ru', 'age': 35, 'height': 182}

print(user1.keys())

user2 = user1.copy()
print(user2)
user2.clear()
print(user2)
print(f'{user1.items()} ...itmes')
user3 = user1.copy()
print(f'{user3.pop("changes")}...pop')
print(f'{user3}....without changes')
user3 = user1.copy()
print(user3.pop('email', 'NO'))
print(user3)
# user3 = user1.copy()
# print(f'{user3.popitem("name", "Herman")}...popitem')
print(f'{user3.setdefault("title2")}.....setdefault')
print(f'{user3}....set title2')

print(f'{user3.update({"secondname": "Molodchikov"})}....update new surname')
print(f'{user3.update({"age": 36})}....update age')
print(f'{user3.update({"weight": 82})}....update()')
print(f'{user3.update({"weight": 82})}....update()')
print(user3)

print(f'{user3.values()}....values()')


