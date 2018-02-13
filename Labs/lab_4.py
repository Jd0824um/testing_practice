def alternate_case(string):
    string_list = list(string)
    alternate_string = ''

    index = 0


    for char in string_list:

        if index % 2 == 0:
            alternate_string += char.lower()
        else:
            alternate_string += char.upper()

        index += 1

    return alternate_string

