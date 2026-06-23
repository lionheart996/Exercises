def todo_list_generator():
    to_do_list = []
    while True:
        text = input()
        if text == 'End':
            break
        to_do_list.append(text)

    sorted_list = sorted(to_do_list, key=lambda x: int(x.split('-')[0]))
    result_sorted_notes = [note.split('-')[1] for note in sorted_list]
    return result_sorted_notes


print(todo_list_generator())

