def find_duplicates(numbers):
    repeated_numbers = []
    
    for number in numbers:
        if numbers.count(number) > 1 and number not in repeated_numbers:
            repeated_numbers.append(number)
    
    return repeated_numbers

# Example usage
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
duplicates = find_duplicates(my_list)
print("Repeated numbers in the list:", duplicates)
