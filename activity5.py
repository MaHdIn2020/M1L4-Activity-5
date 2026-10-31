# Python program to check if a number is an Armstrong number
# Take input from the user
num = int(input("Enter a number: "))

# Count the number of digits
num_digits = len(str(num))

# Calculate sum of each digit raised to the power of num_digits
sum_of_powers = sum(int(digit) ** num_digits for digit in str(num))

# Check if the sum equals the original number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
