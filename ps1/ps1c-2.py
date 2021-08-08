total_cost = 1000000
r = 0.04
annual_salary = 0
portion_saved = 0
current_savings = 0
semi_annual_raise = 0.07
months = 36
num_steps = 0
epsilon = 100

annual_salary = int(input('Enter your annual salary: '))

portion_down_payment = 0.25 * total_cost
monthly_salary = annual_salary / 12

# what are we trying to find - portion saved %
# current_savings is closest to down payment cost in 36 months

# loop runs while current_savings - downpayment is greater than 100$
# sets the portion_saved
# calculates savings and difference from downpayment
# updates new portion_saved

lo = 0
hi = 10000
portion_saved = (lo + hi) // 2

while (abs(portion_down_payment - current_savings) >= epsilon):
	print('step',num_steps,'low',lo,'high',hi,(portion_saved / 10000))
	num_steps += 1
	current_savings = 0
	new_annual_salary = annual_salary
	
	# this loop calculates the savings in 36 months
	n = 0
	while n <= 36:
		current_savings += current_savings * r / 12
		current_savings += monthly_salary * portion_saved / 10000
		if (n % 6 == 0) & (n != 0):
			new_annual_salary *= (1 + semi_annual_raise)
			monthly_salary = new_annual_salary / 12
		n += 1
	
	if (portion_down_payment - current_savings) > epsilon:
		lo = portion_saved
	else:
		hi = portion_saved
	portion_saved = (lo + hi) // 2
	print('savings',current_savings,'down',portion_down_payment)
	if lo == 9999:
		print('Not able to save enough in 36 months')
		break
