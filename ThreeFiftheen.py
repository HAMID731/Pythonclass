e_approx = 0
factorial = 1  # Initialize factorial value for 0!

for n in range(10):
    if n > 0:
        factorial *= n  # Update factorial iteratively
    e_approx += 1 / factorial
    print(f"e approximation after {n + 1} terms: {e_approx}")
