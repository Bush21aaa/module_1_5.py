immutable_var = 1, 2, 3, 'Urban', True
print(immutable_var)
#значения элементов кортежа нельзя изменить, потому что они сохраняются как единое целое, а не список
mutable_list = ['fly', 'buy', 13, 11]
print(mutable_list)
mutable_list[1] = 2024
print(mutable_list)
mutable_list[-2] = 888
print(mutable_list)
mutable_list.append('end')
print(mutable_list)
mutable_list.remove(2024)
print(mutable_list)