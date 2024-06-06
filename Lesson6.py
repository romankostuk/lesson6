my_dict = {'Iphone': 100000, 'Samsung': 50000, 'Xiaomi': 30000, 'Honer': 25000}
print(my_dict)
print(my_dict['Samsung'])
my_dict['Nokia'] = 2500
my_dict.update({'Simens': 2500,
                'Motorolla': 60000})
del my_dict['Iphone']
print(my_dict)
# 2 часть задания:
my_set = {1, 2, 3, 1, 2, 3, 'a', 'b', 'c', 'a', 'b', 'd'}
print(my_set)
print(my_set.add(5))
print(my_set)
print(my_set.add(6))
print(my_set)
print(my_set.discard(3))
print(my_set)