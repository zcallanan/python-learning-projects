'''In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many
scientists have a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}'''



if __name__ == '__main__':
    import json
    import re
    from collections import Counter
    from bokeh.plotting import figure, show, output_file
    
    def json_exists(json_file):
        '''Tries reading a file, if file read return True, else False.'''
        try:
            with open(json_file, 'r') as f:
                return True
        except:
            return False

    def txt_read(file_name, json_file):
        '''Reads 'birthdays.txt' and returns a dictonary of values'''
        data_dict, file_read = {}, False
        if json_exists(json_file) == False: #Data from txt is only read if
            with open(file_name, 'r') as f:
                line = f.readline().strip()
                while line != '':
                    line = line.split(' - ')
                    data_dict[line[0]] = line[1]
                    line = f.readline().strip()
            file_read = True
            return data_dict, file_read
        else:
            return data_dict, file_read

    def json_write(data_dict, file_name, file_read):
        '''Writes data to specified json file'''
        if file_read == True:
            with open(file_name, 'w') as f:
                json.dump(data_dict, f)

    def json_read(file_name):
        '''Reads json file and returns dictionary.'''
        with open(file_name, 'r') as f:
            dictionary = json.load(f)
        return dictionary

    def intro(birth_dict):
        '''Takes and returns user input.'''
        print('Welcome to the birthday dictionary. We know the birthdays of:')
        keys = birth_dict.keys()
        for x in keys:
            print(' * ', x)
        print('----------------------------------------------\n- Enter a name to look up their birthday.\n- Enter \'add\' to add another person to the list.\n- Enter \'month\' to count how many have a birthday in a month.')
        user_input = input('Which of the preceding do you want?')
        user_input = user_input.capitalize()
        return user_input

    def get_value(birth_dict, user_input):
        '''Gets and prints value associated with key'''
        value = birth_dict.get(user_input, 'That name is not recognized!')
        if value == 'That name is not recognized!':
            result = value
            val = False
        else:
            result = '{}\'s birthday is '.format(user_input) + value + '.\n'
            val = True
        return result, val

    def date_format(date):
        '''Custom Calls:\n  None\nDescription:\n  Confirms MM/DD/YY format\nArguments:\n  date - string - MM/DD/YY'''
        pattern = re.compile(r'\d{2}/\d{2}/\d{2}')
        result = re.search(pattern, date)
        if result is not None:
            return True
        else:
            return False
    
    def add_name_date(birth_dict):
        '''Adds a name & date to birth_dict'''
        valid_name = False
        while valid_name == False:
            name = input('Enter a name with only letters:')
            if name.isalpha() == True:
                valid_name = True
                name = name.capitalize()
        valid_date = False
        while valid_date == False:
            date = input('Enter a date in the format MM/DD/YY:')
            valid_date = date_format(date)
            if valid_date == True:
                birth_dict[name] = date
                json_write(birth_dict, 'birthdays.json', True)

    def months(month_dict, birth_dict):
        '''Prints month names and the number of people who have a birthday that month'''
        value_list, month_list = [], []
        for x in birth_dict.values(): #Generate a list of split dict values
            string = x.split('/')
            value_list.append(string)
        iterate = 0
        for x in value_list: # Generate a list of only month values
            month_list.append(value_list[iterate][0])
            iterate += 1
        count_dict = Counter(month_list) #Count number of times a month appears in month_list
        for key in month_dict: #For key in month_dict
            month_list = month_dict[key]
            print(month_list)
            if key in count_dict: #If key also in count_dict
                print('"{}" : {}'.format(month_dict[key], count_dict[key])) #Then print month name and number of times it was counted
                

    def create_histogram(x, y):
        output_file("plot.html")
        p = figure()
        p.vbar(x=x, top=y, width=0.5)
        show(p)
    
    def fun():
        '''Returns help(foo)'''
        help(txt_read)
        help(json_write)
        help(json_read)
        help(get_dict)
        help(intro)
        help(get_value)
        help(date_format)
        help(add_name_date)
        help(months)
        
    '''Function Calls'''
    name_data, name_read = txt_read('birthdays.txt', 'birthdays.json')
    month_data, month_read = txt_read('months.txt', 'months.json')
    json_write(name_data, 'birthdays.json', name_read)
    json_write(month_data, 'months.json', month_read)
    
    while True:
        birth_dict = json_read('birthdays.json')
        month_dict = json_read('months.json')
        user_input = intro(birth_dict)
        if user_input == 'Add':
            add_name_date(birth_dict)
        elif user_input == 'Months':
            months(month_dict, birth_dict)
        else:
            result, val = get_value(birth_dict, user_input)
            print(result)
