# Ask the user for the quantity
quantity = int(input("Enter the quantity: "))

# Define the cost per unit
cost_per_unit = 100

# Calculate the total cost
total_cost = quantity * cost_per_unit

# Check if the total cost is more than 1000 and apply the discount
if total_cost > 1000:
    discount = 0.10 * total_cost
    total_cost -= discount

# Print the total cost for the user
print("Total cost: $", total_cost)
