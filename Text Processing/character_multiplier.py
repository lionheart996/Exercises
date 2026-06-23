strings = input().split()
first = strings[0]
second = strings[1]
total_sum = 0

min_len = min(len(first), len(second))

for i in range(min_len):
    total_sum += ord(first[i])*ord(second[i])

if len(first) > len(second):
    for i in range(min_len, len(first)):
        total_sum += ord(first[i])
else:
    for i in range(min_len, len(second)):
        total_sum += ord(second[i])

print(total_sum)