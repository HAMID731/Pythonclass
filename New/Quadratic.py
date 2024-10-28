import math

print("Quadratic Equation Solver (ax^2 + bx + c = 0)")

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

determinant = b**2 - 4*a*c

if determinant > 0:
        root1 = (-b + math.sqrt(determinant)) / (2*a)
        root2 = (-b - math.sqrt(determinant)) / (2*a)
        print("Roots are real and different.")
        print(f"Root 1 = {root1}")
        print(f"Root 2 = {root2}")
elif determinant == 0:
        root = -b / (2*a)
        print("Roots are real and equal.")
        print(f"Root = {root}")
else:
        print("cannot solve")
