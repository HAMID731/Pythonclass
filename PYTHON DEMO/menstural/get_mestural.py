def calculate_next_period_start(last_period_date, cycle_length):
	if type(last_period_date) in [str]:
		raise TypeError	
	if type(cycle_length) in [str]:
		raise TypeError	
	return last_period_date + cycle_length

def calculate_ovulation_day(last_period_date, cycle_length):
	if type(last_period_date) in [str]:
		raise TypeError	
	if type(cycle_length) in [str]:
		raise TypeError
	return last_period_date + cycle_length - 14

def calculate_fertile_start(last_period_date, cycle_length):
	if type(last_period_date) in [str]:
		raise TypeError	
	if type(cycle_length) in [str]:
		raise TypeError
	ovulation_day = last_period_date + cycle_length - 14
	return ovulation_day - 5

def calculate_fertile_end(last_period_date, cycle_length):
	if type(last_period_date) in [str]:
		raise TypeError	
	if type(cycle_length) in [str]:
		raise TypeError
	ovulation_day = last_period_date + cycle_length - 14
	return ovulation_day + 1



