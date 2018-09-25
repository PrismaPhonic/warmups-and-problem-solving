def is_palindrome(str):
    str_list = list(str.lower().replace(' ',''))
    return str_list == str_list[::-1]