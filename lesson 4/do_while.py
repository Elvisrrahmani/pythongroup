while True:
    user_input = input("enter a positive number:")

    if user_input.isnumeric():
        number = int(user_input)
        if number > 0:
            break

    print("invalid input.try again")

print("you enter a valid positive number:", number)