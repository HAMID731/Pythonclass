scanner = input
print("How many students do you have: ")
students = int(scanner().strip())
print("How many subjects do they offer: ")
subjects = int(scanner().strip())
print("saving >>>>>>>>>>>>>>>> ")
print("\nsaved successfully\n")
print()

scores = [[0] * subjects for _ in range(students)]
totals = [0] * students
averages = [0] * students

for i in range(students):
	print(f"Entering scores for student {i + 1}:")
	for j in range(subjects):
		while True:
			print(f"Enter score for subject {j + 1}:")
			score = int(scanner().strip())
			print("saving >>>>>>>>>>>>>>>> ")
			print("\nsaved successfully\n")
			print()
			if 0 <= score <= 100:
				break
			print("Invalid score. Please enter a score between 0 and 100.")
		scores[i][j] = score
		totals[i] += score
	averages[i] = totals[i] / subjects

print("\nCLASS SUMMARY")
print("---------------------------------------------------------------------------------------------------------\n")
print("STUDENT", end="\t")
for j in range(subjects):
	print(f"SUB{j + 1}", end="\t")
print("TOT\tAVE")
print("-------------------------------------------------------------------------------------------------------------\n")
for i in range(students):
	print(f"Student{i + 1}", end="\t")
	for j in range(subjects):
		print(scores[i][j], end="\t")
	print(f"{totals[i]:.2f}\t{averages[i]:.2f}")
