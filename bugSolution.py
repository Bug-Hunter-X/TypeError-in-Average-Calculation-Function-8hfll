def calculate_average(numbers):
    if not numbers:
        return 0
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers")
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"Average: {result}")

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"Average: {result}")

my_list = [1, 2, 3, 4, 'a']
result = calculate_average(my_list) # This will raise ValueError
print(f"Average: {result}") 