'''Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).'''


def user_input():
    while True:
        x = input('Enter a potential prime number or type "exit" to quit:')
        if x == 'exit':
            return x
        elif x.isdigit() == False:
            pass
        else:
            x = int(x)
            return x

def prime(a):
    result = [x for x in range(2,a) if a % x == 0]
    if len(result) > 0:
        print(a, 'is not a prime number.')
    else:
        print(a, 'is a prime number.')

while True:
    get_input = user_input()
    if get_input == 'exit':
        break
    prime(get_input)
    
    
    
