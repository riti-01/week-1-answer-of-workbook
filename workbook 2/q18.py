counter = 0  # global variable

def increment():
    global counter
    counter += 1
    print("Counter:", counter)

increment()
increment()
