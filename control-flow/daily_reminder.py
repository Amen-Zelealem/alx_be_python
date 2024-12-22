def main():
    # Prompt for task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Validate priority input
    match priority:
        case "high":
            message = f"'{task}' is a high priority task."
        case "medium":
            message = f"'{task}' is a medium priority task."
        case "low":
            message = f"'{task}' is a low priority task."
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            return

    # Add time-sensitivity to the message
    if time_bound == "yes":
        message += " It requires immediate attention today!"
    elif time_bound == "no":
        message += " Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound. Please enter yes or no.")
        return

    # Print the customized reminder
    print("Reminder:", message)


# Run the program
if __name__ == "__main__":
    main()
