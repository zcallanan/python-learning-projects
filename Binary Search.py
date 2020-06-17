'''Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest
to largest) and another number. The function decides whether or not the given number is inside the list and
returns (then prints) an appropriate boolean.'''

if __name__ == "__main__":
    import random

    def create_int_list(a): #f(user_input)
        b = a + random.randint(25,75)

        while True:
            x = random.sample(range(b), k = random.randint(8, 18))
            x = sorted(x)
            if a < x[0] or a > x[-1]: #check if user input is in the random number range

                pass #if False, get another number list
            else:
                print('The number list I generated is:', x)
                return x #if True, return number list

    def user_input():
        while True:
            x = input('Enter a positive number or type \'quit\' to exit:')
            if x == 'quit':
                break
            elif x.isdigit== False or x >= '1' == False:
                print('That\'s not a positive number!')
            else:
                return int(x)

    '''Deprecated function:
    def binary_search(n, number_list): #f(user_input, n_list)
        list_length = len(number_list) - 1 #A 10 length list has an end_index of 9, so len(list) - 1
        while True:
            median_index = int(list_length / 2)
            if len(number_list) == 2:
                while True:
                    if number_list[0] == n or number_list[1] == n:
                        return True
                    else:
                        return False
            elif n < number_list[median_index]:
                number_list = [x for x in number_list if x <= number_list[median_index]]
            elif n > number_list[median_index]:
                number_list = [x for x in number_list if x >= number_list[median_index]]
            else:
                return True
            list_length = len(number_list)'''


    '''This function evaluates whether the middle value of a list is equal to a number, and if not sets
    the highest index or lowest index to the median index, determines a new median value, until the median value
    equals the highest or lowest index. If n is not equal to the median at this point, then it is not in the list'''
    def binary_search(n, number_list):
        end_index = len(number_list) - 1 #End index value is one less than the length
        start_index = 0 #First index always starts at 0
        while True:
            median_index = int(((end_index - start_index) / 2) + start_index) #Half difference of index values added onto starting index gives middle index
            if n == number_list[median_index]:
                print(n, 'is in the list at index:', median_index)
                return True
            elif median_index == start_index or median_index == end_index: #When down to 2 index values, if median value is not equal the number, then neither is
                print(n, 'is not in the list.')
                return False
            elif n < number_list[median_index]: #Number less than median value, then median value becomes last index value
                end_index = median_index
            else: #n > number_list[median_index] --> Number greater than median value, then median value becomes first index value
                start_index = median_index

n = user_input()
n_list = create_int_list(n)
binary_search(n, n_list)
