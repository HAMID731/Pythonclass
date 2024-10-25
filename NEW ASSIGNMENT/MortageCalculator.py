print(f"WELCOME TO FINTECH COMPANY")
print(f"where your satisfaction is what we relay on")

loan_amount=int(input("ENTER YOUR DESIRED AMOUNT OF LOAN(#): "))
interest_rate=int(input("ENTER YOUR interest rate: "))

time_given=(f"YOU ARE GIVEN THE PRIVILEDGE OF 5 MOUNT AFTER THE DAY YOUR LOAN WAS ISSUED")

duration=int(input("HOW MANY YEARS SHOULD YOU BE GIVEN TO REPAY"))
montly_rate=(interest_rate/100)/12
sum_amount=duration*12

montly_mortage=loan_amount*montly_rate*(1+montly_rate)**sum_amount/ ((1+montly_rate)**sum_amount-1)

print(f"enter the duration in year : ${montly_mortage:.2f}")
