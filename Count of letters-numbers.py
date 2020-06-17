'''Write a program that accepts a sentence
and calculate the number of letters and digits.'''

user_input = input('Enter a sentence or type quit to exit:')
check = 1

def letter_number_count(a):
    array = list(a)
    alpha_count = 0
    number_count = 0
    for x in array:
        if x.isalpha() == True:
            alpha_count += 1
        elif x.isdigit() == True:
            number_count += 1
        else:
            pass
    string_output = 'Letters:' + str(alpha_count) + '\nNumbers:' + str(number_count)
    b = 0
    return string_output, b

while user_input != 'quit':
    if check == 0:
        user_input = input('Enter another sentence or type quit to exit:')
        if user_input == 'quit':
            break
        result, check = letter_number_count(user_input)
        print(result)
    elif check == 1:
        result, check = letter_number_count(user_input)
        print(result)
    else:
        break
        
