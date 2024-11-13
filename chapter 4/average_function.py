def average(first, *args):
    total = first
    count = 1
    for num in args:
        total += num
        count += 1
    return total / count
