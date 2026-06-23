string_explosion = input()

strength = 0
result = []

for i in range(len(string_explosion)):
    ch = string_explosion[i]

    if ch == ">":
        result.append(ch)
        strength += int(string_explosion[i + 1])

    elif strength > 0:
        strength -= 1

    else:
        result.append(ch)

print("".join(result))
