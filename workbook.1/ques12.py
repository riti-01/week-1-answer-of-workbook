list1 = [1, 2, 3]
list2 = list1           # Reference copy, same object
list3 = [1, 2, 3]        # New object with same values
print("ID of list1:", id(list1))
print("ID of list2:", id(list2))
print("ID of list3:", id(list3))
print("list1 == list2 by ID?", id(list1) == id(list2))  # True
print("list1 == list3 by ID?", id(list1) == id(list3))  # False