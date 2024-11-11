pie = 3.147

print("Enter department\n1. circle\n2. rectangle\n3. triangle\nEnter Number>>>>>>")

answer = int(input())

match answer:
    case 1:
        print("circle")
        radius = float(input())
        sum1 = pie * (radius * radius)
        print("The area of the circle is", sum1)

    case 2:
        print("rectangle")
        print("Enter length:")
        length = float(input())
        print("Enter width:")
        width = float(input())
        sum2 = length * width
        print("The area of the rectangle is", sum2)

    case 3:
        print("triangle")
        print("Enter base:")
        base = float(input())
        print("Enter height:")
        height = float(input())
        sum3 = 0.5 * (base * height)
        print("The area of the triangle is", sum3)
