user_input = input("Enter Your input: ")

if user_input.isalnum():
    if user_input.isalpha():
        print('You Enterad are letters')
        if user_input.islower():
            print("letters is lower")
        elif user_input.isupper():
            print('letters is Upper')
        else:
            print("letters is neither lower and upper")
    elif user_input.isnumeric():
        print("You Entered a numbers")
    else:
        print("There is a mix between letters and numbers.")
else:
    print("Invalid input. Please enter a string.")
    