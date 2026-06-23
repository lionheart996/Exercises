def weight_sorter():
    list_of_boxers = []
    while True:
        text = input()
        if text == "End":
            break
        list_of_boxers.append(text)

    sorted_boxers = sorted(list_of_boxers, key=lambda x: int(x.split("-")[1]), reverse=True)
    result_boxers = [boxer.split('-')[0] for boxer in sorted_boxers ]
    return result_boxers

print(weight_sorter())