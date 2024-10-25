largest=0
smallest=0
for count in range(1,11):
	score=int(input(f"enter number {count} : "))
	if score>0 and score<=100:
		if score>largest:
			largest=score
	score=int(input(f"enter number {count} : "))
	if score>0 and score<=100:
		if score<smallest:
			smallest=score

print(f"THE LARGEST IS {largest}")
print(f"THE SMALLEST IS {smallest}")