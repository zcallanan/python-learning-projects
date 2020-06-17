

if __name__ == '__main__':
    '''Reads 'sowpods.txt, saves all words to a list and prints/returns a random word from that list'''
    import random
    def pick_word():
        with open('sowpods.txt') as f: #Read 'sowpods.txt'
            text = f.readlines()  #.readlines() returns a list of all lines as strings ending in \n
        word_list = [x.strip() for x in text] #For all strings in text, strip() newlines
        word = random.choice(word_list) #Make a random choice of a word from a word list
        print(word)
        return word
    '''Function Calls'''
    chosen_word = pick_word()
  

    
        
