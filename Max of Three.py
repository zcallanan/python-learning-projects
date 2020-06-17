'''Implement a function that takes as input three variables,and returns the largest of the three. Do this without
using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us.
All you need is some variables and if statements!'''

if __name__ == '__main__':
    '''Function returns True if a is a float type, and False if a is not a float type'''
    def is_float(a):
        '''Try: float(a) -> True\nexcept ValueError: -> False'''
        try:
            float(a)
            return True
        except ValueError:
            return False

    '''Function returns True if a is an integer type, and False if a is not an integer type'''
    def is_integer(a):
        '''Try: int(a) -> True\nexcept ValueError: -> False'''
        try:
            int(a)
            return True
        except ValueError:
            return False

    '''Function tests whether a is an integer or float, and converts string to its proper type, then returns a'''
    def process_number(a):
        '''if a is int -> a = int(a), return a\nelif a is float -> a = float(a), return a\nelse -> return False'''
        if is_integer(a) == True:
            a = int(a)
        elif is_float(a) == True:
            a = float(a)
        else:
            return False
        return a
            
      
    def user_input():
        '''Takes user input, processes that input, returns input in either integer or float type''' 
        n = True
        while type(n) == bool:
            x = input('Enter a number:')
            n = process_number(x)
            if n != False:
                x = n
            else:
                print('That\'s not a number!')
        n = True
        while type(n) == bool:
            y = input('Enter another number:')
            n = process_number(y)
            if n != False:
                y = n
            else:
                print('That\'s not a number!')
        n = True
        while type(n) == bool:
            z = input('Enter a third number:')
            n = process_number(z)
            if n != False:
                z = n
            else:
                print('That\'s not a number!')
        return x,y,z

    def max_value(value_one, value_two, value_three):
        '''Compares value_one, value_two, and value_three for which is higher or all equal. Prints highest number'''
        if value_one > value_two and value_one > value_three:
            print(value_one, 'is the highest number!')
        elif value_two > value_one and value_two > value_three:
            print(value_two, 'is the highest number!')
        elif value_three > value_two and value_three > value_one:
            print(value_three, 'is the highest number!')
        elif value_one == value_two and value_two == value_three:
            print('No number is higher than the other!')
                

    value_one, value_two, value_three = user_input()
    max_value(value_one, value_two, value_three)


             
             


  

