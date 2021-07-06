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

khan_n = 0
correy_n = 0
li_n= 0
otooley_n= 0

khan_p = 0
correy_p = 0
li_p= 0
otooley_p= 0

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
               
        votes += 1
        
        # For each row determine the candidate 
        if (row[2] == "Khan"):
            khan_n += 1
        elif (row[2] == "Correy"):
            correy_n += 1
        elif (row[2] == "Li"):
            li_n += 1
        else:
            otooley_n += 1

#percent of votes by candidate
khan_p = round((khan_n/votes)*100)
correy_p = round((correy_n/votes)*100)
li_p= round((li_n/votes)*100)
otooley_p= round((otooley_n/votes)*100)

#determine  the most votes
most_votes=max(khan_n, correy_n, li_n, otooley_n)
#print(most_votes)

#determine the winner
if most_votes==khan_n: 
    winner="Khan"
elif most_votes==correy_n:
    winner="Correy"
elif most_votes==li_n:
    winner="Li"
else: winner="O'Tooley"

#print(winner)
#print and output results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {votes}")
print(f"----------------------------")
print(f"Khan: {khan_p}% ({khan_n})")
print(f"Correy: {correy_p}% ({correy_n})")
print(f"Li: {li_p}% ({li_n})")
print(f"O'Tooley: {otooley_p}% ({otooley_n})")
print(f"----------------------------")
print(f"Winner: {winner}")



# print(f"Net Profit/Losses: {net_profit}")
# print(f"Average Profit/Losses: {avg_profit}")


output = os.path.join('Analysis', 'election_output.txt')
with open(output, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Total Votes: {votes}\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Khan: {khan_p}% ({khan_n})\n")
    txtfile.write(f"Correy: {correy_p}% ({correy_n})\n")
    txtfile.write(f"Li: {li_p}% ({li_n})\n")
    txtfile.write(f"O'Tooley: {otooley_p}% ({otooley_n})\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Winner: {winner}\n")


    