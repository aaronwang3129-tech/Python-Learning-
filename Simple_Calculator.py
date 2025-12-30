print("Welcome to the Simple Calculator!")
while True:
    operation = input("Type the operation symbol you want to use:"
                      " (Addition: +) "
                      " (Subtraction: -)"
                      " (Multiplication: *)"
                      " (Division: /) ")
    first_number = input("Type the first number you want to use:")
    second_number = input("Type the second number you want to use:")
    if operation == "exit":
        print("Thanks for using the Simple Calculator!")
        break
    elif operation == "+":
        addition = float(first_number) + float(second_number)
        print("Your answer is: " + str(addition))
        print("Type 'exit' to exit the Simple Calculator")
    elif operation == "-":
        subtraction = float(first_number) - float(second_number)
        print("Your answer is: " + str(subtraction))
        print("Type 'exit' to exit the Simple Calculator")
    elif operation == "*":
        multiplication = float(first_number) * float(second_number)
        print("Your answer is: " + str(multiplication))
        print("Type 'exit' to exit the Simple Calculator")
    elif operation == "/":
        division = float(first_number) / float(second_number)
        print("Your answer is: " + str(division))
        print("Type 'exit' to exit the Simple Calculator")
    else:
        print("Please type a valid operation")
