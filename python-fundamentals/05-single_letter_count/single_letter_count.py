def single_letter_count(string, character):
    return len([char for char in string if char.lower() == character.lower()])