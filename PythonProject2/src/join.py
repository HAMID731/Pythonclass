def join_clean(parts):
    cleaned_parts = []
    for part in parts:
        for char in part:
            if char.isalpha():
                cleaned_parts.append(char)

    word = "".join(cleaned_parts)
    return word