annual_income = int(input("Enter Annual Income: "))

if annual_income <= 9875:
    print("10%")
elif 9876 <= annual_income <= 40125:
    print("12%")
elif 40126 <= annual_income <= 85525:
    print("22%")
elif annual_income >= 84526:
    print("24%")
