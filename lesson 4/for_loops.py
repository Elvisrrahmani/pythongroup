#create a list of names

names = ["alice","bob","charlie","david"]

for name in names:
    print(name)

    ###########################

sentence = "Hello, world!"

for character in sentence:
    if character.isalpha():
        print(character)

    ######################################################

for number in range(1,6):
    print(number)


    ###########################
numbers = [12,45,6,72,21,8,94,57]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
print("the maximum value in the list is",maximum)

######################################################

numbers = [12,45,6,72,21,8,94,57]

maximum = numbers[0]

for num in numbers:
    if num < maximum:
        maximum = num
print("the minimum value in the list is",maximum)


