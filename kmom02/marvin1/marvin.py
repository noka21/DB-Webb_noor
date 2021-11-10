#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

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

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
menu_loop = True
while menu_loop:

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
    print("q) Quit.")
    choice = input("--> ")

    if choice == "q":
        print("Bye, bye - and welcome back anytime!")
        break

    elif choice == "1":
        name = input("What is your name? ")
        print("\nInfo says:\n")
        print("Hello %s - your awesomeness!" % name)
        print("What can I do you for?!")

    elif choice == "2":
        degree_sign = "\N{DEGREE SIGN}"
        temp_Celsius = input(
            " Please enter a temperatur in Celsius to convert it to Fahrenheit:  ")
        # convert the value and round it
        temp_Fahrenheit = round((float(temp_Celsius) * 9 / 5 + 32), 2)
        print(
            f"{temp_Celsius}{degree_sign} in Celsius is {temp_Fahrenheit}{degree_sign} in Fahrenheit")

    elif choice == "3":
        text = str(input("Please input a single word: "))

        if text == "done":
            break
        else:
            try:
                occurrence = int(input("Please input a number: "))
            except ValueError:
                print("not a number!")
                continue

            new_text = ''
            for i in range(occurrence):
                new_text += text
            print(new_text)

    elif choice == "4":

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

    elif choice == "5":
        user_word = input("Give me a word ")
        new_word = ""
        for (i, value) in enumerate(user_word):
            if i >= len(user_word) - 1:
                new_word = user_word[i] * (i + 1) + ""
                print(new_word, end="")
            else:
                new_word = user_word[i] * (i + 1) + "-"
                print(new_word, end="")

    elif choice == "6":
        input_user = input("Give me a word  ")
        is_isogram = True
        for letter in input_user:
            if input_user.count(letter) >= 2:
                is_isogram = False
        if is_isogram is False:
            print("No match!")
        else:
            print("Match!")

    elif choice == "7":
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

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\n\nPress enter to continue to the menu...")
