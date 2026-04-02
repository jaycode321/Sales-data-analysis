import numpy as np
import calendar

# Sales details Generation
sales_data = np.random.randint(1000, 5000, (5, 12))
print(f"5 Years sales records: \n{sales_data}\n")

#yearly total
year_total = sales_data.sum(axis = 1)
years  = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]
for t, y in zip(year_total, years):
	print(f"Total sales in {y} is: {t}/=")
	
#Monthly average
monthly_avg = sales_data.mean(axis = 0)
months = list(calendar.month_name)[1:]
print("\nMonthly averages in each year:")
for  m, a in zip(months, monthly_avg):
	print(f"Monthly average in {m} is {a}/=")
	
#year with highest Q4 sales
q4_sales = sales_data[:, 9:].sum(axis = 1)
best_year = years[np.argmax(q4_sales)]
print(f"\nThe year that had highest Q4 sales is {best_year}")

#Best perfoming month
best_month  = months[np.argmax(monthly_avg)]
print(f"\nThe overall best month is {best_month}")