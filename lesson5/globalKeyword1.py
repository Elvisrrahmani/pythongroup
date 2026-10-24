greeting = "hello"

def greet(name):
    global message

    message = f"{greeting},{name}!"

    print(message)

greet("bob")
print(message)
