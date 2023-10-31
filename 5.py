def remove_duplicates(input_list):
    result = []
    for item in input_list:
        if item not in result:
            result.append(item)
    return result
# Example usage:
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(my_list)
print(unique_list)
