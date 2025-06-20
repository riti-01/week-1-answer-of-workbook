def greet(name="Guest", greeting="Hello"):
    print(f"{greeting}, {name}!")

greet()                          # Uses default arguments
greet(name="Alice")              # Override only name
greet(greeting="Hi", name="Bob") # Override both using keywords
