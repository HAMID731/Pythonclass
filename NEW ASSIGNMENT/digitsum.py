calone =int(input("ENTER A NUMBER"))
cal1= calone % 10
useless= calone%100
cal2= useless//10
cal3 = calone//100

print(f"{cal1+cal2+cal3}")