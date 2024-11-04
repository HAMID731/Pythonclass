total_miles = 0
total_gallons = 0

miles_driven = int(input("Enter miles driven (or -1 to exit): "))

while miles_driven != -1:
    gallons_used = int(input("Enter gallons used: "))
    
    mpg = miles_driven / gallons_used
    total_miles += miles_driven
    total_gallons += gallons_used
    print(f"Miles per gallon for this trip: {mpg:.2f}")

    if total_gallons > 0:
        overall_mpg = total_miles / total_gallons
        print(f"Combined miles per gallon: {overall_mpg:.2f}")

    miles_driven = int(input("Enter miles driven (or -1 to exit): "))

print("Exiting program.")
