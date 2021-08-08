total_cost = 0
current_savings = 0
r = 0.04
annual_salary = 0
portion_saved = 0
semi_annual_raise = 0

annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

portion_down_payment = 0.25 * total_cost
monthly_salary = annual_salary / 12


# count number of months it takes for savings to reach down payment amount
# calculate gain from investment from savings and add to savings
# add portion saved from salary to savings
# add raise every 6 months and update new monthly salary
# increment month counter
# repeat until you have enough for the down payment

n = 0
while(current_savings < portion_down_payment):
	current_savings += current_savings * r / 12
	current_savings += monthly_salary * portion_saved
	if (n % 6 == 0) & (n != 0):
		annual_salary *= (1 + semi_annual_raise)
		monthly_salary = annual_salary / 12
	n += 1
	
print('Number of months:', n)