#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import random  

marvin_image = r"""
                 _______
               _/       \_
              / |  INFO | \
             /  |__   __|  \
            |__/((o| |o))\__|
            |      | |      |
            |\     |_|     /|
            | \           / |
             \| /  ___  \ |/
              \ | / _ \ | /
               \_________/
                _|_____|_
           ____|_________|____
          /                   \
"""

def print_menu():
    """
    function to print the menu
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Info. What can I do you for?")
    print("1) Present yourself to the Info.")
    print("2) Celsius to Fahrenheit ")
    print("3) Let's play parrot! You say it, I will repeat it.")
    print("4) Sum numbers and find the average ")
    print("5) Repeat letters in word")
    print("6) Isogram")
    print("7) Is smaller, bigger or equal.")
    print("8) Do you want to create randomize string?")
    print("9) Get acronym to the name you give :")
    print("10) Give mig a string I'll hide all characters except the last four: ")
    print("11) Do you want to search a word in a text?")
    print("q) Quit.")


def greet():
    """
    Menu choice 1
    """
    name = input("What is your name? ")
    print("\nInfo says:\n")
    print(f"Hello {name} - your awesomeness!")
    print("What can I do you for?!")


def celcius_to_farenheit():
    """
    Menu choice 2
    """
    degree_sign = "\N{DEGREE SIGN}"
    temp_Celsius = input(
        " Please enter a temperatur in Celsius to convert it to Fahrenheit:  ")
    # convert the value and round it
    temp_Fahrenheit = round((float(temp_Celsius) * 9 / 5 + 32), 2)
    print(
        f"{temp_Celsius}{degree_sign} in Celsius is {temp_Fahrenheit}{degree_sign} in Fahrenheit")


def word_manipulation():
    """
    Menu choice 3
    """
    text = str(input("Please input a single word: "))
    try:
        occurrence = int(input("Please input a number: "))
    except ValueError:
        print("not a number!")
    print(multiply_str(text,occurrence))


def sum_and_average():
    """
    Menu choice 4
    """
    print("Enter a number, done to quit: ")
    number = 0
    sum_number = 0
    counter_4 = 0
    while True:
        user_input = input("input: ")
        if user_input == "done":
            break
        else:
            try:
                number = round((float(user_input)), 2)
            except ValueError:
                print("not a number!")
                continue
            counter_4 += 1
            sum_number = round((sum_number+number), 2)
            try:
                average = round((sum_number/counter_4), 2)

            except ZeroDivisionError:
                print("You do not enter any numbers ")
    print(f"The sum of all numbers are {sum_number} and the average is {average}")

def hyphen_string():
    """
    Menu choice 5
    """
    user_word = input("Give me a word ")
    new_word = ""
    for (i, _) in enumerate(user_word):
        if i >= len(user_word) - 1:
            new_word = user_word[i] * (i + 1) + ""
            print(new_word, end="")
        else:
            new_word = user_word[i] * (i + 1) + "-"
            print(new_word, end="")


def is_isogram():
    """
    Menu choice 6
    """
    input_user = input("Give me a word  ")
    is_isogram_var = True
    for letter in input_user:
        if input_user.count(letter) >= 2:
            is_isogram_var = False
    if is_isogram_var is False:
        print("No match!")
    else:
        print("Match!")


def compare_numbers():
    """
    Menu choice 7
    """
    previous_nr = None
    current_nr = 0
    while True:
        user_input = input("Enter number, done to quit: ")
        if user_input == "done":
            break
        else:
            try:
                current_nr = float(user_input)
            except ValueError:
                print("not a number!")
                continue
            if previous_nr is not None:
                if current_nr > previous_nr:
                    print("larger!")
                elif current_nr < previous_nr:
                    print("smaller!")
                else:
                    print("same!")
            previous_nr = current_nr

def randomize_string(string):
    """
    Menu choice 8
    """
    random_string = ''.join(random.sample(string,len(string)))
    return f"{string} --> {random_string}"

def get_acronym(string):
    """
    Menu choice 9
    """
    acronym=""
    for i in (string):
        if i.isupper():
            acronym +=i
    return acronym

def multiply_str(string,number_):
    """
    Menu create function which use inside modul
    """
    return string*number_


def mask_string(string):
    """
    Menu choice 10
    """
    mask_string_mark="#"
    length_string=len(string)-4
    new_mask_string=multiply_str(mask_string_mark,len(string)-4)
    last_four=string[length_string:]
    return new_mask_string+last_four
    

def find_all_indexes(string1,string2):
    """
    Menu choice 11
    """
    index_string= ""
    i=0
    j=0
    try:
        while j in range(0,len(string1)):
            i=string1.index(string2,j,len(string1))
            index_string+=str(i)+","
            j=i+len(string2)
        
    except ValueError:
        print('')
    return index_string[:len(index_string)-1]
    