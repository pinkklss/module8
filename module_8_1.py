def add_everything_up(a, b):
    if isinstance(a, (int, float)) and isinstance(b, str):
        return f'{a}{b}'
    elif isinstance(b, (int, float)) and isinstance(a, str):
        return f'{a}{b}'
    else:
        try:
            return a + b
        except TypeError:
            return f'{a}{b}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
