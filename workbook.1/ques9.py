a = 'hello'
b = 'hello'
c = 'HELLO'
print("ID of a:", id(a))
print("ID of b:", id(b))
print("ID of c:", id(c))
# a and b will likely have the same ID (string interning), c will have a different one due to different content.