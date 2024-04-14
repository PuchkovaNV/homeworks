immutable_var = [1, 2, 3, 4], 5, 6, 7, 'Red', True
print(immutable_var)

#immutable_var[1] = 200  # Кортеж так же, как и список, является коллекцией, но в отличие от него он неизменяем

mutable_list = [5, 6, 7, 'apple', 'coconut']
print(mutable_list)

mutable_list[0] = 25
mutable_list[3] = 'cherry'
print(mutable_list)
