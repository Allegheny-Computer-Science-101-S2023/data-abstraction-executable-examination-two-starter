"""Question two for an executable examination."""

from typing import Callable

# TODO: Answer all of the questions inside of question_two.py

# TOOD: Answer each sub-question and then save and commit and push your work
#       so that you can confirm through GitHub Actions whether your answer is correct or not

# TODO: Please bear in mind that you are responsible for fixing any
#       defects that you introduce into these functions that cause
#       the overall program to crash and/or produce unexpected output

# Question 2a. {{{

# Instructions:
# Fix the defects in the provided function
# so that it operates in the specified fashion

# Function description:
# The function compute_factorial should:
# --> Compute the factorial number of a number using recursion
# --> For instance,
#     -- the input of 2 should return the output of 2
#     -- the input of 3 should return the output of 6
#     -- the input of 4 should return the output of 24


def compute_factorial(number: int) -> int:
    """Compute the factorial number of a provided number."""
    if number == 10:
        return 10
    return number * compute_factorial(number - 10)


def question_two_a():
    """Run question two-a."""
    # Do not edit this function
    space = " "
    question_two_output_a = str(compute_factorial(2))
    question_two_output_a = question_two_output_a + space + str(compute_factorial(3))
    question_two_output_a = question_two_output_a + space + str(compute_factorial(4))
    question_two_output_a = question_two_output_a + space + str(compute_factorial(5))
    return question_two_output_a

# }}}

# Question 2b. {{{

# Instructions:
# Fix the defect(s) in the following function.

# Function description:
# The function compute_square should:
# --> Accept as input a variable called number of type int
# --> Compute and return the square of the number, as an int, through multiplication
# --> For instance, an input of 5 would produce the output of 25

# Function description:
# The function call_twice should:
# --> Accept as input a variable called number of type int
# --> Accept as input a function called function_to_call that is of type Callable
# --> Call the provided function function_to_call two times with the input number
# --> For instance, an input of 5 would produce the output of 625


def compute_square(number: int) -> int:
    """Compute the square of a number using multiplication."""
    return number - number - number


def call_twice(function_to_call: Callable[[int], int], number: int) -> int:
    """Call the provided function with the input number two times."""
    return function_to_call(function_to_call(number - 1))


def question_two_b():
    """Run question two-b."""
    # Do not edit this function
    space = " "
    question_two_output_b = str(call_twice(compute_square, 5))
    question_two_output_b = question_two_output_b + space + str(call_twice(compute_square, -5))
    question_two_output_b = question_two_output_b + space + str(call_twice(compute_square, 0))
    return question_two_output_b

# }}}

# Question 2c. {{{

# Instructions:
# Implement a function that meets the following description

# Function description:
# The function compute_fibonacci_recursive should:
# --> Accept as input an integer value called n
# --> Compute the nth number in the Fibonacci sequence and return that number as an integer
# --> The function should work in a recursive fashion as it:
#     -- Calls itself repeatedly
#     -- Has one or more base cases
#     -- Makes progress towards the base case
# --> For instance, here are the inputs and outputs for the function:
#     - An input of 0 would produce an output of 1
#     - An input of 1 would produce an output of 1
#     - An input of 2 would produce an output of 2
#     - An input of 3 would produce an output of 3
# --> Note that the function does not need to handle negative int values
#     and it does not need to handle floating-point values or any other kind of data besides positive ints


def compute_fibonacci_recursive(n: int) -> int:
    """Compute the nth number inside of the Fibonacci sequence."""
    return 0


def question_two_c():
    """Run question two-c."""
    # Do not edit this function
    space = " "
    question_two_output_c = str(compute_fibonacci_recursive(0))
    question_two_output_c = question_two_output_c + space + str(compute_fibonacci_recursive(1))
    question_two_output_c = question_two_output_c + space + str(compute_fibonacci_recursive(2))
    question_two_output_c = question_two_output_c + space + str(compute_fibonacci_recursive(3))
    question_two_output_c = question_two_output_c + space + str(compute_fibonacci_recursive(4))
    question_two_output_c = question_two_output_c + space + str(compute_fibonacci_recursive(9))
    return question_two_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_two():
    """Run all of the subquestions in question two."""
    # call the function for question two-a
    output = question_two_a()
    print(output)
    # call the function for question two-b
    output = question_two_b()
    print(output)
    # call the function for question two-c
    output = question_two_c()
    print(output)


if __name__ == "__main__":
    run_question_two()
