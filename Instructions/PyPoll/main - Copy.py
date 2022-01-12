import os
import csv

print(os.getcwd())

csvpath = os.path.join('02-Homework', '03-Python', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')
print(csvpath)

candidate_votes={}


total_votes=0

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
       # print(row)
        total_votes=total_votes+1

        candidate_name= row[2]
        if candidate_name in candidate_votes:
            candidate_votes [candidate_name] = candidate_votes[candidate_name]+1

        else : 
            candidate_votes [candidate_name] = 1
#print (candidate_votes)
print("Election Results")
print ("-------------------------")
print ("Total Votes: %d" % total_votes)
print("-------------------------")

winner= ""
winning_votes=0

for Name in candidate_votes:
    # print(Name, candidate_votes [Name], candidate_votes[Name]/total_votes)
    vote_percent = candidate_votes[Name]/total_votes*100
    print ("%s: %2.3f%% (%d)" % (Name, vote_percent, candidate_votes[Name]))

    if candidate_votes [Name] > winning_votes:
        winner=Name
        winning_votes=candidate_votes[Name]
print("-------------------------")
print("Winner: %s" % winner)
print("-------------------------")

#still need to export to file...



    
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------









#The total number of votes cast


#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.
#for row in open(csvpath) 
 #   num_votes+=1
#print (num_votes)


