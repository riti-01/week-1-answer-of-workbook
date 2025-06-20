a = (1, 2, 3)
b = (1, 2, 3)
print("ID of tuple a:", id(a))
print("ID of tuple b:", id(b))
print("IDs are same?", id(a) == id(b))
# Tuples with same immutable content may have same ID due to interning