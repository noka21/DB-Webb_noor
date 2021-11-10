"""
Import your new file/module
# in `answer.py`
"""
def multiplication(nr1 , nr2):
    """
    takes two arguments and return the product of the two arguments.
    """
    return nr1 * nr2
def funny_word(word):
    """
     takes one argument and prepends it to the string ' is a funny word'.
    """
    return f"{word} is a funny word"

def decider(word_or_nr):
    """
     takes one argument
    """
    if word_or_nr.isalpha() is True:
        return funny_word(word_or_nr)
    
    return multiplication(int(word_or_nr) , int(word_or_nr))

def double_decider(word_arg,nr_arg):
    """
    Separate the two values by ' and the square is '
    """
    word_d=decider(word_arg)
    nr_d=decider(nr_arg)
    
    return word_d+" and the square is "+str(nr_d)
