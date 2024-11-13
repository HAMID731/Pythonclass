def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

for c in range(0, 101):
    print(f"{c} C = {round(fahrenheit(c), 1)} F")
