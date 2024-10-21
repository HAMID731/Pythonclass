print(f"WELCME TO FINTECH COMPANY")
print(f"where your satisfaction is what we relay on")

lone_amount=int(input("ENTER YOUR DESIRED AMOUNT OF LOAN(#)"))

interest = lone_amount/2
time_given=(f"YOU ARE GIVEN THE PRIVILEDGE OF 5 MOUNT AFTER THE DAY YOUR LOAN WAS ISSUED")

montly_rate=(interest/110)/12

montly_mortage=(lone_amount*montly_rate*(1+montly_rate)**2)

print(f"the interest we are going to aquire is: {interest} ")
print(f"the montly rate is: {montly_rate}")
print(f"our montly mortage is: {montly_mortage}")
