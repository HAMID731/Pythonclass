#write a function that takes a string and returns the number of vowel in the string



def user_inp(word):

	user_input = input("Enter a phrase: ")

	phrase = (user_input. replace('of', '')). split()

	acronym = ""

	for wor in phrase:
		 acronym = acronym + word[0]. upper()

user_input = input("Enter a phrase: ")
print(user_inp(user_input))