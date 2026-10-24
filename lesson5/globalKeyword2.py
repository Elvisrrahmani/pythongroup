greeting = "hello"
name = "bob"

def greet():
    global greeting
    greeting = "goodbye"

    name = "alice"

    message = f"{greeting},{name}!"
    print(message)

greet()

print(greeting)
print(name)