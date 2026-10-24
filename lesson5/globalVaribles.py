#define a global variable
gretting = "hello"

def greet(name):
    message = f"{gretting},{name}"
    print(message)

greet("bob")

print (gretting)