#!/usr/bin/env python3

"""
3da9c4af8c6a88014dbcc08ff042556b
python
lab4
v4
noka21
2021-10-03 16:20:33
v4.0.0 (2019-03-05)

Generated 2021-10-03 18:20:33 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()


# ==========================================================================
# Lab 4 - python
#
# "In these exercises we will take a look into lists."
#


# --------------------------------------------------------------------------
# Section 1. List basics
#
#
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Concatenate the two lists [mosquito, floor] and [chair, Depp].
#
# Answer with your list.
#
# Write your code below and put the answer into the variable ANSWER.
#


list_1 = ["mosquito", "floor"]
list_2 = ["chair", "Depp"]


ANSWER = list_1+list_2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use the list [Dafoe, Sheen, Berenger, Depp, Whitaker].
#
# Add the words 'yellow' and 'donkey' as the second and third element.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#


list_3 = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]
list_3.insert(1, "yellow")
list_3.insert(2, "donkey")


ANSWER = list_3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the list [Dafoe, Sheen, Berenger, Depp, Whitaker].
#
# Replace the third word with: 'cord'.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#
list_3 = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]
list_3[2] = "cord"

ANSWER = list_3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Sort the list
#
# > [wasp, fly, butterfly, bumblebee, mosquito]
#
# in descending alphabetical order. Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#
list_4 = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]
list_4.sort(reverse=True)

ANSWER = list_4

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Use `remove()` to delete the word:
#
# > 'flute'
#
# from the list:
#
# > [flute, guitar, drums, piano, bass]
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#
list_5 = ["flute", "guitar", "drums", "piano", "bass"]
list_5.remove("flute")

ANSWER = list_5

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Built-in list functions
#
# Some basic built-in functions.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Use a built-in function to sum all numbers in the list:
#
# > [67, 50, 2, 39, 15]
#
# Answer with the result as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

list_sum = [67, 50, 2, 39, 15]
ANSWER = sum(list_sum)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Use built-in functions, such as `sum` and `len` to get the average value of
# the list:
#
# > [567, 23, 12, 36, 7]
#
# Answer with the result as a float with at most one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#
list_average = [567, 23, 12, 36, 7]

ANSWER = sum(list_average)/len(list_average)
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the built-in functions `split()` and `join()` to fix this string:
#
# > "The?sun?is?shining"
#
# into a real sentence, (without '?').
#
# Answer with the fixed string.
#
# Write your code below and put the answer into the variable ANSWER.
#
string_to_be_fixed = "The?sun?is?shining"
List_6 = string_to_be_fixed.split("?")


ANSWER = " ".join(List_6)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Use slice on the list
#
# > [pig, horse, cow, cat, dog]
#
# and replace the second and third element with
#
# > "book, candle"
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#
list_7 = ["pig", "horse", "cow", "cat", "dog"]
list_8 = ["book", "candle"]
list_7[1:3] = list_8
ANSWER = list_7

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.5 (1 points)
#
# Assign the list
#
# > [b, a, e, d, c]
#
# to a variable called 'list1'.
#
# Assign the list again, but to another variable called 'list2'.
#
# Answer with the result of 'list1 is list2'.
#
# Write your code below and put the answer into the variable ANSWER.
#
list1 = ["b", "a", "e", "d", "c"]
list2 = ["b", "a", "e", "d", "c"]

ANSWER = list1 is list2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.6 (1 points)
#
# Use your lists from the last exercise. Assign 'list1' to another variable
# called 'list3' like this:
#
# > list3 = list1
#
# Answer with the result of 'list1 is list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#
list3 = list1

ANSWER = list1 is list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.7 (1 points)
#
# Use your lists from the last exercise. Change the first element in 'list1'
# to
#
# > "p"
#
# Answer with 'list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#
list1[0] = "p"

ANSWER = list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Create a function that returns the list passed as argument sorted in
# numerical and ascending order. Also multiply all values with 10.
#
# Use the list:
#
# > [567, 23, 12, 36, 7]
#
# and the built-in method `sort()`.
#
# Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#
list_9 = [567, 23, 12, 36, 7]


def list_sort_func(list_9_arg):
    """
    unction that returns the list passed 
    """
    list_9_arg.sort()
    for (i, _) in enumerate(list_9):
        list_9[i] = list_9[i]*10
    return list_9_arg


ANSWER = list_sort_func(list_9)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Create a function that takes the list:
#
# > [567, 23, 12, 36, 7]
#
# as argument.
#
# The function should multiply all even numbers by 2 and add 9 to all odd
# numbers.
#
# Answer with the modified list sorted in numerical order, descending.
#
# Write your code below and put the answer into the variable ANSWER.
#
list_10 = [567, 23, 12, 36, 7]


def list_even_func(list_9_arg):
    """
    unction that returns the list passed 
    """
    for (i, _) in enumerate(list_9_arg):
        if list_9_arg[i] % 2 == 0:
            list_9_arg[i] = list_9_arg[i]*2
        if list_9_arg[i] % 2 == 1:
            list_9_arg[i] = list_9_arg[i]+9

    list_9_arg.sort(reverse=True)
    return list_9_arg


ANSWER = list_even_func(list_10)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, True)


dbwebb.exit_with_summary()
