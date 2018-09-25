def mode(lst):
    element_counts = {num: lst.count(num) for num in lst}
    highest = max(element_counts.values())
    for num, count in element_counts.items():
        if count == highest:
            return num