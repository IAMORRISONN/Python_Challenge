# Modules
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

months = 0
total = 0
previous_profit = 0
total_change_in_profit = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""

change_PL = {}

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)  

    for row in csvreader:
        months += 1

        total += int(row[1])

        change_in_profit = int(row[1]) - previous_profit
        change_PL[row[0]] = change_in_profit  
        total_change_in_profit += change_in_profit

        previous_profit = int(row[1])

        if change_in_profit > greatest_increase:
            greatest_increase = change_in_profit
            greatest_increase_month = row[0]
        elif change_in_profit < greatest_decrease:
            greatest_decrease = change_in_profit
            greatest_decrease_month = row[0]

average_change = total_change_in_profit / (months - 1)  

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

output_file = "analysis.txt"
with open(output_file, "w") as output:
    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write(f"Total Months: {months}\n")
    output.write(f"Total: ${total}\n")
    output.write(f"Average Change: ${average_change:.2f}\n")
    output.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    output.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
