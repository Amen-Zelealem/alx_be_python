FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Function to validate and convert temperature input
def validate_temperature(temp_input):
    try:
        return float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Function to validate unit input
def validate_unit(unit_input):
    unit = unit_input.strip().upper()
    if unit not in {"C", "F"}:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    return unit

# Main function for user interaction
def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = validate_temperature(temp_input)

        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        unit = validate_unit(unit_input)

        if unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        elif unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
