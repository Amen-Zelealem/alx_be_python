def main():
    try:
        # Prompt the user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Ask the user to choose an operation
        operation = input("Choose the operation (+, -, *, /): ").strip()

        # Perform the calculation using a match-case statement
        match operation:
            case "+":
                result = num1 + num2
                print(f"The result is {result}.")
            case "-":
                result = num1 - num2
                print(f"The result is {result}.")
            case "*":
                result = num1 * num2
                print(f"The result is {result}.")
            case "/":
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"The result is {result}.")
            case _:
                print("Invalid operation. Please choose from +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


# Run the program
if __name__ == "__main__":
    main()
