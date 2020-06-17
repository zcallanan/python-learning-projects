'''Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)'''

def get_string():
    x = input('Enter a string or type "quit" to exit:')
    if x == 'quit': #If quit is entered, skip comparison
        return x
    l = list(x) #string converted to a list
    l_length = len(l) 
    l_range = range(l_length) 
    reversed_list = [] 
    count = -1 #used to append characters in the list from the end to the start
    c = 0
    while c < l_length:
        if count == 0: #first character of reversed word
            reversed_list.append(l[-1])
            count = count - 1
        else: #all other characters of reversed word
            reversed_list.append(l[count])
            count = count - 1
        c = c + 1
    comparison = True
    
    for x in l_range:
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
