# Package Express Shipping Calculator
# Created by: Rachel Martinez
# Version: 2.0.0

# Display welcome screen
print("Welcome to Package Express. Please follow the instructions below.")

# Input package weight
weight_input = float(input("Please enter the package weight:\n"))

# Check maximum weight
if weight_input > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Input package dimensions
width_input = float(input("Please enter the package width:\n"))
height_input = float(input("Please enter the package height:\n"))
length_input = float(input("Please enter the package length:\n"))

# Calculate total size
total_size = width_input + height_input + length_input

# Check maximum size
if total_size > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Calculate shipping cost
# Formula: (width * height * length * weight) / 100
shipping_total = (width_input * height_input * length_input * weight_input) / 100

# Display shipping cost
print(f"Your estimated total for shipping this package is: ${shipping_total:.2f}")
print("Thank you!") 