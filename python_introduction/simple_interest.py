# Assign specific values to the variables
principal = 1000  # Representing $1000
rate = 0.05  # Representing 5% Annual Interest
time = 3  # Representing 3 Years

# Calculate the Simple interst using the Formula (I = P * R * T)
interest = principal * rate * time

# Check functionality to verify the calculation
expected_interest = 150.0  # Manually calculated expected value

#  Print the Sample interst
print(f"The simple interest is: {interest} ")


# Verify the result
if interest == expected_interest:
    print(f"The simple interest is: {interest} (Calculation is correct)")
else:
    print(f"The simple interest is: {interest} (Calculation is incorrect)")
    print(f"Expected interest: {expected_interest}")
