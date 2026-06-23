text = input().split()

for word in text:
    if word.startswith(':'):
        print(word[:2])

