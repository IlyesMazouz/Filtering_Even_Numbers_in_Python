"""
a function that filters even numbers and appends them into a new list
"""
def filter_even_numbers(input_list):
    even_numbers = []

    for number in input_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

input_list = [3, 8, 12, 7, 4, 6, 9, 10]
even_numbers = filter_even_numbers(input_list)
print(even_numbers)
