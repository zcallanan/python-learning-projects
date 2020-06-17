

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
        '''Returns a string with len(chosen_word) underscores'''
        chosen_word, s, hangman_word = list(chosen_word), '_ ', ''
        for x in range(len(chosen_word)):
            hangman_word += s
        return hangman_word
            
    def modify_hangman_word(hangman_word, user_input, chosen_word):
        '''Adds correctly guessed characters to the underscore string'''
        hangman_word_list = list(hangman_word)
        chosen_word_list = list(enumerate(chosen_word))
        for index, value in chosen_word_list:
            if value == user_input:
                hangman_word_list[index * 2] = value
                hangman_word_list[index * 2 + 1] = ' '

        hangman_word = ''.join(hangman_word_list)
        return hangman_word
                
    def evaluate_win(chosen_word, hangman_word):
        '''Did you win?'''
        hangman_word = hangman_word.split(' ')
        hangman_word = ''.join(hangman_word)
        if chosen_word == hangman_word:
            return True

    def duplicate_guesses(user_input, guessed_letters):
        '''If a letter guessed previously is guessed again, return True'''
        for x in guessed_letters:
            if x == user_input:
                return True

    def fun():
        help(pick_word)
        help(duplicate_guesses)
        help(get_input)

    def get_input(guessed_letters):
        '''Loops user input request and protects against duplicates'''
        while True:
            user_input = input('Guess your letter or type \'quit\' to exit:')
            user_input = user_input.strip()
            if user_input == 'quit':
                return user_input, 0
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
                    return user_input, guessed_letters

    '''Function Calls'''
    guesses = 1
    guessed_letters = []
    chosen_word = pick_word()
#     print('chosen word:', chosen_word)
    hangman_word = create_hangman_word(chosen_word)
    print(hangman_word)

    while True:
        user_input, guessed_letters = get_input(guessed_letters)
        if user_input == 'quit':
            break
        hangman_word = modify_hangman_word(hangman_word, user_input, chosen_word)
        print(hangman_word)
        guesses += 1
        if evaluate_win(chosen_word, hangman_word) == True:
            print('You guessed', guesses, 'times to discover the entire word!', chosen_word)
            break
    
                
