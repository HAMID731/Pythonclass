validator=1
largest=0
while validator<=10:
	score=int(input("ENTER NUMBER"))
	if score > largest:
		largest=score
		validator=validator+1
		validator+=1
	else:
		print("invalid input")
		validator-=1

print(f"largest is{largest}")