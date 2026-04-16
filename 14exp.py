while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = a / b
        print("Result =", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    except ValueError:
        print("Error: Invalid input (enter numbers only)")

    again = input("Do you want to continue? (y/n): ")
    if again.lower() != 'y':
        print("Program ended")
        break