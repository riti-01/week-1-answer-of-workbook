def average(*args):
    if not args:
        return 0  # Avoid division by zero
    return sum(args) / len(args)

# Example usage
print("Average is:", average(10, 20, 30))
