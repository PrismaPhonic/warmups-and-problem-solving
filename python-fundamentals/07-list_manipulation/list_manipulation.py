def list_manipulation(lst, method, loc, element=None):
    if method == 'add':
        if loc == 'beginning':
            lst.insert(0, element)
        elif loc == 'end':
            lst.insert(len(lst), element)
        return lst
    elif method == 'remove':
        if loc == 'beginning':
            return lst.pop(0)
        if loc == 'end':
            return lst.pop(-1)