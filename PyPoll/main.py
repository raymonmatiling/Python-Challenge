## Challenge 2: PyPoll


# Objective 1: Import modules os and csv

import os
import csv

# Objective 2: Set the path for the CSV file in PyPollcsv

PyPollcsv = os.path.join("Resources","election_data.csv")

# Objective 3: Create the lists to store data. Initialize

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Open the CSV using the set path PyPollcsv
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) #Skip the header row
    
    #Iterate through each row in the CSV file    
    for row in csvreader:
        # Count total votes
        total_votes += 1
        # Extract the candidate name from the row
        candidate_name = row[2]
        
        # Update the candidate's vote count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1    
    
# Print the election results 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print(f"Total Votes : {total_votes}")    
print("-------------------------")

# Iterate through the candidates and print their results
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Update the winner information if needed
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Print who is the winner
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# Print to a text file: election_results.txt
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write(f"Total Votes : {total_votes}\n")
    text.write("---------------------------------------\n")
    
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        text.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    text.write("---------------------------------------\n")
    text.write(f"The winner is: {winner}\n")
    text.write("---------------------------------------\n")


