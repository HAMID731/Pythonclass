x1 = int(input("Enter the x coordinate of the first point: "))
y1 = int(input("Enter the y coordinate of the first point: "))
x2 = int(input("Enter the x coordinate of the second point: "))
y2 = int(input("Enter the y coordinate of the second point: "))

if x1 == x2:
    print("The points are located on a vertical line (perpendicular to the x-axis).")
elif y1 == y2:
    print("The points are located on a horizontal line (perpendicular to the y-axis).")
else:
    print("The points are not located on a line perpendicular to an axis.")
