def calculate_totals(goods, prices, quantities):
	subtotal = 0
	for i in range(len(goods)):
		subtotal += prices[i] * quantities[i]

	discount = subtotal * 0.1 if subtotal > 100 else 0
	vat = (subtotal - discount) * 0.075
	final_total = subtotal - discount + vat

	print("\n--- Purchase ---")
	print("Items Purchased:")
	for i in range(len(goods)):
		print(f"Item {i}: Goods = {goods[i]}, Price = {prices[i]}, Quantity = {quantities[i]}, Subtotal = {prices[i] * quantities[i]}")

	print(f"\nSubtotal: {subtotal}")
	print(f"Discount: {discount}")
	print(f"VAT (7.5%): {vat}")
	print(f"Final Total: {final_total}")

	return final_total

def ask_for_payment(final_total):
	amount_paid = float(input("\nEnter the amount paid by the customer: "))

	if amount_paid < final_total:
		print(f"Insufficient payment. Please pay at least: {final_total}")

	change = amount_paid - final_total
	print(f"Amount Paid: {amount_paid}")
	print(f"Change Given: {change}")

goods = []
prices = []
quantities = []

name = input("Enter your name: ")
continue_input = "yes"

while continue_input == "yes":
	goods.append(input("Enter name of goods: "))
	prices.append(float(input("Enter price of goods: ")))
	quantities.append(int(input("Enter quantity of goods: ")))

	continue_input = input("Do you want to buy more (yes or no): ").lower()

final_total = calculate_totals(goods, prices, quantities)
ask_for_payment(final_total)
