def flip_case(string, letter):
    return "".join([
        (char.swapcase()
        if char.lower() == letter.lower()
        else char)
        for char in string
    ])

flip_case("Hardy har har", "h") # "hardy Har Har"


[  (cha.swap() if ... else .. )
     for char in string]