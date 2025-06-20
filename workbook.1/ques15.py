a = 5.5
b = float(5.5)
print("ID of a (5.5):", id(a))
print("ID of b (float(5.5)):", id(b))
print("IDs are same?", id(a) == id(b))
# Typically, IDs will differ because float objects are not interned like small ints or strings