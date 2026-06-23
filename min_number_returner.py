def min_number(int_1, int_2, int_3):
    list = [int_1, int_2, int_3]
    list.sort()
    return list[0]

def min_number_2(*args):
    list = [*args]
    n= len(list)
    for i in range(n):
        for j in range(n-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


min_number(45, 8, 9)

print(min_number(45, 8, 9))

print(min_number_2(22, 56, 89, 45, 12, 65, 12, 25))