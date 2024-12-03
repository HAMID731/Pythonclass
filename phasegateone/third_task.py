"""
initialise an empty list

prompt user to enter first number
collect number
store as first_number

prompt user to enter second number
collect number
store as second_number

prompt user to enter third number
collect number
store as third_number

using the append, add the collected number to the list
and using the sort function sort the number in decending to ascending number

iterate through the list of sorted numbers and display the number side by side and there should differ by a comma
"""

arranged_number = []

first_number= int(input("Enter first number: "))
arranged_number.append(first_number)
second_number= int(input("Enter second number: "))
arranged_number.append(second_number)
third_number= int(input("Enter third number: "))
arranged_number.append(third_number)

arranged_number.sort()

for num in arranged_number:
	print(num , end=",")