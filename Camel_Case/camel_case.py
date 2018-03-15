def alternate_case(string):
    string_list = list(string)
    alternate_string = ''

    index = 0

## loops through each char in a list
    for char in string_list:

        if index % 2 == 0: #Modulous operatior to check if it equals 0
            alternate_string += char.lower() #if yes, charter is lowercase
        else:
            alternate_string += char.upper() #else uppercase

        index += 1 # increments index counter

    return alternate_string  #returns new_camel case string

