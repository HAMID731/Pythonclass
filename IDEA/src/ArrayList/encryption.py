def rot13(text):
    result = ""
    for char in text:
        if char == 'a': result += 'n'
        elif char == 'b': result += 'o'
        elif char == 'c': result += 'p'
        elif char == 'd': result += 'q'
        elif char == 'e': result += 'r'
        elif char == 'f': result += 's'
        elif char == 'g': result += 't'
        elif char == 'h': result += 'u'
        elif char == 'i': result += 'v'
        elif char == 'j': result += 'w'
        elif char == 'k': result += 'x'
        elif char == 'l': result += 'y'
        elif char == 'm': result += 'z'
        elif char == 'n': result += 'a'
        elif char == 'o': result += 'b'
        elif char == 'p': result += 'c'
        elif char == 'q': result += 'd'
        elif char == 'r': result += 'e'
        elif char == 's': result += 'f'
        elif char == 't': result += 'g'
        elif char == 'u': result += 'h'
        elif char == 'v': result += 'i'
        elif char == 'w': result += 'j'
        elif char == 'x': result += 'k'
        elif char == 'y': result += 'l'
        elif char == 'z': result += 'm'
        else:
            result += char
    return result

print(rot13("hello"))
