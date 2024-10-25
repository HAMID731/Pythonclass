
import math

def calculate_polygon_area():
    num_sides = int(input("Enter the number of sides: "))
    side_length = float(input("Enter the length of each side: "))

    
    area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))
    
    print(f"The area of the polygon is: {area:.2f} square units")

calculate_polygon_area()