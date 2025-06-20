list1 = eval(input("Enter the first list (e.g., [1, 2, 3]): "))
list2 = eval(input("Enter the second list (e.g., [1, 2, 3]): "))
print("ID of list1:", id(list1))
print("ID of list2:", id(list2))
print("IDs are same?", id(list1) == id(list2))
# Even with same values, different list objects have different IDs.
