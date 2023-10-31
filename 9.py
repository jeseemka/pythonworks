# Ask the user for their salary and years of service
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

# Check if the years of service are more than 5
if years_of_service > 5:
    # Calculate the bonus as 5% of the salary
    bonus = 0.05 * salary
    print(f"You are eligible for a 5% bonus. Your bonus amount is: ${bonus:.2f}")
else:
    print("Sorry, you are not eligible for a bonus.")

# Calculate and print the net bonus amount
