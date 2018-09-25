def multiple_letter_count(string):
    string = string.lower()
    return {char: string.count(char) for char in string}