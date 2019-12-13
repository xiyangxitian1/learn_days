import copy

a = (1, 2, [1, 2, ])
print(id(a[0]))
b = a
print(id(b[0]))
c = copy.deepcopy(b)
print(id(c[0]))
