'''When a player (say player 1, who is X) wants to place an X on the screen, they can’t just click on a terminal.
So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place
their piece.'''

if __name__ == '__main__':
    def validate(player_input, array, all_inputs, player_number):
        '''Create a list with input data'''
        input_list = list(player_input) #Convert player input to a list for validation and processing
        '''Validate input length'''
        player_input = player_input.strip() #Remove any leading or trailing white space
        if len(input_list) != 3: #Validate input list is only 3 characters
            return False, all_inputs
        '''Validate input format'''
        validate_array = ['1','2','3'] #Possible row and column values
        val_increment = 0 #number increment
        enumerated_list = list(enumerate(input_list))
        for index, val in enumerated_list:
            if val in validate_array and (index == 0 or index == 2):
                val_increment += 1
            elif index == 1 and val == ',':
                val_increment += 1
        if val_increment != 3:
            return False, all_inputs
            '''Validate if a square is taken or return value & all_input list'''
        elif array[int(input_list[0]) - 1][int(input_list[2]) - 1] > 0:
            return 1, all_inputs
        else:
            all_inputs.extend([[player_number, player_input]])
            all_inputs = sorted(all_inputs)
            return input_list, all_inputs
            
    def user_input(player_number, form, array, all_inputs):
        text = 'Player ' + player_number + ' enter a row,col value to place your ' + form + ':'
        while True:
            player_input = input(text)
            if player_input == 'quit':
                return player_input, all_inputs
            elif player_input == 'squares':
                n = 0
                while n < len(all_inputs):
                    if all_inputs[n][0] == '1':
                        if a == True:
                            print('Player 1 has X\'s on:')
                            a = False
                        print(all_inputs[n][1])
                    elif all_inputs[n][0] == '2':
                        if b == True:
                            print('Player 2 has O\'s on:')
                            b = False
                        print(all_inputs[n][1])
                    n += 1
            else:
                value, all_inputs = validate(player_input, array, all_inputs, player_number)
                if value == False:
                    print('Your entry is not in the correct format: row,col')
                elif value == 1:
                    print('That square is already taken!')
                else:
                    return value, all_inputs

    def game():
        turns_increment = 1
        array = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        all_inputs = []
        print('Welcome to Tic-Tac-Toe! This is a two player game.\n* Player 1 plays as "X" and Player 2 plays as "O"\n* Place your "X" or "O" on the board by entering the square location in the form of: \'row,col\'\n    ** The upper left square is entered as: 1,1 \n    ** The middle square is entered as: 2,2\n    ** The lower right square is entered as 3,3\nEnter \'squares\' to view the occupied squares or \'quit\' to exit')
        while turns_increment < 10:
            if turns_increment % 2 != 0:
                player_number = '1'
                form = 'X'
            else:
                player_number = '2'
                form = 'O'
            choice, all_inputs = user_input(player_number, form, array, all_inputs)
            if choice == 'quit':
                print('Player has quit!')
                break
            array[int(choice[0]) - 1][int(choice[2]) - 1] = int(player_number)
            turns_increment += 1


    '''Function Calls'''
    result = game()
   

