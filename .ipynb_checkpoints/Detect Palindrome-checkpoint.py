'''Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)'''

def get_string():
    x = input('Enter a string or type "quit" to exit:')
    if x == 'quit': #If quit is entered, skip comparison
        return x
    l = list(x)
    reversed_list = list(l[::-1])
    comparison = True
    
    for x in range(len(l)):
        if l[x] != reversed_list[x]: #Characters in list position x comparison. If not equal, not a palindrome
            comparison = False
            break
    if comparison == False:
        result = print('The string entered is not a palindrome!')
    else:
        result = print('The string entered is a palindrome!')


while True:
    user_input = get_string()
    if user_input == 'quit':
        break
