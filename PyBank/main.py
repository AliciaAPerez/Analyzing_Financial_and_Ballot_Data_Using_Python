#PyBank 
import os
import csv

# Path to collect data from the Resources folder
bankpath = os.path.join("Resources", "budget_data.csv")

#data variables and lists
months = 0
months_change = 0
net_total = 0
changes_month_to_month = []
change_sum = 0
greatest_increase = 0
greatest_decrease = 0

#open csv file as read
with open(bankpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    csv_header = next(csvreader)  
    #set values for first row
    first_row = next(csvreader)
    prev_value = int(first_row[1])
    #set value for months as we're skipping first line
    months += 1
    #set total for months as we're skipping first ine
    net_total += int(first_row[1])
    
#Calculations:
#total number of months
    for row in csvreader:
        months += 1
        #one month less for changes, but need both totals recorded
        months_change += 1
        
#total amount of profit/losses over entire period
        net_total += int(row[1])

#calculate changes in profits/loss over entire preriod
        #making a dictionary of date and changes
        #save date
        date = str(row[0])
        changes_month_to_month.append(date)
        #find the change in profits
        changes = int(row[1]) - prev_value
        changes_month_to_month.append(changes)
        #sum of changes
        change_sum += changes
        #greatest increase
        if changes > greatest_increase:
            increasedate = date
            greatest_increase = changes
        #greatest decrease
        if changes < greatest_decrease:
            decreasedate = date
            greatest_decrease = changes
        #average of changes
        average_changes = change_sum / months_change
        #change prev_row to update 
        prev_value = int(row[1])

#round the decimal place to two places
rounded_average = round(average_changes, 2)

#print information to text file and terminal
with open("Analysis/FinancialAnalysis.txt", "w") as txtfile:
    output = (f"Financial Analysis \n"
            f".........................................\n"
            f"Total Months: {months}\n" 
            f"Total: ${net_total}\n"
            f"Average Change: ${rounded_average} \n"
            f"Greatest Increase in Profits: {increasedate} (${greatest_increase}) \n"
            f"Greatest Decrease in Profits: {decreasedate} (${greatest_decrease}) \n"
            f".........................................\n"
            )
    txtfile.write(output)
    print(output)