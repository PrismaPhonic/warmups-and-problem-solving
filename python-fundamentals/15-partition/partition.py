def partition(lst, callback):
    list1 = []
    list2 = []
    for element in lst:
        if callback(element):
            list1.append(element)
        else:
            list2.append(element)
    return [list1, list2]
