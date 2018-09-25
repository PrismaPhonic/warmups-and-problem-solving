def multiply_even_numbers(lst):
    product = 1
    for num in lst:
        if num % 2 == 0:
            product = product * num
    return product