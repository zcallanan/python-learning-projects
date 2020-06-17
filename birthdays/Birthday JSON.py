if __name__ == '__main__':
    import json
    import re
    
    def txt_read():
        '''Custom Calls:\n  None\nDescription:\n  Reads 'birthdays.txt' and returns a dictonary of values\nArguments:\n  None'''
        data = {}
        with open('birthdays.txt', 'r') as f:
            line = f.readline().strip()
            while line != '':
                line = line.split(' - ')
                data[line[0]] = line[1]
                line = f.readline().strip()
        return data

    def json_write(data):
        with open('birthdays.json', 'w') as f:
            json.dump(data, f)

    def json_read():
        ''''''
        with open('birthdays.json', 'r') as f:
            birth_dict = json.load(f)
        return birth_dict

    def intro(birth_dict):
        print('Welcome to the birthday dictionary. We know the birthdays of:')
        keys = birth_dict.keys()
        for x in keys:
            print(' * ', x)
        user_input = input('Who\'s birthday do you want to look up, or add another name and birthday by entering \'add\'?')
        user_input = user_input.capitalize()
        return user_input

    def get_value(birth_dict, user_input):
        value = birth_dict.get(user_input, 'That name is not recognized!')
        if value == 'That name is not recognized!':
            result = value
            val = False
        else:
            result = '{}\'s birthday is '.format(user_input) + value + '.'
            val = True
        return result, val

    def regex(date):
        pattern = re.compile(r'\d{2}/\d{2}/\d{2}')
        result = re.search(pattern, date)
        if result is not None:
            return True
        else:
            return False
    
    def add_name_date(birth_dict):
        valid_name = False
        while valid_name == False:
            name = input('Enter a name with only letters:')
            if name.isalpha() == True:
                valid_name = True
                name = uppercase(name)
        valid_date = False
        while valid_date == False:
            date = input('Enter a date in the format MM/DD/YY:')
            valid_date = regex(date)
            if valid_date == True:
                birth_dict[name] = date
                json_write(birth_dict)
        
    '''Function Calls'''
    data = txt_read()
    json_write(data)
    
    while True:
        birth_dict = json_read()
        user_input = intro(birth_dict)
        if user_input == 'Add':
            add_name_date(birth_dict)
        else:
            result, val = get_value(birth_dict, user_input)
            print(result)
        
        
        

    

