def greet_person(name, greeting="hello"):
    message = f"{greeting},{name}"
    return message

default_greeting = greet_person("alice")
custom_greeting = greet_person("bob","hi")

print(default_greeting)
print(custom_greeting)