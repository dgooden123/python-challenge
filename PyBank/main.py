# PyBank analysis
# 
# Obectives
# 1. The total number of months included in the dataset


# 2. The net total amount of "Profit/Losses" over the entire period


# 3. The average of the changes in "Profit/Losses" over the entire period


# 4. The greatest increase in profits (date and amount) over the entire period


# 5. The greatest decrease in losses (date and amount) over the entire period

# import os and csv modules
import os
import csv

#define variables/lists
months = []
profit= []
changes= []

# set path for CSV budget file
#csvpath=os.path.join('Users','dgoodenough', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')
csvpath=os.path.join('..', 'Resources', 'budget_data.csv')
# read CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

     # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


    # Read each row of data after the header add to the months and profit lists
    for row in csvreader:
        months.append(row[0])
        profit.append(row[1])
        changes.append(profit[i+1]-profit [i]

        #print(row)
        #print(months)

#total number of months in dataset
total_months=len(months)
#calculate the net profit
net_profit=sum(profit)

#calculate the average profit
avg_profit=net_profit/total_months

#find the month with the greatest profit and greatest loss



#print and output results
print(f"Total Months: str(total_months)")
print(f"Net Profit/Losses: str(net_profit)")
print(f"Average Profit/Losses: str(avg_profit)")

output = os.path.join('..', 'Resources', 'budget_output.txt')