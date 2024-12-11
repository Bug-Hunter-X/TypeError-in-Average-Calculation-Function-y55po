def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = [1, 2, 'a', 4, 5]
average = calculate_average(my_list) #This will not cause TypeError
print(f"The average is: {average}") 