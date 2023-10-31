# Input two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Compare the two integers and find the greatest
if num1 > num2:
    print("The greatest integer is:", num1)
elif num2 > num1:
    print("The greatest integer is:", num2)
else:
    print("Both integers are equal.")
