sequence = input().split()
lower_sequence = [ch.lower() for ch in sequence]
dict = {}
for char in lower_sequence:
    if char not in dict:
        dict[char] = 1
    else:
        dict[char] += 1
list_odd_occurrences = []
for key, value in dict.items():
    if value % 2 != 0:
        list_odd_occurrences.append(key)

print(', '.join(list_odd_occurrences))
