x = 3
y = x

print("id of x and y: ")
print(id(x), id(y))

print("Right now they are pointing same memory location")


print("if we change the new location to y: ")

y = 4

print("Now value of x and y")
print("x =", x)
print("y =", y)

print("id of x and y: ")
print("x: ", id(x), "y: ", id(y))