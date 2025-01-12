def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = input("Enter your choice: ")
            if choice == '1':
                # Prompt for and add an item
                item = input("Enter the item to add: ").strip()
                if item:
                    shopping_list.append(item)
                    print(f"'{item}' has been added to your list.")
                else:
                    print("Please enter a valid item.")
            elif choice == '2':
                # Prompt for and remove an item
                item = input("Enter the item to remove: ").strip()
                if not shopping_list:
                    print("The list is empty.")
                elif item not in shopping_list:
                    print(f"'{item}' is not in the shopping list.")
                else:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from your list.")
            elif choice == '3':
                # Display the shopping list
                if shopping_list:
                    print("Your Shopping List:")
                    for idx, item in enumerate(shopping_list, start=1):
                        print(f"{idx}. {item}")
                else:
                    print("The list is empty.")
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()