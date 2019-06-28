# First we'll import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("Resources","election_data.csv")
cand = []
cand_nm = []
vote = []
ttlv = 0
iter=0

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    elData = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(elData)
    print('A')
    
    for row in elData:
        cand.append(row[2])
        for uniq in cand:
            if uniq not in cand_nm:
                cand_nm.append(uniq)
            iter=iter+1
            print(iter)
    
    for x in cand_nm:
        nmvt = cand.count(x)
        vote.append(nmvt)
        print("C")
    
    #print(vote)
    ttlv = len(cand)
    #print(ttlv)
    pctV = [(a*100) / ttlv for a in (vote)]
    #print(pctV)
    wins = cand_nm[pctV.index(max(pctV))]
    #print(wins)
    print("Election Results \n------------------------------")
    print(f"Total Votes: {len(cand)} \n------------------------------")
    for i in range(len(cand_nm)):
        print(f"{cand_nm[i]}: {round(pctV[i],3)}% ({vote[i]})")
    print(f"------------------------------\n Winner: {wins}\n------------------------------")