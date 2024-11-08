def is_prime(num):
	if num < 2:
		return "number must be greater than 1"
	if num == 2:
		return True
	for value in range(3,num):
		if num % value ==0:
			return False
	return True

result = int(input("Slot in number: "))

print(is_prime(result))