#!/usr/bin/env python3

"""
479a201f24a7c08b3b3227d8df8cef67
python
lab5
v4
noka21
2021-10-20 05:37:54
v4.0.0 (2019-03-05)

Generated 2021-10-20 07:37:54 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""
from itertools import chain
from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()


# ==========================================================================
# Lab 5 - python
#
# A look into dictionaries and tuples.
#


# --------------------------------------------------------------------------
# Section 1. Dictionaries
#
# Some basics with dictionaries.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a small phonebook using a dictionary. Use the names as keys and
# numbers as values.
#
# Use
#
# > Baggins, Aragorn, Smaug
#
# and corresponding numbers
#
# > 55523412, 55564222, 55567894
#
# Add the phonenumbers as integers. Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#

phonebook_dic = {
    "Baggins": 55523412,
    "Aragorn": 55564222,
    "Smaug": 55567894

}


ANSWER = phonebook_dic

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# How many items are there in the phonebook dictionary?
#
# Write your code below and put the answer into the variable ANSWER.
#
count = 0
for key in phonebook_dic:
    count += 1


ANSWER = count

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the `get()` method on your phonebook and answer with the phonenumber of
# 'Baggins'.
#
# Write your code below and put the answer into the variable ANSWER.
#
wrd = 'Baggins'
for key, value in phonebook_dic.items():
    if wrd in phonebook_dic:
        ANSWER = phonebook_dic.get(wrd)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Get all keys from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#
key_list = []
for key in phonebook_dic:
    key_list = phonebook_dic.keys()
ANSWER = sorted(key_list)


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Get all values from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER1 = list(phonebook_dic.values())

ANSWER=sorted(ANSWER1)

    
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Use the in-operator to test if the name 'Baggins' exists in the phonebook
# dictionary. Answer with the return boolean value.
#
# Write your code below and put the answer into the variable ANSWER.
#
for key in phonebook_dic:
    if key == 'Baggins':
        ANSWER = True

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a copy of the phonebook dictionary.
# Get and remove the item 'Baggins' from the copied phonebook (use pop()).
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#
ANSWER=phonebook_dic.copy()
ANSWER.pop('Baggins')



# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Tuples
#
# Some basics with tuples.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a tuple with 'moose, 12, 1.98, table, 7'. Answer with the length of
# the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#
tup=("moose", 12, 1.98, "table", 7)

ANSWER = len(tup)
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Create a tuple out of:
#
# > (moose, 12, 1.98, table, 7).
#
# Assign each value in the tuple to different variables:
#
# > 'a','b','c','d','e'.
#
# Answer with the variable: 'd'.
#
# Write your code below and put the answer into the variable ANSWER.
#
tup2='a','b','c','d','e'
tup2=("moose", 12, 1.98, "table", 7)
ANSWER = tup2[3]

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the list
#
# > [98, 5, 12, 369, 1]
#
# Assign the first two elements to a tuple with a slice on the list.
#
# Answer with the first element in the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

lis_1=[98, 5, 12, 369, 1]
(a,b)=((lis_1[0], lis_1[1]))

lis_1.insert(0,(a,b))

ANSWER=a

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Create a tuple with
#
# > (elephant, 33, 7.28, stove, 4)
#
# Convert it to a list and replace the second element with:
#
# > "green"
#
# Convert it back to a tuple and answer with the first three elements in a
# comma-separated string,  without an ending `,`.
#
# Write your code below and put the answer into the variable ANSWER.
#
tup4="elephant", 33, 7.28, "stove", 4
tup5=list(tup4)
tup5[1]="green"
tup6=tuple(tup5)
s = [[i] for i in tup6[:3]]
ANSWER=','.join(map(str,chain.from_iterable(s)))

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, True)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Use a for-loop to walk through the original phonebook dictionary and create
# a string representing it. Each name and number should be on its own row,
# separated by a space. The names must come in alphabetical order. Note that
# every row should end with a newline character, `\n`.
#
# Answer with the resulting string.
#
# Write your code below and put the answer into the variable ANSWER.
#
ANSWER=""
lst=[]
for (k,v) in phonebook_dic.items() :
    newtup=(k,v)
    lst.append(newtup)
tup_1=sorted(lst)
for i_1,i_2 in tup_1:
    an=i_1
    sn=i_2
    ANSWER+=an+" "+ str(sn)+"\n"

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Convert the phonenumber to a string and add the prefix '+1-', representing
# the language code, to each phone-number.
#
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#

for k in phonebook_dic :
    phonebook_dic[k]= '+1-'+str(phonebook_dic[k])
ANSWER = phonebook_dic

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, True)


dbwebb.exit_with_summary()
