def count_letters(text):
  letter_counts = {}
  for letter in text:
    if letter.isalpha():
      letter = letter.lower()
      if letter in letter_counts:
        letter_counts[letter] += 1
      else:
        letter_counts[letter] = 1
  return letter_counts

