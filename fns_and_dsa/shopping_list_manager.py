# shopping_list_manager.py

def display_menu():
    """Display the shopping list menu options."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to manage the shopping list."""
    shopping_list = []  # Initialize an empty shopping list

    while True:
        display_menu()  # Call display_menu function
        try:
            # Prompt user for a numeric input
            choice = int(input("Enter your choice (1-4): ").strip())

            if choice == 1:
                # Add an item to the shopping list
                item = input("Enter the name of the item to add: ").strip()
                if item:
                    shopping_list.append(item)
                    print(f"'{item}' has been added to the shopping list.")
                else:
                    print("Item name cannot be empty.")

            elif choice == 2:
                # Remove an item from the shopping list
                item = input("Enter the name of the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from the shopping list.")
                else:
                    print(f"'{item}' not found in the shopping list.")

            elif choice == 3:
                # View the shopping list
                print("\nCurrent Shopping List:")
                if shopping_list:
                    for idx, item in enumerate(shopping_list, start=1):
                        print(f"{idx}. {item}")
                else:
                    print("The shopping list is empty.")

            elif choice == 4:
                # Exit the program
                print("Goodbye!")
                break

            else:
                # Handle numbers outside the range 1-4
                print("Invalid choice. Please enter a number between 1 and 4.")

        except ValueError:
            # Handle non-numeric input for the choice
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
