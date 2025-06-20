def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print("Inner count:", count)
    inner()
    inner()

outer()
