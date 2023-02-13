from copy import deepcopy

me = ["nayem", ["deshi", "software engineer"]]

other = deepcopy(me)
other[0] = "x"
print(id(other), id(me))
print(me)
print(other)


other[1][0] = "brain station 23"

print(id(me[1]), id(other[1]))
print(me)
print(other)
