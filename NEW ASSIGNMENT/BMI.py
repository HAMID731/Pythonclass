weight_kilogram =int(input("ENTER YOUR WEIGHT (KILOGRAM)"))
height_meter =int(input("ENTER YOUR HEIGHT (METER)"))

bmi= weight_kilogram / (height_meter*height_meter)

print(f"YOUR BODY MASS INDEX IS {bmi:.2F}")