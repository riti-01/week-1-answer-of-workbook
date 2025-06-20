def average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

print("Average:", average(4, 8, 15, 16, 23, 42))
print("Average with no input:", average())
