#!/usr/bin/env python3

"""
ac77598a59e59639199957b0af03b664
python
lab1
v4
noka21
2021-09-01 19:26:33
v4.0.0 (2019-03-05)

Generated 2021-09-01 21:26:33 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()


# ==========================================================================
# Lab 1 - python
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python manual](https://docs.python.org/3/library/index.html).
#
# There you will find everything this lab will go through and much more.
#


# --------------------------------------------------------------------------
# Section 1. Integers, floats and basic arithmetics
#
# The foundation of numbers and basic arithmetic.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a variable called `num_one` and give it the value 25.
#
# Answer with the value of `num_one`.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_one = 25


ANSWER = num_one

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create another variable called `num_two` and give it the value 72. Create a
# third variable called `result` and assign to it the sum of the first two
# variables.
#
# Answer with the `result` variable.
#
# Write your code below and put the answer into the variable ANSWER.
#
num_two = 72
result = num_one + num_two


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a variable called `num_three` and give it the value 94.
#
# Create another variable called `num_four` and give it the value 60.
#
# Subtract `num_three` from `num_four` and add the `result` variable from
# above to result of the subtraction. Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#
num_three = 94
num_four = 60


ANSWER = (num_four - num_three) + result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Answer with the result of a multiplication of `num_one` and `num_three`.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = num_one * num_three

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a variable called `float_one` and give it the value 22.35.
#
# Create another variable called `float_two` and give it the value 32.96.
#
# Sum the two values and answer with the result, rounded to two decimals. Use
# the function `round()` to round the number to two decimals.
#
# Write your code below and put the answer into the variable ANSWER.
#
float_one = 22.35
float_two = 32.96
result5 = float_two + float_one


ANSWER = round(result5, 2)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# All variables used in the exercise below are defined above.
#
# Sum `num_three` with `num_one` and subtract `num_four`. Multiply the result
# by `num_two`, add `float_two` and subtract `float_one`. Use the function
# `round()` to round the number to two decimals.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#
result6 = ((num_three + num_one - num_four) * num_two) + float_two - float_one

ANSWER = round(result6, 2)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Strings and concatenation
#
#
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Concatenate (svenska: konkatenera) the two words 'print' and 'resort' and
# answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#
print_word = "print"
resort_word = "resort"

ANSWER = print_word + resort_word

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Concatenate the word 'resort' with the integer 25, with a space between the
# two values.
# Answer with the new string.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = resort_word + " " + str(num_one)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Concatenate the integer 25 with the word 'print' with a space between. To
# the resulting string concatenate the string ' and '. To this string
# concatenate integer 72 and the word 'resort' with a space between between
# the two variables.
#
# Write your code below and put the answer into the variable ANSWER.
#
and_word = " and "

ANSWER = (str(num_one) + " " + print_word) + \
    and_word + str(num_two) + " " + resort_word

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Assign the string value '30' to a variable called `string_number` and
# assign the integer value 5 to a variable called `actual_number`.
#
# Use `int()` to change the type of `string_number` to an integer and divide
# the integer value with `actual_number`. Answer with an integer by using the
# function `round()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

string_number = "30"
actual_number = 5
division_result = int(string_number)/actual_number
ANSWER = round(division_result)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# BTH is using a wind-turbine and solar panels to harvest energy from the
# wind and sun. On a windy and sunny day in September the sun shines for 10
# hours with an average output effect of the solar panels of 9345 W per hour.
# The wind turbine has an average output effect of 314 W per hour for all 24
# hours of the day.
#
# Calculate the total output energy i kWh from the wind turbine and the solar
# panels for the entire day.
#
# Energy i kWh is calculated as `energy = effect * hours / 1000`.
#
# Write your code below and put the answer into the variable ANSWER.
#
sun_energy = 9345 * 10/1000
wind_energy = 314*24/1000
sun_and_wind_energy = sun_energy + wind_energy
ANSWER = float(sun_and_wind_energy)
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Peter has the phonenumber '0731415926' and Anna has the phonenumber
# '0727182818'. They call each other every sunday afternoon for 9 minutes.
#
# Calculate the number of hours that they talk with each other pr year
# (assume 52 sundays pr year). Use that number in a string concatenation with
# the following format:
#
# 'Peter calls from [#Peter's phonenumber] to Anna on [#Anna's phonenumber]
# for [#hours] hours every year.'
#
# Replace the content inside [#] with the corresponding values.
#
# Answer with the concatenated string.
#
# Write your code below and put the answer into the variable ANSWER.
#
Peter_phonenumber = "0731415926"
Anna_phonenumber = "0727182818"
year_hours = 9*52/60


ANSWER = "Peter calls from " + Peter_phonenumber + " to Anna on " + \
    Anna_phonenumber + " for " + str(year_hours) + " hours every year."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
