# Словари
my_dict = {'Alex': 1986, 'Egor': 1985, 'Eugene': 1988}
print('Dict:', my_dict)
print('Existing value:', my_dict['Alex'])
print('Not existing value:', my_dict.get('Gross'))
my_dict.update({'Boris': 2001,
                'Tanya': 2003})
deleted_value = my_dict.pop('Eugene')
print('Deleted value:', deleted_value)
print('Modified dictionary:', my_dict)
# Множества
my_set = {1, 2, 3, 'String', True, 1.1, False, 3, 2, 1, 'String', (5,6,7)}
print('Set:', my_set)
my_set.add(9)
my_set.add(2.2)
my_set.remove(False)
print('Modified set:', my_set)