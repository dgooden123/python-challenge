# PyPoll analysis
# 
# Obectives
# 1. The total number of votes cast


# 2. A complete list of candidates who received votes


# 3. The percentage of votes each candidate won


# 4. The total number of votes each candidate won


# 5. The winner of the election based on popular vote.




# import os and csv modules
import os
import csv

#define variables
votes = 0
khan = 0
correy = 0
li= 0
otooley= 0


# set path for CSV election file

csvpath=os.path.join('Resources', 'election_data.csv')
# read CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    
    


    # Read each row of data add vote 
    for row in csvreader:
               total_votes += 1
        
        # For each row determine the candidate 
        if (row[2] == "Khan"):
            khan += 1
        elif (row[2] == "Correy"):
            correy += 1
        elif (row[2] == "Li"):
            li += 1
        else:
            otooley += 1

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
print(f"{greatest_inc_month} {max_profit}")
print(f"{greatest_dec_month} {min_profit}")
#find the month with the greatest profit and greatest loss



#print and output results
print(f"Total Months: {total_months}")
print(f"Net Profit/Losses: {net_profit}")
print(f"Average Profit/Losses: {avg_profit}")

#output = os.path.join('..', 'Resources', 'budget_output.txt')