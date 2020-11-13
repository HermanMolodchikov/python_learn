#list.append(x)#Добавляет элемент в конец списка
#list.extend(L)#Расширяет список list, добавляя в конец все элементы списка L
#list.insert(i, x)#Вставляет на i-ый элемент значение x
#list.remove(x)#Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
#list.pop([i])#Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
#list.index(x, [start [, end]])#Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
#list.count(x)	#Возвращает количество элементов со значением x
#list.sort([key=функция])#Сортирует список на основе функции
#list.reverse()#Разворачивает список
#list.copy()#Поверхностная копия списка
#list.clear()#Очищает список


list1 = [1, 2, 3, 'hello', ['test', 10], 'world', True]
names = ['Invanov', 'Pertov', 'Sidorov']
print(names[1])
list2 = [213, 124, 54356, 124, 546, 7, 23]
list1[2] = 'world'
list1[:2] = [10, 15]

list1.append(['new', 1])
print(list1)

list1.extend([[5, 7]])
print(list1)

list1[4].insert(0, 'insert')
list1.insert(2, 'insert')
print(list1)

list1.remove('world')
print(list1)

item = list1.pop()
print(str(item) + ' pop')

list1.index(10)
print(str(list1) + ' index')

print(str(list1.count(10)) + ' ...........count')

print(str(list2) + ' before sort')
list2.sort()
print(str(list2) + ' after sort')

list2.reverse()
print(str(list2) + ' reverse')

copyList = list1[4].copy()
print(str(copyList) + ' copy')

list1[4].clear()
print(str(list1) + '   clear')

# print(len(list1[4]))
# print(len(list1))
# print(list1[4][0])#test
#print(list1[0:3])


