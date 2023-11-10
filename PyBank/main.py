## Challenge 1: PyBank


# Objective 1: Import modules os and csv

import os
import csv

# Objective 2: Set the path for the CSV file in PyBank folder

PyBankcsv = os.path.join("Resources","budget_data.csv")

# Objective 3: Create the lists to store data. 

profit = []
monthly_changes = []
monthly_changes_profits = []
date = []

# Initialize the variables as required.
 
count = 0
total_profit = 0
initial_profit = 0

# Open the CSV using the set path PyBankcsv
with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    count += 1
    total_profit += int(first_row[1])
    prev_net = int(first_row[1])
            
    for row in csvreader:    
      
      count += 1 
      total_profit += int(row[1])
           
      monthly_changes = int(row[1]) - prev_net
      prev_net = int(row[1])
      monthly_changes_profits += [monthly_changes]
      date += [row[0]]
      total_change_profits = sum(monthly_changes_profits) / len(monthly_changes_profits)
      
    # Find the greatest increase and decrease in profits
    greatest_increase_profits = max(monthly_changes_profits)
    greatest_decrease_profits = min(monthly_changes_profits)

    increase_date = date[monthly_changes_profits.index(greatest_increase_profits)]
    decrease_date = date[monthly_changes_profits.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print(f"Average Change: ${total_change_profits:.2f}")
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

# Print to a text file: election_results.txt

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write(f"    Average Change: ${total_change_profits:.2f}\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("                                                          \n")
    text.write("----------------------------------------------------------\n")

