def convert_to_snake_case_iteration(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')
    
    return clean_snake_cased_string

def main():
    print(convert_to_snake_case_iteration('aLongAndComplexString'))

if __name__ == '__main__':
    main()
