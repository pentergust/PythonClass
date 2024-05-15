# Метод split можно вызвать вообще без аргументов или с одним аргументомстрокой. 
# В первом случае строка разбивается на части, разделённые любыми
# символами пустого пространства (набором пробелов, символом табуляции и т. д.).
# Во втором случае разделителем слов считается строка-аргумент. Из
# получившихся слов формируется список.
s = 'раз    два     три'
print(s.split()) #['раз', 'два', 'три']
print(' one two three '.split()) # ['one', 'two', 'three']
print('192.168.1.1'.split('.')) # ['192', '168', '1', '1'] 
print(s.split('а')) # ['р', 'з дв', ' три']
print('A##B##C'.split('##')) # ['A', 'B', 'C']
print('A##B##C'.split('#')) # ['A', '', 'B', '', 'C']
print(s.split(' ')) #['раз', '', '', '', 'два', '', '', '', '', 'три']