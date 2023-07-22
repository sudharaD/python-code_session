x = [12, 3, 4, 5, 6, 787, 8]
y = [0, 0, 0]
print(x)
# y = x[0]
# print(y)
x[0] = 21
print(x)
x.append(100)
print(x)
x.insert(1, 200)
print(x)
x.remove(200)
print(x)
x.pop(0)
print(x)
z = x + y
print(z)
print(not 10 in z)
print(10 in z)
