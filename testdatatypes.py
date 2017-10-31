a = [1, 2, 3]
b = [4, 5, 6]
c = a
d = list()
for i in range(2):
    d.append(a)
y = a + b
x = a * 2
z = [a, a]

print(b, c, d, y, x, z, a)

a[0] = 9

print(b, c, d, y, x, z, a)

a = [1]

print(b, c, d, y, x, z, a)


#print(dir(a))
#print(help(a.__ge__))

