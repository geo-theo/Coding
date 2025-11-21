# Expand your solution to the "Continuously compounded interest" exercise from Secction 1.2 to write a table giving
# the total amount paid and the remaining principal after each monthly payment.

# use escape characters like: \t, \n, \r, etc.

import stdio
import sys
import math

###########################
##### Code from 1.2.1 #####
###########################

# save variables to plug into formula
t = float(sys.argv[1])
p = float(sys.argv[2])
r = float(sys.argv[3])
e = math.e

# if r is not given as decimal ask user to input a decimal instead
if r > 1:
    stdio.writeln("Interest rate should be a decimal (example: 0.1 for 10%). You entered: " + str(r))
    sys.exit("Retry execution with decimal r")

# given compounding formula from textbook
compounded = p * ((e)**(r * t))

# print out the compounded amount of money
stdio.writeln("Compounded result of $" + str(p) + " at " + str(r*100) + "% interest rate for " + str(t) + " years: $" + str(compounded))

############################################################################################################
###############################
##### New Code for 1.3.14 #####
###############################
############################################################################################################

total_months = int(t * 12.0) # get total months from input of t years
monthly_interest = r / 12.0 # get monthly rate from input of r rate
payments = p / total_months # equal monthly payments based on p principal
remaining_payments = p # sets the amount of payments to be made
total_paid = 0.0 # sets tracking to start at 0

# Table header
stdio.writeln("\nMonth\tPayment\tTotal Paid\tRemaining Principal")

for month in range(1, total_months + 1): #months has to start at January (1)
    interest = remaining_payments * monthly_interest # calculate interest from remaining balance
    remaining = remaining_payments + interest - payments # payment made after applying interest
    total_paid += payments # add payment to tracker

    # make table entries using \t escape character, and round to two decimal places to save room per entry
    stdio.writeln(str(month) + "\t" + "$" + str(round(payments, 2)) + "\t" + "$" + str(round(total_paid, 2)) + "\t" + "\t" + "$" + str(round(remaining, 2)))

    remaining_payments = remaining  # carry forward to next month




