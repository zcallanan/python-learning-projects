if __name__ == '__main__':
    import random
    
    def pick_word():
        '''Reads 'sowpods.txt', saves all words to a list and prints/returns a random word from that list'''
        with open('sowpods.txt') as f: #Read 'sowpods.txt'
            text = f.readlines()  #.readlines() returns a list of all lines as strings ending in \n
        word_list = [x.strip() for x in text] #For all strings in text, strip() newlines
        word = random.choice(word_list) #Make a random choice of a word from a word list
        return word

    def create_hangman_word(chosen_word):
        '''Creates the original hangman string as series of underscores and white space.'''
        chosen_word, s, hangman_word = list(chosen_word), '_ ', ''
        for x in range(len(chosen_word)):
            hangman_word += s
        return hangman_word

    def modify_hangman_word(hangman_word, user_input, chosen_word, incorrect_guess):
        '''Adds correctly guessed letters to hangman word and keeps track of incorrect guesses.'''
        hangman_word_list = list(hangman_word)
        chosen_word_list = list(enumerate(chosen_word))
        word_length = int(len(hangman_word_list) / 2)
        increment = 0
        for index, value in chosen_word_list:
            if value == user_input:
                hangman_word_list[index * 2] = value
                hangman_word_list[index * 2 + 1] = ' '
            else:
                increment += 1
        if increment == word_length:
            incorrect_guess += 1
            if incorrect_guess < 5:
                print('You guessed incorrectly! You have', 6 - incorrect_guess, 'incorrect guesses left!')
            elif incorrect_guess < 6:
                print('You guessed incorrectly! You have', 6 - incorrect_guess, 'incorrect guess left!')

        hangman_word = ''.join(hangman_word_list)
        return hangman_word, incorrect_guess
                
    def evaluate_win(chosen_word, hangman_word):
        '''Returns True when the chosen word = guessed word.'''
        hangman_word = hangman_word.split(' ')
        hangman_word = ''.join(hangman_word)
        if chosen_word == hangman_word:
            return True

    def duplicate_guesses(user_input, guessed_letters):
        '''If a letter guessed previously is guessed again, return True'''
        for x in guessed_letters:
            if x == user_input:
                return True
            
    def draw_hangman(incorrect_guess):
        '''Draws hangman progression as user makes incorrect guesses.'''
        hangman = [[' ',' ',' ',' ',' ',' ',' '],['O',' ',' ',' ',' ',' ',' '],['O',' ','|',' ','|',' ',' '],['O','\\','|',' ','|',' ',' '],['O','\\','|','/','|',' ',' '],['O','\\','|','/','|',' /',' '],['O','\\','|','/','|',' /','\\']]
        n = incorrect_guess
        for x in hangman:
            line_one = hangman[incorrect_guess][0]
            line_two = hangman[incorrect_guess][1], hangman[incorrect_guess][2], hangman[incorrect_guess][3]
            line_three = hangman[incorrect_guess][4]
            line_four = hangman [incorrect_guess][5], hangman [incorrect_guess][6]
        framework = print('  ------'), print('  |    |'), print('  %s    |' % line_one), print(' %s%s%s   |' % line_two), print('  %s    |' % line_three), print(' %s%s    |' % line_four), print('--------')    


    def fun():
        help(pick_word)
        help(create_hangman_word)
        help(modify_hangman_word)
        help(evaluate_win)
        help(duplicate_guesses)
        help(draw_hangman)
        help(get_input)

    def get_input(guessed_letters, guesses):
        '''Description:\n  Loops user input request and protects against duplicates'''
        while True:
            user_input = input('Guess your letter or type \'quit\' to exit:')
            user_input = user_input.strip()
            if user_input == 'quit':
                return user_input
            elif user_input == 'fun':
                fun()
            elif user_input.isalpha() == False:
                print('That\'s not a letter!')
            else:
                user_input = user_input.upper()
                if duplicate_guesses(user_input, guessed_letters) == True:
                   print('You\'ve guessed that letter already!')
                else:
                    guessed_letters.append(user_input)
                    guesses += 1
                    return user_input, guessed_letters, guesses

    '''Function Calls'''
    while True:
        guesses, incorrect_guess = 1, 0
        guessed_letters = []
        chosen_word = pick_word()
        hangman_word = create_hangman_word(chosen_word)

        while True:
            draw_hangman(incorrect_guess)
            print(hangman_word)
            user_input, guessed_letters, guesses = get_input(guessed_letters, guesses)
            if user_input == 'quit':
                break
            hangman_word, incorrect_guess = modify_hangman_word(hangman_word, user_input, chosen_word, incorrect_guess)
            if incorrect_guess > 5:
                draw_hangman(incorrect_guess)
                print('You guessed incorrectly 6 times and were hanged! You lose!')
                break
            print(hangman_word)
            if evaluate_win(chosen_word, hangman_word) == True:
                print('You guessed', guesses, 'times to discover the entire word!', chosen_word)
                break
        play_again = input('Would you like to play again? Enter \'quit\' to exit, or any key to continue playing:')
        if play_again == 'quit':
            break
        
                    

