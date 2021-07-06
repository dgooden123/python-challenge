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
total_months=0
net_changes= []


# set path for CSV budget file
#csvpath=os.path.join('Users','dgoodenough', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')
csvpath=os.path.join('Resources', 'budget_data.csv')
# read CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

     # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    jan_data=next(csvreader)
    months.append(jan_data[0])
    profit.append(int(jan_data[1]))
    previous_net=int(jan_data[1])


    # Read each row of data after the header add to the months and profit lists
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
        changes=int(row[1])-previous_net
        previous_net=int(row[1])
        
        net_changes.append(changes)


        #print(row)
        #print(months)


#total number of months in dataset
total_months=len(months)
#calculate the net profit
net_profit=sum(profit)

#calculate the average profit
avg_profit=sum(net_changes)/len(net_changes)

max_profit=max(net_changes)
min_profit=min(net_changes)
max_index=net_changes.index(max_profit)
min_index=net_changes.index(min_profit)


greatest_inc_month=months[max_index+1]
greatest_dec_month=months[min_index+1]

#find the month with the greatest profit and greatest loss



#print and output results
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${avg_profit}")
print(f"Greatest Increase in Profits: {greatest_inc_month} ${max_profit}")
print(f"Greatest Decrease in Profits: {greatest_dec_month} ${min_profit}")


#output = os.path.join('Analysis', 'budget_output.txt')