number = int(input("Enter Number Of Days: "))

if number <=5 :
	print("the fine is 50 paise")
elif number>=6 and number<=10:
	print("the fine is 1 rupee")
elif number>10 and number<30 :
	print("the fine is 5 rupee")
elif number>30 :
	print("Your Membership Is Cancelled")