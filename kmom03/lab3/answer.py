#!/usr/bin/env python3

"""
ac34781bd3ced108abccf2700c88045f
python
lab3
v4
noka21
2021-09-29 19:07:30
v4.0.0 (2019-03-05)

Generated 2021-09-29 21:07:30 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb
import functions


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()


# ==========================================================================
# Lab 3 - python
#
# In this lab we take another look at functions and we use modules to
# structure our code.
#


# --------------------------------------------------------------------------
# Section 1. Functions
#
#
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a function `valid_password` that takes one string argument. Check
# whether the argument is a valid password according to the following rules:
#
# * 8 characters or longer
# * Contains upper and lowercase letters
# * Contains a number
#
# The function should return True or False depending on whether the password
# is valid.
#
# Answer with the return value of the function when called with the string
# 'mYsecretPASSW0rd'.
#
# Tip: Use built-in character functions `isupper()`, `islower()`,
# `isdigit()`.
#
# Write your code below and put the answer into the variable ANSWER.
#
def valid_password(password):
    """
    function check validpassword
    """

    return (not password.isdigit() and not password.isalpha() and
     not password.isupper() and not password.islower() and len(password) >= 8)


ANSWER = valid_password("mYsecretPASSW0rd")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Using the function `valid_password` answer with the return value of the
# function when called with the string 'mYsecretpassword'.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = valid_password("mYsecretpassword")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a function `number_of_vowels` that takes one argument. The function
# returns the number of vowels (vokaler) in the given argument. The following
# letters is used as vowels in this exercise: aeiouy. Your solution should be
# case-insensitive.
#
# Answer with the number of vowels in the following text:
#
# 'How brief our moment of life is. How to be steadfast, and strong, and in control of yourself.'
#
# Write your code below and put the answer into the variable ANSWER.
#


def number_of_vowels(text):
    """
    returns the number of vowels
    """
    count = 0
    for vowel in text:
        if vowel in ('a', 'e', 'i', 'o', 'u', 'y'):
            count += 1
    return count


ANSWER = number_of_vowels(
    'How brief our moment of life is. How to be steadfast, and strong, and in control of yourself.')

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a function `analyze_password` that uses `valid_password` and
# `number_of_vowels`. The function should return whether or not a password is
# valid and how many vowels the given password contains concatenated to a
# string.
#
# Example: With the input value Se3ret the function should return the
# following string: 'Se3ret is not a valid password and contains 2 vowels.'.
#
# With the input value mYsecretPASSW0rd the function should return the
# following string: 'mYsecretPASSW0rd is a valid password and contains 4
# vowels.'.
#
# Answer with the return value of the function `analyze_password` called with
# the following argument: mYsecretpassw0rd.
#
# Write your code below and put the answer into the variable ANSWER.
#


def analyze_password(password_an):
    """
    analyze password
    """
    if valid_password(password_an) :
        return f"{password_an} is a valid password and contains {number_of_vowels(password_an.lower())} vowels."
    return False


ANSWER = analyze_password("mYsecretpassw0rd")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Modules
#
# In this section we will look into modules and how we can structure our
# code.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a new Python file called `functions.py`. Import your new file/module
# in `answer.py` using the import statement: `import functions`
#
# In your new module, create a function called `multiplication` that takes
# two arguments. The function should return the product of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 82 and 7.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = functions.multiplication(82, 7)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# In your new module, create a function called `funny_word` that takes one
# argument and prepends it to the string ' is a funny word'. **EXAMPLE:** If
# the argument is 'water', the function should return: `"water is a funny
# word"`.
#
# Use the argument 'vacation' and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = functions.funny_word("vacation")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# In your new module, create a function called `decider`. The function takes
# one argument. If the argument is a string return a call to `funny_word()`,
# if the argument is an integer return the square of the argument by using
# the `multiplication` function.
#
# Answer with a call to the function `decider` with the value `90` as
# argument.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = functions.decider("90")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# In your new module, create a function called `double_decider`. The function
# takes two arguments. For each argument call the `decider` function.
# Concatenate the returned values in a string.
#
# Separate the two values by ' and the square is '.
#
# Answer with a call to the function `double_decider` with the values:
# blunderbuss and 90 as arguments.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = functions.double_decider("blunderbuss","90")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)


dbwebb.exit_with_summary()
