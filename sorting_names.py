def sort_names():
    names = input().split(', ')
    sorted_names = sorted(names, key=lambda x: (-len(x), x))
    return sorted_names

print(sort_names())