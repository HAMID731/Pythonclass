def swap_first_letters(word1, word2):
    if not word1 or not word2:
        if not word1 and not word2:
            return "", ""
        elif not word1:
            return "", word2
        else:
            return word1, ""
    else:
        return word2[0] + word1[1:], word1[0] + word2[1:]