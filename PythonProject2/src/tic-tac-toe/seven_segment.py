def display_digit(digit):
    segments = {
        '0': ['a', 'b', 'c', 'd', 'e', 'f'],
        '1': ['b', 'c'],
        '2': ['a', 'b', 'd', 'e', 'g'],
        '3': ['a', 'b', 'c', 'd', 'g'],
        '4': ['b', 'c', 'f', 'g'],
        '5': ['a', 'c', 'd', 'f', 'g'],
        '6': ['a', 'c', 'd', 'e', 'f', 'g'],
        '7': ['a', 'b', 'c'],
        '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        '9': ['a', 'b', 'c', 'd', 'f', 'g']
    }

    if digit not in segments:
        return "Invalid digit"

    on = segments[digit]

    lines = ["", "", "", "", ""]

    lines[0] = " " + ("-" if 'a' in on else " ") * 3 + " "
    lines[1] = ("|" if 'f' in on else " ") + " " * 3 + ("|" if 'b' in on else " ")
    lines[2] = " " + ("-" if 'g' in on else " ") * 3 + " "
    lines[3] = ("|" if 'e' in on else " ") + " " * 3 + ("|" if 'c' in on else " ")
    lines[4] = " " + ("-" if 'd' in on else " ") * 3 + " "

    for line in lines:
        print(line)

display_digit("0")