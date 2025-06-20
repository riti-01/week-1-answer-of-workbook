def outer():
    x = 10
    def inner():
        print("Value of x from outer():", x)
    inner()

outer()
