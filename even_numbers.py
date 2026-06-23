def even_numbers(*args):
    evens = filter(lambda x: x % 2 == 0, args)
    return list(evens)

evens = even_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(evens)