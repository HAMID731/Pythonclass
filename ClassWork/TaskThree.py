row = 1
column = 1
while column<=5:
	column =column + 1
	row = row + 1
	while row < column:
		row = row + 1
		print(f"*",end="")
	print()