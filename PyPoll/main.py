# First we'll import the os module
import os

# Module for reading CSV files
import csv
# election_data.csv
csvpath = os.path.join("PyPoll","Resources","election_data1.csv")
cand = {}
cand_nm = []
vote = []
ttlv = 0
count = 0
elDat={}

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    # elData = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvfile)
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        count += 1
        candidate = row[2]
        if candidate not in cand:
            cand[candidate] = 1
        else:
            cand[candidate] += 1

print(cand[0]

for x in cand
    nmvt = len(cand)
    vote.append(nmvt)
    print("C")
        
    #print(vote)
ttlv = len(cand)
    #print(ttlv)
pctV = [(a*100) / ttlv for a in (vote)]
    #print(pctV)
wins = cand[pctV.index(max(pctV))]
    #print(wins)
print("Election Results \n------------------------------")
print(f"Total Votes: {len(cand)} \n------------------------------")
for i in range(len(cand_nm)):
    print(f"{cand_nm[i]}: {round(pctV[i],3)}% ({vote[i]})")
print(f"------------------------------\n Winner: {wins}\n------------------------------")