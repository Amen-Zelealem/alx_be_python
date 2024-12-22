def main():
    try:
        # Prompt the user for the size of the pattern
        size = int(input("Enter the size of the pattern: "))

        if size <= 0:
            print("Please enter a positive integer.")
            return

        # Draw the pattern using nested loops
        row = 0
        while row < size:
            for _ in range(size):
                print("*", end="")
            print()  # Move to the next row
            row += 1

    except ValueError:
        print("Invalid input. Please enter a positive integer.")


# Run the program
if __name__ == "__main__":
    main()
