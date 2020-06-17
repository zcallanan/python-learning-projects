'''Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
first and last elements of the given list. For practice, write this code inside a function.'''

import random
a = random.sample(range(10), k = random.randint(4,9)) #Generate random list

def new_list(b):
    y = [x for x in b if x == b[0] or x == b[-1]]
    return y

print('Original List:', a)
print('New list with first and last values:', new_list(a))



