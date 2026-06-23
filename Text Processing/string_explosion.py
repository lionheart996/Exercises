# string_explosion = input()
#
# strength = 0
# result = []
#
# for i in range(len(string_explosion)):
#     ch = string_explosion[i]
#
#     if ch == ">":
#         result.append(ch)
#         strength += int(string_explosion[i + 1])
#
#     elif strength > 0:
#         strength -= 1
#
#     else:
#         result.append(ch)
#
# print("".join(result))
from multiprocessing.reduction import steal_handle

string = input()

strength = 0
output = ''

for index in range(len(string)):
    if strength > 0 and string[index] != '>':
        strength -= 1
    elif string[index] == '>':
        output += string[index]
        strength += int(string[index+1])
    else:
        output += string[index]

print(output)



















