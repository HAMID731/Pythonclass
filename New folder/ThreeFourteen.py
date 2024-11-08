approximation_of_pi = 0
terms = int(input("Enter the number of terms to approximate π: "))

print("Approximation of π:")
for count in range(terms):
    approximation_of_pi += (-1)**count / (2 * count + 1)
    pi_value = 4 * approximation_of_pi
    print(f"After {count + 1} terms: {pi_value}")
