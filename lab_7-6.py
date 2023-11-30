"""
Create a Python file named lab_7-6.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a 2 separate functions within the same document. 
Create a 3rd function which requires both the first two functions within it
Create 4 test cases for your 3rd function. 
"""
#adding two numbers
def add_numbers(a, b):
    return a + b

#suntracting two numbers
def subtract_numbers(a, b):
    return a - b

#combining both functions together
def combine_operations(x, y, z):
    result_add = add_numbers(x, y)
    result_multiply = subtract_numbers(result_add, z)
    return result_multiply


# even numbers
test_result_1 = combine_operations(2, 6, 8)
print(f"Test Case 1 Result: {test_result_1}")

# odd numbers
test_result_2 = combine_operations(5, 9, 3)
print(f"Test Case 2 Result: {test_result_2}")

# negative numbers
test_result_3 = combine_operations(-1, -3, -9)
print(f"Test Case 3 Result: {test_result_3}")

# negative and posituve
test_result_4 = combine_operations(-8, -5, 2)
print(f"Test Case 4 Result: {test_result_4}")