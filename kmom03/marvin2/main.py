"""
here
"""
import marvin


def main():
    """
    file main.py contain the code to start the program.
    the main function contains the code for while-loop.
    main file should call the main function in the block
    """
    menu_loop = True
    while menu_loop:
        marvin.print_menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            marvin.greet()

        elif choice == "2":
            marvin.celcius_to_farenheit()

        elif choice == "3":
            marvin.word_manipulation()

        elif choice == "4":
            marvin.sum_and_average()
        elif choice == "5":
            marvin.hyphen_string()

        elif choice == "6":
            marvin.is_isogram()
        elif choice == "7":
            marvin.compare_numbers()

        elif choice == "8":
            string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(string))

        elif choice == "9":
            string = input("Enter a name to create Acronym : ")
            print(marvin.get_acronym(string))

        elif choice == "10":
            string = input("Enter a string to mask_string: ")
            print(marvin.mask_string(string))

        elif choice == "11":
            string1 = input("Enter a string to find: ")
            string2 = input("Enter a string to find: ")
            print(marvin.find_all_indexes(string1, string2))

        else:
            print("That is not a valid choice. You can only choose from the menu")

        input("\n\nPress enter to continue to the menu...")


if __name__ == "__main__":
    main()
