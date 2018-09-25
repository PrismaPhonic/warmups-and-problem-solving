def calculate(make_float, operation, first, second, message='The result is'):
    operations = {
        'add': lambda a, b : a + b, 
        'subtract': lambda a, b : a - b, 
        'multiply': lambda a, b : a * b, 
        'divide': lambda a, b : a / b
        }
    result = operations[operation](first, second)
    final_result = float(result) if make_float == True else int(result)
    return f"{message} {str(result)}"
