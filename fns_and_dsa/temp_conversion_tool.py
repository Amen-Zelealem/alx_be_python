# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    try:
        # Use the global conversion factor
        return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    except Exception as e:
        raise ValueError(f"Error during conversion: {e}")

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    try:
        # Use the global conversion factor
        return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    except Exception as e:
        raise ValueError(f"Error during conversion: {e}")

# User interaction
def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        # Validate that the input is numeric
        if not temp_input.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temp_input)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
