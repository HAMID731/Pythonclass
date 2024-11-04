total_sales = 0
commission_rate = 0.09
base_pay = 200

print("Enter the value of items sold by the salesperson (enter -1 to finish):")

while True:
    sale = float(input())

    if sale == -1:
        break

    total_sales += sale

total_earnings = base_pay + (total_sales * commission_rate)
print(f"Total earnings: ${total_earnings:.2f}")

exceeds_threshold = total_sales > 5000
if exceeds_threshold:
    print("Total sales exceeded $5000.")
else:
    print("Total sales did not exceed $5000.")
