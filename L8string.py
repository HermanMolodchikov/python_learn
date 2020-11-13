#string


my_text = "\"Hello\", 'Python!' \\test "
print(my_text[0] )# Выводит первый символ
print(my_text[0:7] )# Выводит подстроку text от 0 символа до 5 (включительно с нулевым, исключая пятый)
# print(my_text[4:10]) # Выведет строку от 4 символа до 10 (включая четвертый, исключая 10)
# print(my_text[0:14]) # Выведет всю строку
# print(my_text[7:]) # Выведет строку с 7 символа до конца
# print(my_text[:5]) # Выведет строку с начала до 5 символа. Аналогично print text[0:5]
# print(my_text[:]) # Выведет всю строку
# print(my_text[-1]) # Выводит последний символ
# print(my_text[-1:-14]) # Не сработает, выведет пустую строку
# print(my_text[::2]) # Третий аргумент - шаг. Выведет каждый второй символ
# print(my_text[::-1] )# Шаг отрицательный. Выведет фразу наоборот
# print(my_text + "Nice to code you") # Выведет новую строку
# print(my_text[-1] * 10) # Выведет 10 восклицательных знаков

verse = "\nУ неё всё своё — и бельё, и жильё,\n\
Ну а я ангажирую угол у тёти.\n\
Для неё — всё свободное время моё,\n\
На неё я гляжу из окна, что напротив.\n"

verse_2 = "\nУ неё каждый вечер не гаснет окно,\n\
И вчера мне лифтёр рассказал за полбанки:\n\
У неё два знакомых артиста кино\n\
И один популярный артист из «Таганки».\n"

verse_3 = '''\nИ пока у меня в ихнем ЖЭКе рука,
Про неё я узнал очень много нюансов:
У неё старший брат — футболист «Спартака»,
А отец — референт в Министерстве финансов. \n'''

verseeng = """
Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth.

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same.

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference."""
print(verse + verse_2 + verse_3 + verseeng)
print(verseeng[0:1:2])
