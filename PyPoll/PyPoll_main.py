#!/usr/bin/env python
# coding: utf-8

# In[23]:


import os
import csv
import pandas as pd

#Set variables
total_votes = 0
Charles = 0
Diana = 0
Raymon = 0

# Open and read csv
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    csv_header = next(csvreader)
    print(csv_header)
    
# Read each row of data after the header
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] == 'Charles Casper Stockham':
            Charles = Charles + 1
        elif row[2] == 'Diana DeGette':
            Diana = Diana + 1
        elif row[2] == 'Raymon Anthony Doane':
            Raymon = Raymon + 1

#The percentage of votes
Charles_percent = round(Charles * 100/ total_votes,3)
Diana_percent = round(Diana * 100/ total_votes,3)
Raymon_percent = round(Raymon * 100/ total_votes,3)

#Create DataFrame and sort by descending to determine the winner
data = {'Candidates': ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane'], 
       'Votes': [Charles, Diana, Raymon]}

df = pd.DataFrame(data)
winner = df.sort_values(by='Votes', ignore_index=True, ascending=False)
winner = winner['Candidates'][0]

# Print results
print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
print(f'Charles Casper Stockham: {Charles_percent}% ({Charles})')
print(f'Diana DeGette: {Diana_percent}% ({Diana})')
print(f'Raymon Anthony Doane: {Raymon_percent}% ({Raymon}')
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
   


# In[25]:


# Save as txt file
with open('pypoll_summary.txt', 'w') as f:
    f.write("Election Results\n"
    "----------------------------\n"
    f'Total Votes: {total_votes}\n'
    "----------------------------\n"
    f'Charles Casper Stockham: {Charles_percent}% ({Charles})\n'
    f'Diana DeGette: {Diana_percent}% ({Diana})\n'
    f'Raymon Anthony Doane: {Raymon_percent}% ({Raymon}\n'
    "----------------------------\n"
    f"Winner: {winner}\n"
     "----------------------------\n")


# In[ ]:




