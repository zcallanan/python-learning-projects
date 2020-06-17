'''This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes
(8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s
print statement.'''

if __name__ == '__main__':
    '''Function that gets input number from user'''
    def get_size():
        while True:
            size = input('What size game board do you want to play with? Enter a number or type \'quit\' to exit:')
            if size == 'quit' or size == 'Quit':
                return size
            elif size.isdigit == False:
                print('>>> That\'s not a number! <<<')
            elif size <= '0':
                print('>>> That number is too low! <<<')
            else:
                size = int(size)
                return size

    def dash_row(x):
        print(' ---' * x) #Print the row of dashes

    def pipe_row(x):
        print('|   ' * (x + 1)) #Print the number of pipes requested + 1

    def draw(x): #Print the game board
        for i in range(x):
            dash_row(x)
            pipe_row(x)
        dash_row(x)

    '''function calls'''
    user_input = get_size()
    if user_input == 'quit' or user_input == 'Quit':
        pass
    else:
        draw(user_input)
            
