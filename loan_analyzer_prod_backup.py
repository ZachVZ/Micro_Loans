"This script will display how to analyze loan data and save the results to a new csv file. "
import csv
from pathlib import Path

"""
Part 1: Automate Loan Calculations.
"""
# Loan data below
loan_costs = [500, 600, 200, 1000, 450]

# Number of loans are in the list
total_number_of_loans = len(loan_costs)
print(f" The total number of loans is {total_number_of_loans}")

# Total value of loans
total_value_of_all_loans = sum(loan_costs)
print(f" The total value of the loans is ${total_value_of_all_loans}")

# Average loan amount from the list
average_loan_amount = total_value_of_all_loans / total_number_of_loans
print(f" The average loan amount is ${average_loan_amount :.2f}")

"""
Part 2: Analyze Loan Data.
"""
# Loan data below
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
    "annual_discount_rate": .2,
}

# Below displays the Future Value and Remaining Months on the loan.
future_value = loan.get('future_value')
remaining_months = loan.get("remaining_months")
print(f" The future value is ${future_value} and the # of remaining months is {remaining_months}")

# Below displays the Present Value ("fair value") of the loan with a a minimum required return of 20% as the discount rate
present_value = loan.get("future_value") / (1+loan.get("annual_discount_rate")/12)**loan.get("remaining_months")
print(f" The present value is ${present_value :.2f}")

# The below conditional statement (an if-else statement) determines if the present value represents the loan's fair value. This provides insight as to whether we should procure the loan.
# If the present value of the loan is greater than or equal to the cost, then print "loan is worth at least the cost to buy it."
# Else, the present value of the loan is less than the loan cost, then print "loan is too expensive and not worth the price."
if present_value >= loan['loan_price']:
    print(" The loan is worth at least the cost to buy it")
else:
    print(" The loan is too expensive and not worth the price.")

"""
Part 3: Perform Financial Calculations.
"""
# Loan data below
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
    "annual_discount_rate": .2,
}

# Below defined a new function that will be used to calculate present value.
# This function includes parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
# The function returns the `present_value` for the loan.
present_value = new_loan['future_value'] / (1+loan['annual_discount_rate']/12)**new_loan['remaining_months']

# By using the function above to calculate the present value of the new loan
# If the present value of the loan is greater than or equal to the new loan price print, "the loan is worth at least the cost to buy it""
# Else print "the loan is too expensive and not worth the price."
# This will determine if its atleast worth the cost of buying it.
print(f"The present value of the loan is: {present_value:.2f}")
if present_value >= new_loan['loan_price']:
    print("the loan is worth at least the cost to buy it")
else:
    print("the loan is too expensive and not worth the price.")

"""
Part 4: Conditionally filter lists of loans.
"""
# Loan data below
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# The created empty list below will hold a filtered list of loans called `inexpensive_loans`
inexpensive_loans= []

# The loop below will run through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"] <=500:
        inexpensive_loans.append(loan)

# Print out of the `inexpensive_loans` list
print(inexpensive_loans)

"""
Part 5: Save the results.
"""
# CSV Header for the new file
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path to create the new csv file
output_path = Path("inexpensive_loans.csv")

# To display the data that will be written to the new csv file
print("writing the data to a csv file")

# To enable write to the new csvfile
with open(output_path, "w") as csvfile:

# To create csvwriter
    csvwriter = csv.writer(csvfile, delimiter= ",") 

# To write to the header row
    csvwriter.writerow(header)

# To write each row of the `loan.values()` from the `inexpensive_loans` list.
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
        print(loan.values())