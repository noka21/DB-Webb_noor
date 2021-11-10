#!/usr/bin/env python3

"""
cded89b46ff77e49bf5b455164680eb3
python
lab2
v4
noka21
2021-09-22 09:08:53
v4.0.0 (2019-03-05)

Generated 2021-09-22 11:08:53 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""


from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()


# ==========================================================================
# Lab 2 - python
#
# In this exercise we will look into flow-control. If-statements, for-loops
# and while-loops.
#


# --------------------------------------------------------------------------
# Section 1. Boolean operators and if-statements
#
# The basics of boolean operators and if-statements.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create three variables representing dice values: `dice1` = 5, `dice2` = 2
# and `dice3` = 4.
#
# Answer with the boolean value of the expression '`dice1` is greater than
# `dice2`'.
#
# Write your code below and put the answer into the variable ANSWER.
#
dice1 = 5
dice2 = 2
dice3 = 4


ANSWER = dice1 > dice2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Sum the three variables `dice1`, `dice2` and `dice3`.
#
# Use an if-statement to decide if the sum of the three variables i greater
# than 11. If the sum is greater than 11 answer with 'big' otherwise answer
# with 'small'.
#
# Write your code below and put the answer into the variable ANSWER.
#
sum_of_dice1_dice2_dice3 = dice1 + dice2 + dice3

if sum_of_dice1_dice2_dice3 > 11:
    ANSWER = "big"
else:
    ANSWER = "small"

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Add the sum of `dice4` = 3 and `dice5` = 5 to the sum of the three other
# dices.
#
# Use an if, elseif, else statement to check the total value of the dices.
# Answer with 'small' if the sum is smaller than 11, 'intermediate' if the
# sum is greater than or equal to 11 but smaller than 21. If the sum is
# greater than or equal to 21 answer with 'big'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice4 = 3
dice5 = 5
sum_of_dice4_dice5 = dice4 + dice5

if sum_of_dice1_dice2_dice3 + sum_of_dice4_dice5 < 11:
    ANSWER = "small"
elif 21 > sum_of_dice1_dice2_dice3 + sum_of_dice4_dice5 >= 11:
    ANSWER = "intermediate"
else:
    ANSWER = "big"

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a variable `summer_word` containing the word 'sunshine'.
#
# Answer with True if `summer_word` contains the letter 's' otherwise answer
# with False.
#
# Tip: Use the `in` operator.
#
# Write your code below and put the answer into the variable ANSWER.
#
summer_word = "sunshine"
ANSWER = "s" in summer_word

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# Section 2. For-loops
#
# The basics of iteration and for-loops.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Loop through the numbers 0 to 10 (10 included) and concatenate a string
# with the numbers comma-separated. You should have a comma at the end of the
# string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#
ANSWER = ""
for i in range(0, 11):
    ANSWER += str(i)+","

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Loop through the letters of the variable `summer_word` from above.
# Concatenate the consonants from `summer_word` and answer with the new word.
#
# Tip: Create a string that contains consonants and check if each letter is
# in it.
#
# Write your code below and put the answer into the variable ANSWER.
#
ANSWER = ""
for letter in summer_word:
    if letter in "snshn":
        ANSWER += letter



# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Loop through all numbers from 11 to 83 both numbers included. Add all odd
# (udda) numbers together and answer with the result.
#
# Tip: Use the modulus % operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = 0
for i in range(11, 84):
    if i % 2 == 1:
        ANSWER += i


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, True)

# --------------------------------------------------------------------------
# Section 3. While-loops
#
# The basics of while-loops.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (1 points)
#
# Create a while-loop that starts at value 5 and ends when the value is
# greater than 71, the value should be incremented by 3 for each iteration.
# Concatenate a string with the values comma-separated. You should have a
# comma at the end of the string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#
string = ""
i = 5
while i <= 71:
    string += str(i)+","
    i = i + 3

ANSWER = string

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (1 points)
#
# Create a while-loop that subtracts 6 from 13, 71 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#
x = 6
y = 13
i = 0
while i < 71:
    y -= x
    i += 1
ANSWER = y

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.3 (1 points)
#
# Create a while-loop that calculates the factorial number for 8, 8!. The
# factorial of a number is the number multiplied by all smaller integers
# greater than 1. The factorial of 8 is `8 * 7 * 6 * 5 * 4 * 3 * 2 * 1`.
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#
ANSWER = 1
i = 8
while i > 1:
    ANSWER *= i
    i -= 1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 4. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.1 (3 points)
#
# Use a for-loop or a while-loop to reverse the word 'disproportionality'.
#
# Answer with the reversed word.
#
# Write your code below and put the answer into the variable ANSWER.
#

reverse_word = "disproportionality"
ANSWER = ""
for char in reverse_word:
    ANSWER = char + ANSWER


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.2 (3 points)
#
# Swedish numberplates consist of three letters and three numbers. The
# numbers range from 001 to 999. Using one of the four common rules of
# arithmetics (+, -, *, /), on how many of the numberplates can the two first
# numbers give the third number?
#
# Examples:
# 'ABC123' can be combined to 1 + 2 = 3. So this numberplate is good.
# 'ABC129' 1 and 2 cannot be combined to give 9 using the four rules of
# arithmetics, so this does not work.
#
# Order matters, so only use 1 +-*/ 2 = 3 and not 2 +-/* 1 = 3.
#
# Do not count multiple times if more than one rule of arithmetics work.
#
# Answer with the number of numberplates.
#
# Write your code below and put the answer into the variable ANSWER.
#

add = 0
sub = 0
mult = 0
counter = 0

for first in range(0, 10):
    for second in range(0, 10):
        for third in range(0, 10):
            add = first + second
            sub = first - second
            mult = first * second
            if add == third or sub == third or mult == third or (second != 0 and first/second == third):
                if first == 0 and second == 0 and third == 0:
                    continue
                counter += 1


ANSWER = counter


# I will now test your answer - change false to true to get a hint.

dbwebb.assert_equal("4.2", ANSWER, False)


dbwebb.exit_with_summary()
