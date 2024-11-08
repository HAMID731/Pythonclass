#write a function that takes a string and returns the number of vowel in the string




def get_number_of_vowels(vowel):
	count = 0

	for word in vowel:
		if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u' or word == 'A' or word == 'E' or word == 'I' or word == 'O' or word == 'U' :
			count += 1
		else:
			print = ("There is no vowel in this word")
	return count



hamid = input("Enter words: ")

print(get_number_of_vowels(hamid))