numbers = input("Enter numbers separated by spaces: ")
numbers = [int(n) for n in numbers.split()]
print("The maximum number is:", max(numbers))
