num1 = int(input("enter weight in pounds: "))
num2 = int(input("enter height in inches: "))

cal1= num1*0.45359237
cal2= num2*0.0254

sum = cal1 / cal2**2
print(f"BMI is  {sum:.2f}")