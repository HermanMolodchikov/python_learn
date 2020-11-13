words = ['мадам', 'топот', 'test', 'madam', 'word']
my_str = ['Око за око', 'А роза упала на лапу азора', 'Около Миши молоко']
new_words = []

qw = my_str[0][::-1]
print(qw)

for word in words:
    if word == word[::-1]:
        new_words.append(word)
print(new_words, id(new_words))

palindromes = [word for word in words if word == word[::-1]]
print(palindromes, id(palindromes))

newMyStr = []
for word in my_str:
    word_t = word.replace(' ', '').lower()
    if word_t == word_t[::-1]:
        newMyStr.append(word)

print(newMyStr, id(newMyStr))


l1 = list(range(1, 10))

l2 = list('hello')

print(l1)

s = '-'.join(map(str, l1))
s2 = ','.join(l2)
print(s)
print(s2)
