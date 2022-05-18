'''This file holds helper functions to do things easier with pyton'''

import pandas as pd
import numpy as np
import random

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

def random_phrase(list1, list2):
    '''A function that takes in two lists
       randomly selects one item from each list
       and then concatenates those two items together 
       with a space inbetween.'''
    item1 = random.choice(list1)
    item2 = random.choice(list2)

    return str(item1) + ' ' + str(item2)

# this condition will only be true if we're running the file as a script
# Put things down here that are for testing your code
# Things that *you* (the developer of the package) might need to test
# but things that some other user of this package wouldn't really care about.
if __name__ == '__main__':
    my_phrase = random_phrase()
    print(my_phrase)

# def some_other_func()