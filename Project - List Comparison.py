'''Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that
are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python'''

def first_list():
   n = []
   instance = 0
   while True:
        if instance == 0:
            x = input('Enter a sequence of numbers. After each number, hit the ENTER key. Hit the ` key to complete the list:')
            if x == '`':
                return(n)
                break
            else:
                if x.isdigit() == False:
                    x = input('Enter a sequence of numbers. After each number, hit the ENTER key. Hit the ` key to complete the list:')
            x = int(x)    
            n.append(x)
            n.sort()
            instance = 1
        else:
            x = input('Enter another number. Remember to hit ENTER after each number and ` to complete the list:')
            if x == '`':
                return(n)
                break
            else:
                if x.isdigit() == False:
                    x = input('Enter another number. Remember to hit the ENTER key. Hit the ` key to complete the list:')
            x = int(x) 
            n.append(x)
            n.sort()

def second_list():
   n = []
   instance = 0
   while True:
        if instance == 0:
            x = input('Enter another sequence of numbers. After each number, hit the ENTER key. Hit the ` key to complete the list:')
            if x == '`':
                return(n)
                break
            else:
                if x.isdigit() == False:
                    x = input('Enter another sequence of numbers. After each number, hit the ENTER key. Hit the ` key to complete the list:')
            x = int(x)    
            n.append(x)
            n.sort()
            instance = 1
        else:
            x = input('Enter another number. Remember to hit ENTER after each number and ` to to complete the list:')
            if x == '`':
                return(n)
                break
            else:
                if x.isdigit() == False:
                    x = input('Enter another number. Remember to hit the ENTER key. Hit the ` key to complete the list:')
            x = int(x) 
            n.append(x)
            n.sort()
    
        
first_input, second_input = first_list(), second_list()
c = []        

if len(first_input) > len(second_input):
    max_len = first_input
    min_len = second_input
else:
    max_len = second_input
    min_len = first_input
  
for x in max_len:
    if x in min_len:
        c.append(x)
        d = set(c)

result = list(d)

print(result)
