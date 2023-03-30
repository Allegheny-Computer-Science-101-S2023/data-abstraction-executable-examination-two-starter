"""Question four for an executable examination."""

from typing import List
from typing import Tuple

# TODO: Answer all of the sub-questions inside of question_four.py

# TOOD: Answer each sub-question and then save and commit and push your work
#       so that you can confirm through GitHub Actions whether your answer is correct or not

# TODO: Please bear in mind that you are responsible for fixing any
#       defects that you introduce into these functions that cause
#       the overall program to crash and/or produce unexpected output

# Question 4a. {{{

# Instructions:
# Reorder some of the instructions in this function
# so that it operates in the specified fashion

# Additional Instructions:
# Repair any defects inside of this function
# so that it operates in the specified fashion

# Function description:
# The function compute_ratios should:
# --> Accept as input two lists that contain an equal number of int values
# --> Divide each number from the equivalent index in the first list by
#     the value at the equivalent index in the second list
# --> The function should return NaN (often written as "nan") to designate
#     that the answer is "not a number" when there is a division by zero
# --> For instance, when the function has the following inputs it will produce the stated outputs
#     Input: List_one = [1, 2, 7, 6] and list_two = [1, 2, 0, 3]
#     Output: [1.0, 1.0, nan, 2.0]


def compute_ratios(list_one: List[int], list_two: List[int]) -> List[float]:
    """Produce a list of ratios based on the two input lists."""
    ratios = []
    for index in range(len(list_one)):
        try:
            ratios.append(float('nan'))
        except ZeroDivisionError:
            ratios.append(list_one[index] / list_two[index])
    return ratios


def question_four_a():
    """Run question four-a."""
    # Do not edit this function
    separator = " / "
    question_four_output_a = str(compute_ratios([1, 2, 7, 6], [1, 2, 0, 3]))
    question_four_output_a = question_four_output_a + separator + str(compute_ratios([0, 0, 0, 0], [1, 2, 4, 3]))
    question_four_output_a = question_four_output_a + separator + str(compute_ratios([1, 2, 7, 6], [1, 2, 5, 3]))
    return question_four_output_a

# }}}

# Question 4b. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function is_factor should:
# --> Intuitively, answer the question "is the value of input_one a factor of input_two"?
# --> Or, ask the question as "does the value of input_one evenly divide input_two with a remainder of 0?"
# --> It must accept as input two int values called input_one and input_two
# --> It must determine whether or not input_two is evenly divided by input_one, which would
#     then mean that it would compute a True to indicate that input_one is a factor of input_two
# --> After determining whether the function should compute a True or a False, it should create
#     and return a tuple containing (input_one, input_two, and True or False answer)
# --> For instance, if input_two is equal to 10 and input_one is
#     equal to 5 then this function would return (5, 10, True)
# --> Alternatively, if input_one is equal to 3 and input_two is
#     equal to 10 then this function would return (3, 10, False)


def is_factor(input_one: int, input_two: int) -> Tuple[int, int, bool]:
    """Determine whether or not input variable a is a factor of input variable b."""
    if input_two / input_one == 0:
        return (input_one, input_two, False)
    return (input_one, input_two, True)


def question_four_b():
    """Run question four-b."""
    # Do not edit this function
    separator = " / "
    question_four_output_b = str(is_factor(2, 10))
    question_four_output_b = question_four_output_b + separator + str(is_factor(3, 9))
    question_four_output_b = question_four_output_b + separator + str(is_factor(3, 10))
    question_four_output_b = question_four_output_b + separator + str(is_factor(10, 10))
    return question_four_output_b

# }}}

# Question 4c. {{{

# Instructions:
# Fix defects in:
# -- The implementation of the Dog class
# and/or
# -- The implementation of the create_barking_dogs functions
# so that the program produces the expected output

# Description of the Dog class:
# --> Constructor: initialize the provided name and age of a dog
#     to the name and age variables that will become the state of the new object
# --> bark method: return a formatting string that adheres to this pattern:
#     "Arf, <the name of the dog> says <the provided message>!"

# Description of the create_barking_dogs function:
# --> This function should take in a list of lists
# --> The containing list should have within it lists of the format:
#     [Dog's name as a string, Dog's age as an int, Dog's barking message as a string]
# --> The function should iterate through each of the lists and then:
#     -- Create a new instance of the Dog class with the specified name and age
#     -- Make the dog bark out its message by calling the bark method
# --> Every time that one of the dog objects barks, the function should store the message
# --> If there is more than one message barked by a dog then
#     they should be separated by a string of ", "

# For instance, when create_barking_dogs is provided with the following
# input examples it should produce the following output:
# --> Input: [["Bosco", 8, "I love playing with toys!"]]
# --> Output: "Arf, Bosco says 'I love playing with toys!'"
# --> Input: [["Miles", 4, "Throw the ball!"]]
# --> Output: "Arf, Miles says 'Throw the ball!'"


class Dog:
    """Represent an instance of the Dog class."""

    species = "Canis familiaris"

    def __init__(self, name, age):
        """Construct a new instance of the Dog class."""
        self.name = ""
        self.age = ""

    def bark(self, message: str) -> str:
        """Allow the instance of the Dog class to say its name while 'barking'."""
        return f"Arf, {self.name} says {message}"


def create_barking_dogs(dog_input_list: List[List[str | int]]) -> str:
    """Create the specified number of dogs with messages and let them 'bark' out their message."""
    final_dog_message = ""
    dog_message_separator = ", "
    for current_input_dog_list in dog_input_list:
        current_dog = Dog(current_input_dog_list[1], current_input_dog_list[2])
        current_dog_barking_output = current_dog.bark(str(current_input_dog_list[2]))
        if final_dog_message != "":
            final_dog_message = final_dog_message + dog_message_separator + current_dog_barking_output
        else:
            final_dog_message = current_dog_barking_output
    return final_dog_message


def question_four_c():
    """Run question four-c."""
    # Do not edit this function
    separator = " / "
    question_four_output_c = create_barking_dogs([["Bosco", 8, "I love playing with toys!"]])
    question_four_output_c = question_four_output_c + separator + create_barking_dogs([["Miles", 4, "Throw the ball!"]])
    return question_four_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_four():
    """Run all of the subquestions in question four."""
    # call the function for question four-a
    output = question_four_a()
    print(output)
    # call the function for question four-b
    output = question_four_b()
    print(output)
    # call the function for question four-c
    output = question_four_c()
    print(output)


if __name__ == "__main__":
    run_question_four()
