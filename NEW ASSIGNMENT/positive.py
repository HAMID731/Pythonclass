num1 =int(input("ENTER NUMBER: "))
num2 =int(input("ENTER NUMBER: "))
num3 =int(input("ENTER NUMBER: "))
num4 =int(input("ENTER NUMBER: "))
num5 =int(input("ENTER NUMBER: "))

negative=0
positive=0
zero=0

if num1< 0:
	negative+=1
elif num1> 0:
	positive+=1
else:
	zero+=1
if num2< 0:
	negative+=1
elif num2> 0:
	positive+=1
else:
	zero+=1
if num3< 0:
	negative+=1
elif num3> 0:
	positive+=1
else:
	zero+=1
if num4< 0:
	negative+=1
elif num4> 0:
	positive+=1
else:
	zero+=1
if num5< 0:
	negative+=1
elif num5> 0:
	positive+=1
else:
	zero+=1
print(f"there are {positive} positive numbers")
print(f"there are {negative} negative numbers")
print(f"there are {zero} zero values")