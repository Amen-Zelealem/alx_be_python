def main():
    try:
        # Prompt the user for a number
        number = int(input("Enter a number to see its multiplication table: "))

        # Generate and print the multiplication table
        for i in range(1, 11):
            result = number * i
            print(f"{number} * {i} = {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Run the program
if __name__ == "__main__":
    main()
