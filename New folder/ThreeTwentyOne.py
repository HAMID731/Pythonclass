print("Pythagorean triples for side lengths up to 20:")
for a in range(1, 21):
    for b in range(a, 21):  
        for c in range(b, 21):
            if a**2 + b**2 == c**2:
                print(f"({a}, {b}, {c})")
