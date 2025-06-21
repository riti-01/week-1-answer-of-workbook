# Store lambda functions in a dictionary
operations = {
    'square': lambda x: x * x,
    'cube': lambda x: x ** 3,
    'double': lambda x: x * 2
}

# Call the lambda function from the dictionary
number = 5
result = operations['square'](number)

# Print the result
print("The square of", number, "is:", result)
