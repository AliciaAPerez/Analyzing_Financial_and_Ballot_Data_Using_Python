#PyPoll 
import os
import csv

# Path to collect data from the Resources folder
pollpath = os.path.join("Resources", "election_data.csv")

#data lists
Vote_Total = 0
Candidates = []
Candidate_Votes = {}
Winning_Candidate = 0


def Percentage(Candidate_Votes, Vote_Total):
    Candidate_Percentage = Candidate_Votes / Vote_Total * 100
    return round(Candidate_Percentage, 0)

#open csv file as read
with open(pollpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    csv_header = next(csvreader)
    
#Calculations:
# total number of votes cast    
    for row in csvreader:
        # Vote_Total = sum(1 for vote in csvreader)
        Vote_Total += 1
                
#complete list of candidates who received votes        
        Candidate = row[2]
        if Candidate not in Candidates:
            Candidates.append(Candidate)
            Candidate_Votes[Candidate] = 0
        Candidate_Votes[Candidate] = Candidate_Votes[Candidate] + 1

with open("Analysis/ElectionResults.txt", "w") as txtfile:
    output1 = (f"Election Results\n"
        f"......................\n"
        f"Total Votes {Vote_Total}\n"
        f"......................\n"
        )
    txtfile.write(output1)
    print(output1)
    for Candidate in Candidates: 
        Votes = Candidate_Votes.get(Candidate)
        if Votes > Winning_Candidate:
            Winner = Candidate
            Winning_Candidate = Votes
        PRCT = Percentage(Votes, Vote_Total)
        output2 = f"{Candidate}: {PRCT}% ({Votes})\n"
        print(output2)
        txtfile.write(output2)
    output3 = (f"......................\n"
            f"Winner: {Winner}\n"
            f"......................")
    txtfile.write(output3)
print(output3)
        
#total number of votes each candidate won
#percentage of votes each candidate won
#winner of election based on popular vote
#print to text file the results