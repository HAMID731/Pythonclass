def find_count(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    return count

