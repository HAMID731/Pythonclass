age = int(input("Enter Age: "))

if age <= 12:
    print("CHILD")
elif 13 <= age <= 17:
    print("ADULT")
elif 18 <= age <= 64:
    print("TEEN")
elif age >= 65:
    print("SENIOR")
