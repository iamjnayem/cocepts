me = ["nayem", ["deshi", "software engineer"]]
other = me.copy()
other[0] = "x"


print(me)
print(other)

me[1][0] = "inosys"

print("check the problem")
print("company name for both has changed")
print(me)
print(other)

print("This is the problem of shallow copy")

