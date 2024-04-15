print('Работа со списками:')
my_list = ['apple', 'orange', 'banana', 'cherry', 'pear', 'mango', 'kiwi']
print('Список:', my_list)
print('Первый и последний элементы списка:', my_list[0:7:6])
print('Подсписок c третьего по пятый элементы:', my_list[2:5])
my_list[2]= 'apricot'
print('Измененный список:', my_list)
print()  # отступ, так требует мой внутренний перфекционист =)
print('Работа со словарями:')
my_dict = {'apple': 'яблоко', 'orange': 'апельсин', 'banana': 'банан', 'cherry': 'вишня'}
print('Словарь:', my_dict)
print('Перевод:', my_dict['apple'])
my_dict['orange'] = 'мандарин'
print('Измененный словарь:', my_dict)
