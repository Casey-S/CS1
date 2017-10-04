

def fizzbuzz():

    user_number = input("Enter a number: ")

    if user_number % 3 == 0:
        print("fizz")
    if user_number % 5 == 0:
        print("buzz")
    if user_number % 3 != 0 and user_number % 5 != 0:
        print(user_number)


fizzbuzz()
