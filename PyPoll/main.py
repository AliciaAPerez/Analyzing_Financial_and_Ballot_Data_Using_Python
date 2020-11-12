#PyPoll 
import os
import csv

# Path to collect data from the Resources folder
pollpath = os.path.join("Resources", "election_data.csv")

#data variables and lists
vote_total = 0
candidates = []
candidate_votes = {}
winning_candidate = 0

#function to calculate percentage
def percentage(candidate_votes, vote_total):
    candidate_percentage = candidate_votes / vote_total * 100
    return round(candidate_percentage, 0)
#
#open csv file as read
with open(pollpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    csv_header = next(csvreader)
    
#Calculations:
#total number of votes cast    
    for row in csvreader:
        vote_total += 1
                
#complete list of candidates who received votes        
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] = candidate_votes[candidate] + 1

#start text file for results and do calculations
#total vote output1 text file
with open("Analysis/ElectionResults.txt", "w") as txtfile:
    output1 = (f"Election Results\n"
        f".........................\n"
        f"Total Votes {vote_total}\n"
        f".........................\n"
        )
    txtfile.write(output1)
    #print for terminal
    print(output1)

    #loop for equations
    for candidate in candidates: 
        #total votes per candidate
        votes = candidate_votes.get(candidate)
        #calculate winner based on votes
        if votes > winning_candidate:
            winner = candidate
            winning_candidate = votes
        #calculate percentage per candidate
        prct = percentage(votes, vote_total)
        #print results per candidate
        output2 = f"{candidate}: {prct}% ({votes})\n"
        #must print here for terminal to print all candidates
        print(output2)
        txtfile.write(output2)

    #print winner output 3 finishing text file
    output3 = (f".........................\n"
            f"Winner: {winner}\n"
            f".........................")
    txtfile.write(output3)
#last print for terminal
print(output3)