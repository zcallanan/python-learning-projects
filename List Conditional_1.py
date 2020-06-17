'''write a program that prints out
all the elements of the list that are less than 5.

Instead of printing the elements one by one,
make a new list that has all the elements less than 5 from this
list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only
elements from the original list a that are smaller than that number
given by the user.'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

result = [x for x in a if x < 5] #list comprehension
print(result)

check = 0
def user_input():
    x = input('Enter a number or type 0 to exit:')
    number_confirmed = False
    while number_confirmed == False:
        if x.isdigit() == False:
            x = input('Enter a number or type 0 to exit:')
        else:
            x = int(x)
            number_confirmed = True
    return x

while check == 0:
    num = user_input()
    if num < 1:
        break
    result = [x for x in a if x < num]
    print(result)
        

