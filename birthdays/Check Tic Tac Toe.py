'''Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone
has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a
diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be
one winner.'''

if __name__ == '__main__':

    game = [[1, 2, 1], [0, 1, 2], [0, 2, 1]] #Hardcoded tic tac toe board

    '''Function takes the row array and converts it to three column arrays within an array.'''
    def column_list(data):
        array, arra, arrb, arrc = [], [], [], []
        index_increment = 0 #Value incremented at the end of each while cycle
        while index_increment < 3:
            for index, val in list(enumerate(data[index_increment])): #For index, value in index n of array a
                if index == 0: #If index of array (which is in the larger array) is equal to zero
                    arra.append(val) #Then append value to array arra
                elif index == 1:
                    arrb.append(val)
                elif index == 2:
                    arrc.append(val)
            index_increment += 1 #n increment
        array.append(arra) #Append arra to array
        array.append(arrb) #Append arrb to array
        array.append(arrc) #Append arrc to array
        return array #Return column array

    '''Function takes the row array and converts it to two diagonal value arrays within an array.'''
    def diagonal(data):
        array, arra, arrb = [], [], []
        index_increment = 0 #Value incremented at the end of each while cycle
        while index_increment < 3:
            for index, val in list(enumerate(data[index_increment])): #For index, value in index n of array a
                if index_increment == 0: #If on first cycle
                    #The first cycle of n skips the middle value in the first index of the game array, as it is not a diagonal value
                    if index == 0: #And index value is zero, then append first value of game
                        arra.append(val)
                    if index == 2:  #And last value of game. 
                        arrb.append(val)
                if index_increment == 1:
                    #The second cycle of n skips the first and last value in the second index of the game array, as they are not a diagonal values
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
        array.append(arra) #Append arra to array
        array.append(arrb) #Append arrb to array
        return array #Return diagonal array

    '''Function takes game list, column list, and diagonal list to evaluate whether a player won. Evaluation
    checks whether an array index has all values equal to 1 and 2. If all values equal within and index, then that
    player won and that number is returned.'''
    def evaluate(game_list, column_list, diagonal_list):
        index_increment = 0 #Value incremented at the end of each while cycle
        while index_increment < 3:
            if index_increment == 0: #First evaluate game_list
                array = game_list
            elif index_increment == 1: #Second evaluate column_list
                array = column_list
            elif index_increment == 2: #Third evaluate diagonal list
                array = diagonal_list
            for index in array: #For each index x in array
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
        
    '''Function takes a value and prints whether player 1 or 2 won, or if game was a draw. Integer 1 or 2 passed
    as an argument is converted to a string for printing.'''       
    def player_wins(player_number):
        if player_number == 1 or player_number == 2:
            print('Player', str(player_number), 'wins!')
        else:
            print('It\'s a draw!')

    '''Function Calls'''
    game_columns = column_list(game)
    diagonals = diagonal(game)
    result = evaluate(game, game_columns, diagonals)
    player_wins(result)
    
    
                
