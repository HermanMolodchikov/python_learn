d = {}
product1 = {'title': 'Sony', 'price': 100}
product2 = dict(title='iPhone', price=100)

users = [
    ['bob@gmail.com', 'Bob'],
    ['katy@gmail.com', 'Katy'],
    ['john@gmail.com', 'John']
]

d_users = dict(users)

print(type(d))
print(d)
print(product1)
print(product2)
print(users)
print(d_users)

users_t = (
    ('bob@gmail.com', 'Bob'),
    ('katy@gmail.com', 'Katy'),
    ('john@gmail.com', 'John')
)

t_users = dict(users_t)
print(users_t)
print(t_users)

product3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)
print(product3)

nums = {i: i + 1 for i in range(1, 10)}
print(nums)

print(product1['title'])
print(product1.get('title'))

for key in product1:
    print(f'{key}: {product1[key]}')

for key, value in product1.items():
    print(key, value)

products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iphone', 'price': 110},
    {'title': 'Samsung', 'price': 900}
]

print(products)

for product in products:
    print(product['title'], product['price'])