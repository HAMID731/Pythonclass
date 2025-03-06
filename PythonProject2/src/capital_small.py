def separate_letters(text):
  uppercase = ""
  lowercase = ""
  for char in text:
    if 'A' <= char <= 'Z':
      uppercase += char
    elif 'a' <= char <= 'z':
      lowercase += char
  both = uppercase + lowercase
  return both

answer = separate_letters("SEmiColoN")
print(answer)
