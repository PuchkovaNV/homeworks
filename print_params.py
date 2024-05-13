def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()  # не работает
print_params(5)  # не работает
print_params (b = 25)  # не работает
print_params(c = [1,2,3])  # не работает


values_list = [1, 'anton', True]
values_dict = {'a': 3, 'b': 'привет', 'c': False}

print_params(*values_list)
print_params(**values_dict)
values_list_2 = [7, 'hello']           
print_params(*values_list_2,42)  # работает

