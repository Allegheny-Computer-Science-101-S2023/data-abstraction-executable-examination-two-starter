"""Question three for an executable examination."""

from pathlib import Path
from typing import Dict
from typing import List
from typing import Tuple

# TODO: Answer all of the questions inside of question_three.py

# TOOD: Answer each question and then save and commit and push your work
#       so that you can confirm through GitHub Actions whether your answer is correct or not

# TODO: Please bear in mind that you are responsible for fixing any
#       defects that you introduce into these functions that cause
#       the overall program to crash and/or produce unexpected output

# Question 3a. {{{

# Instructions:
# Implement all of the source code lines in this function
# so that it operates in the specified fashion

# Function description:
# The function input_file should:
# --> Accept as input a file_name that is of type string
# --> Assume that the program that runs the function will
#     be executed from the root of the GitHub repository;
#     as in "python source/question_three.py"
# --> Construct a pathlib Path object and then read in the
#     values from the file and store them as strings in a list
# --> Return a list of strings containing all of the values
#     that were stored inside of the file
# --> For instance, the inputs/observations.txt file contains these values:
#     5
#     7
#     9
#     11
#
#     This means that it would cause this function to produce the output:
#     ['5', '7', '9', '11']


def input_file(file_name: str) -> List[str]:
    """Use a pathlib Path object to read and return the contents of the specified file."""
    return ["None"]


def question_three_a():
    """Run question three-a."""
    # Do not edit this function
    question_three_output_a = input_file("inputs/observations.txt")
    return question_three_output_a

# }}}

# Question 3b. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function convert_list_to_paired_dictionary should:
# --> Accept as input a variable called input_list that is a list of strings
# --> Use a for loop or a while loop to iterate through each element in the input_list
# --> Convert each value in the input_list from a string to an int
# --> Return a dictionary (i.e., a dict) that maps the string value to the int value
# --> For instance, when the function receives the input ['5', '7', '9', '11']
#     if will produce the output {'5': 5, '7': 7, '9': 9, '11': 11}


def convert_list_to_paired_dictionary(input_list: List[str]) -> Dict[str, int]:
    """Convert a list of strings to a dictionary that maps the strings to their int values."""
    output_dict_for_pairing: Dict[str, int] = {"0": 0}
    for input_value in input_list:
        input_value_int = float(input_value)
        output_dict_for_pairing[input_value] = input_value_int
    return output_dict_for_pairing


def question_three_b():
    """Run question three-b."""
    # Do not edit this function
    separator = " / "
    question_three_output_b = str(convert_list_to_paired_dictionary(['5', '7', '9', '11']))
    question_three_output_b = question_three_output_b + separator + str(convert_list_to_paired_dictionary(['1', '2', '3', '4']))
    return question_three_output_b

# }}}

# Question 3c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function sum_list should:
# --> Accept as input a tuple of four int values
# --> Compute the sum of all of the int values in the tuple
# --> Return the sum of all the int values in the tuple
# --> For instance, if the function receives (5, 7, 9, 11) as
#     an input it returns the dictionary that contains {(5, 7, 9, 11): 32}
# Note that this function is not required to handle any other inputs than
# a tuple that contains four int values


def sum_list(input_list: Tuple[int, int, int, int]) -> Dict[Tuple[int, ...], int]:
    """Sum all of the values inside of a list of int values."""
    return {(0, ): 0}


def question_three_c():
    """Run question three-c."""
    # Do not edit this function
    separator = " / "
    question_three_output_c = str(sum_list((int(5), int(7), int(9), int(11))))
    question_three_output_c = question_three_output_c + separator + str(sum_list((int(1), int(2), int(3), int(4))))
    return question_three_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_three():
    """Run all of the subquestions in question three."""
    # call the function for question three-a
    output = question_three_a()
    print(output)
    # call the function for question three-b
    output = question_three_b()
    print(output)
    # call the function for question three-c
    output = question_three_c()
    print(output)


if __name__ == "__main__":
    run_question_three()
