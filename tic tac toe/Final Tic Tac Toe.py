if __name__ == '__main__':
    def dash_row():
        '''Prints ' ---' three times in a row when called'''
        print(' ---' * 3) #Print the row of dashes

    def pipe_row(s):
        '''Returns an assembled string of '| ' + s + ' ' where s = ' ', X, or O'''
        if s == 'end':
            result = '|'
        else:
            if s == 0:
                s = ' '
            elif s == 1:
                s = 'X'
            elif s == 2:
                s = 'O'
            result = '| ' + s + ' ' 
        return result

    def draw(array): #Print the game board
        '''Function prints game board when called. Prints four rows of dashes, separated by a row of pipes(three total)'''
        row_one = list(enumerate(array[0]))
        row_two = list(enumerate(array[1]))
        row_three = list(enumerate(array[2]))
        
        to_draw, n = '', 0
        while n < 3:
            dash_row() #Print dash row, to be followed by a pipe row
            if n == 0:
                draw_list = row_one
            elif n == 1:
                draw_list = row_two
            elif n == 2:
                draw_list = row_three
            for x,y in draw_list:
                if y == 0:
                    to_draw = to_draw + pipe_row(0)
                elif y == 1:
                    to_draw = to_draw + pipe_row(1)
                elif y == 2:
                    to_draw = to_draw + pipe_row(2)
            to_draw = to_draw + pipe_row('end')
            print(to_draw)
            n += 1
            to_draw = ''
        dash_row() #Final dash row
            


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
        enumerated_list = list(enumerate(input_list)) #Creates a list for index reference
        for index, val in enumerated_list:
            if val in validate_array and (index == 0 or index == 2): #If val is 1, 2, or 3 and val is in index slot 0 or 2
                val_increment += 1
            elif val == ',' and index == 1: #If val is ',' and in index slot 1
                val_increment += 1
        if val_increment != 3:
            return False, all_inputs #Return of False indicates a misformated input
            '''Validate if a square is taken or return value & all_input list'''
        elif array[int(input_list[0]) - 1][int(input_list[2]) - 1] > 0: #array uses is 0,1,2. Input is 1,2,3. So 
            return 1, all_inputs #Return of 1 indicates an occupied square
        else:
            all_inputs.extend([[player_number, player_input]]) #all_inputs creation
            all_inputs = sorted(all_inputs)
            return input_list, all_inputs    
             
    def user_input(player_number, form, array, all_inputs):
        '''Function requests and returns user input.'''
        draw(array) #Draws game board before user input to display what squares are taken
        text = 'Player ' + player_number + ' enter a row,col value to place your ' + form + ':'
        while True:
            player_input = input(text)
            if player_input == 'quit':
                return player_input, all_inputs
            elif player_input == 'fun':
                function_info()
            elif player_input == 'squares':
                n, a, b = 0, True, True
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
    
    def get_choice(player_number, form, array, all_inputs):
        '''Description:  Calls for user input and returns quit choice or assigns player number to array'''
        choice, all_inputs = user_input(player_number, form, array, all_inputs)
        if choice == 'quit': #Do not add 'quit' to array, so returns unmodified array in order to quit
            return array, all_inputs, choice
        else:
            array[int(choice[0]) - 1][int(choice[2]) - 1] = int(player_number)
            return array, all_inputs, choice #Returns modified array
        

    def game():
        '''Description:\n  Keeps track of rounds, initiates input and evaluation functions'''
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
            array, all_inputs, choice = get_choice(player_number, form, array, all_inputs)
            if choice == 'quit':
                print('Player has quit!')
                return False
            game_columns = columns(array)
            diagonals = diagonal(array)
            result = evaluate(array, game_columns, diagonals)
            game_over_check = player_wins(result,array)
            if game_over_check == 1 or game_over_check == 2:
                return player_number
            turns_increment += 1
        if turns_increment > 9:
            player_wins('Draw')
        
    def columns(array):
        '''Takes the row array and converts it to three column arrays within an array.'''
        column_list, arra, arrb, arrc = [], [], [], []
        index_increment = 0 #Value incremented at the end of each while cycle
        while index_increment < 3:
            for index, val in list(enumerate(array[index_increment])): #For index, value in index n of array a
                if index == 0: #If index of array (which is in the larger array) is equal to zero
                    arra.append(val) #Then append value to array arra
                elif index == 1:
                    arrb.append(val)
                elif index == 2:
                    arrc.append(val)
            index_increment += 1 #n increment
        column_list.append(arra) #Append arra to array
        column_list.append(arrb) #Append arrb to array
        column_list.append(arrc) #Append arrc to array
        return column_list #Return column array

    def diagonal(array):
        '''Takes the row array and converts it to two diagonal value arrays within an array.'''
        diagonal_list, arra, arrb = [], [], []
        index_increment = 0 #Value incremented at the end of each while cycle
        while index_increment < 3:
            for index, val in list(enumerate(array[index_increment])): #For index, value in index n of array a
                if index_increment == 0: #If on first cycle
                    #The first cycle of n skips the middle value in the first index of the game array, as it is not a diagonal value
                    if index == 0: #And index value is zero, then append first value of game
                        arra.append(val)
                    if index == 2:  #And last value of game. 
                        arrb.append(val)
                if index_increment == 1:
                    #The second cycle of n skips the first and last value in the second index of the game array, as they are not a diagonal value
                    if index == 1:
                        arra.append(val)
                    if index == 1:
                        arrb.append(val)
                if index_increment == 2:
                    #The third cycle of n skips the middle value in the third index of the game array. The last value is appended to the first array arra, and the first value is appended to the second array arrb
                    if index == 2:
                        arra.append(val)
                    if index == 0:
                        arrb.append(val)
            index_increment += 1 #n increment
        diagonal_list.append(arra) #Append arra to array
        diagonal_list.append(arrb) #Append arrb to array
        return diagonal_list #Return diagonal array

    def evaluate(array, column_list, diagonal_list):
        '''Function takes game list, column list, and diagonal list to evaluate whether a player won. Evaluation checks whether an array index has all values equal to 1 and 2. If all values equal within and index, then that player won and that number is returned.'''
        index_increment = 0 #Value incremented at the end of each while cycle
        while index_increment < 3:
            if index_increment == 0: #First evaluate array
                evaluate_list = array
            elif index_increment == 1: #Second evaluate column_list
                evaluate_list = column_list
            elif index_increment == 2: #Third evaluate diagonal list
                evaluate_list = diagonal_list
            for index in evaluate_list: #For each index x in evaluate_list
                first_player_increment = 0
                second_player_increment = 0
                for player_value in index: #For each value in index x 
                    if player_value == 1:
                        first_player_increment += 1
                        if first_player_increment == 3: #If there are three player 1 values in an index, player 1 won and return 1
                            return 1
                    if player_value == 2:
                        second_player_increment += 1
                        if second_player_increment == 3: #If there are three player 2 values in an index, player 2 won and return 2
                            return 2
            index_increment += 1 #n increment
        
    def player_wins(player_number, array):
        '''Description:\n  Function takes a value and prints whether player 1 or 2 won, or if game was a draw'''
        if player_number == 1 or player_number == 2:
            print('Player', str(player_number), 'wins!')
            draw(array)
            return player_number
        elif player_number == 'Draw':
            print('It\'s a draw!')
            
    def function_info():
        '''Prints function info'''
        help(dash_row)
        help(pipe_row)
        help(draw)
        help(validate)
        help(user_input)
        help(get_choice)
        help(game)
        help(columns)
        help(diagonal)
        help(evaluate)
        help(player_wins)

    '''Main Calls'''
    game_count = 1
    while True:
        winner_array = []
        winner = game()
        winner_array.append(winner)
        player_one_wins, player_two_wins = 0, 0
        continue_result = input('Do you want to play another game? Enter \'y\' to continue or \'quit\' to exit:')
        if continue_result == 'quit':
            for x in winner_array:
                if x == '1':
                    player_one_wins += 1
                if x == '2':
                    player_two_wins += 1
            if player_one_wins > 1:
                print('Player 1 won', player_one_wins, 'times!')
            elif player_one_wins == 1:
                print('Player 1 won', player_one_wins, 'time!')
            if player_two_wins > 1:
                print('Player 2 won', player_two_wins, 'times!')
            elif player_two_wins == 1:
                print('Player 2 won', player_two_wins, 'time!')
            break
    
        


    
   
