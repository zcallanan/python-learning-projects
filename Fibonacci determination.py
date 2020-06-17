'''Write a Python program to get the Fibonacci series between two numbers'''



def user_input(): #Take two user inputs, because I can
    def is_number(x): #Is it a number? function
        try:
            int(x)
            return True
        except ValueError:
            return False
    
    '''First user input'''
    user_input_one = int(input('Enter a positive number or type a negative number to exit:'))
    one_confirmed = False
    while one_confirmed == False: #Did the user enter a number?
        if is_number(user_input_one) == False:
            user_input_one = int(input('That\'s not a number. Add a positive number or type a negative number to exit:'))
        else:
            one_confirmed = True        
    '''Second user input'''        
    user_input_two = int(input('Enter a second positive number or type a negative number to exit:'))
    two_confirmed = False
    while two_confirmed == False: #Did the user enter a number?
        if is_number(user_input_two)== False:
            user_input_two = int(input('That\'s not a number. Add a second positive number or type a negative number to exit:'))
        else:
            two_confirmed = True
    '''Make inputs integers'''
    user_input_one = int(user_input_one)
    user_input_two = int(user_input_two)

    '''Negative 1 equals quit'''
    if user_input_one < 0 or user_input_two < 0:
        user_input_one, user_input_two = -1, -1
    
    return(user_input_one, user_input_two) #input function output

def find_fibonacci(y,z):
    value_range = range(y,z)
    array = []
    a = 0
    b = 1
    c = 1

    for x in value_range:
        n = a + b
        if a < n and b == n and n >= y:
            array.append(a)
            array.append(b)
        if n <= z and n >= y:
            array.append(n)
        if n > z:
            break
        a = b
        b = n
    return(c, print(array))

check = 0
input_one = 0
input_two = 0
    
while input_one != -1 or input_two != -1:
    if check == 1: #subsequent iterations
        input_one, input_two = user_input()
        if input_one == -1 or input_two == -1:
            break
        find_fibonacci(input_one, input_two)
    else: #initial iteration
        input_one, input_two = user_input()
        if input_one == -1 or input_two == -1:
            break
        check = find_fibonacci(input_one, input_two)
        

    
