colors1 = ["red", "blue"]
colors2 = colors1

print(colors1)
print(colors2)

print(id(colors1), id(colors2))


colors2 = "green"
print(id(colors2))
print(colors2)

help(list.copy)


my_list = [1, 2, 3]
your_list = my_list.copy()
print(id(my_list), id(your_list))


my_list = [1,2, 3, [4, 5, 6]]
your_list = my_list.copy()

print(id(my_list), id(your_list))

print("follow ids of sublist will be same")
print(id(my_list[3]), id(your_list[3]))

print("here actually comes of deep copy")