s = "hello"
n = 100
print("Original ID of s:", id(s))
print("Original ID of n:", id(n))

# Reassign
s = "world"
n = 200
print("New ID of s:", id(s))
print("New ID of n:", id(n))
# IDs change on reassignment since strings and integers are immutable