a = 256
b = 256
print("ID of a (256):", id(a))
print("ID of b (256):", id(b))

c = 257
d = 257
print("ID of c (257):", id(c))
print("ID of d (257):", id(d))
# Explanation: Python caches small integers (-5 to 256), so IDs for 256 are same. Larger integers like 257 are not cached, so IDs differ.