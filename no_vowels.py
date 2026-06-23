def no_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    list = []
    for ch in text:
        if ch not in vowels:
            list.append(ch)
    return ''.join(list)

print(no_vowels("Python"))