def flip_case(string, char):
    flipped = ''
    for c in string:
        if c.lower() == char.lower():
            flipped += c.swapcase()
        else:
            flipped += c
    return flipped