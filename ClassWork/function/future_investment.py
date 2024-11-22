def get_investment(investment_amount ,monthly_interest_rate ,month):
	result = 0
	result = investment_amount*(1+monthly_interest_rate**month)
	return result