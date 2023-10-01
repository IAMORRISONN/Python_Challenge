# Modules
import os
import csv




# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

month = 0 
total = 0
current_amount = 0
change_in_month = 0
average_change = 0
total_change_in_PF = 0

change_PL : { month:[month] , change_in_month:[change_in_month] }

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(csvreader)
    # Loop through looking for the video
    for row in csvreader:
        month= month + 1
        Total = total + int(row [2])
        change_in_month = int(row[1]) - current_amount 
        print(change_in_month)
        current_amount = int(row[1])
        total_change_in_PF = total_change_in_PF + change_in_month 


print("/////////")
print(total_change_in_PF)
print(month)  
average_change = total_change_in_PF / month 

        print(row)
        print (f"Total Month : {month}")
        print(f"Total : {total}")
        print(change_in_month) 
        print(average_change)
Print(change_PL)