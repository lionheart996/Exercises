number_of_wagons = int(input())
wagons = []
for i in range(number_of_wagons):
    wagons.append(0)
while True:
    command = input().split()
    if command[0] == "End":
        break
    if command[0] == "add":
        wagons[-1] += int(command[1])

    elif command[0] == "insert":
        wagon_number = int(command[1])
        people_in = int(command[2])
        wagons[wagon_number] += people_in
    else:
        wagon_number = int(command[1])
        people_out = int(command[2])
        wagons[wagon_number] -= people_out

print(wagons)