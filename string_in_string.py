def count_copies(source, target) -> int:
    source_len = len(source)
    target_letter_index = 0
    loop_counter = 0
    copies = 0
    while target_letter_index < len(target):
        target_letter = target[target_letter_index]
        index = loop_counter % source_len
        if index == 0:
            copies += 1
        if source[index] == target_letter:
            target_letter_index += 1
        loop_counter += 1
    return copies


source = "ap"
target = "papa"

print(count_copies(source, target))
