total_miles = 0
total_gallons = 0
gallons = 0  

gallons = float(input("Enter the gallons used (-1 to end): "))

while gallons != -1:
    miles = float(input("Enter the miles driven: "))
    mpg = miles / gallons
    print(f"The miles/gallon for this tank was {mpg:.2f}")
    
    total_miles += miles
    total_gallons += gallons
    
    gallons = float(input("Enter the gallons used (-1 to end): ")) 

if total_gallons > 0:
    overall_mpg = total_miles / total_gallons
    print(f"The overall average miles/gallon was {overall_mpg:.2f}")
else:
    print("No data entered.")
