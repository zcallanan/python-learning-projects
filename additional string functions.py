'''Replace'''
text = 'ha@@iness'

print(text.replace('@','p'))

'''Split'''
text = 'Dog walking'
print(text.split())

my_string = 'python123'
print(my_string.isalnum())  #Checks if the string is a combination of alphabets and numbers
'''returns True''' 
print(my_string.isupper()) #Checks if all the characters are upper cases 
'''returns False''' 
print(my_string.islower()) #Checks if all the characters are lower cases
'''returns True''' 
print(my_string.isalpha()) #Checks if all the characters are alphabets 
'''return False''' 
print(my_string.isdigit()) #Checks if all the characters are numbers 
'''returns False'''

my_string = 'this is sUposseD to bE a tItLe'
print(my_string.title())
'''Returns: 
This Is Supposed To Be A Title'''

my_string = 'python'
print('-'.join(my_string)) #p-y-t-h-o-n
'''Joining lists: ''' 
my_list = ['hello','world']
print('@'.join(my_list)) #hello@world

my_string = 'pyThOn'
print(my_string.upper()) #PYTHON 
print(my_string.lower()) #python
