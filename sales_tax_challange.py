# Constants
PAINT_REQUIRED_PER_SQFT = 1 / 115  # 1 gallon per 115 square feet
LABOR_REQUIRED_PER_SQFT = 8 / 115  # 8 hours per 115 square feet
LABOR_COST_PER_HOUR = 20.00  # $20.00 per hour

# Input from user
square_feet = float(input("Enter the square feet of wall space to be painted: "))
paint_price_per_gallon = float(input("Enter the price of the paint per gallon: $"))

# Calculations
gallons_of_paint_required = square_feet * PAINT_REQUIRED_PER_SQFT
hours_of_labor_required = square_feet * LABOR_REQUIRED_PER_SQFT
cost_of_paint = gallons_of_paint_required * paint_price_per_gallon
labor_charges = hours_of_labor_required * LABOR_COST_PER_HOUR
total_cost = cost_of_paint + labor_charges

# Display results
print("Number of gallons of paint required:", gallons_of_paint_required)
print("Hours of labor required:", hours_of_labor_required)
print("Cost of the paint: $", format(cost_of_paint, ".2f"))
print("Labor charges: $", format(labor_charges, ".2f"))
print("Total cost of the paint job: $", format(total_cost, ".2f"))
