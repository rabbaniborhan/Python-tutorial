##Traditional Way (using a temporary variable)

a = 5
b = 10

temp = a
a = b
b = temp

print("a =", a)  # 10
print("b =", b)  # 5


##Pythonic Way (Tuple Unpacking)

a, b = b, a

print("a =", a)  # 10
print("b =", b)  # 5


##Swapping Using Arithmetic (Not recommended often)

a = a + b  # a = 15
b = a - b  # b = 5
a = a - b  # a = 10

print("a =", a)
print("b =", b)


x, y, z = 1, 2, 3
x, y, z = z, x, y  # rotate
print(x, y, z)      # 3 1 2
