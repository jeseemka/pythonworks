# Take input for the ages of three people
age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))

# Determine the oldest and youngest ages
oldest_age = max(age1, age2, age3)
youngest_age = min(age1, age2, age3)

# Display the results
print(f"The oldest person is {oldest_age} years old.")
print(f"The youngest person is {youngest_age} years old.")
