# First we'll import the os module
import os
# Module for reading CSV files
import csv
# election_data.csv
csvpath = os.path.join("PyPoll","Resources","election_data.csv")
cand = {}
count = 0


with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvfile)
    csvreader = csv.reader(csvfile)
    
    for row in csvreader:
        count += 1
        candidate = row[2]
        # Vote1=(cand.get(candidate))
        if candidate not in cand:
            cand[candidate] = 1
            # cand[vote] = 1
        else:
            cand[candidate] += 1

# print(cand.get(candidate)) EXTRA STUFF
        
vMax = max(cand.keys(), key=(lambda k: cand[k]))
vMin = min(cand.keys(), key=(lambda k: cand[k]))
# print(vMax)
# print(vMin)
# print(cand)
# ttlv = count
# print(ttlv)

# Also Unnecessary
# wins = list(cand)
# print(wins)
# Winner = wins[wins.index(max(cand))]
# print(winner)


    #text output

print("Election Results \n------------------------------")
print(f"Total Votes: {count} \n------------------------------")
print(f"Winner: {vMax} \n------------------------------")
for key, value in cand.items():
    print(f"{key}:  {round(value/count*100,3)}%   ({value})")

#         wins.append(key) Alternate append to list not needed
#         wins.append(value)
# for i in range(len(cand)):
    # pctv = ((value) / (vMax))
    # print(f"{key}: {round(pctV[i],3)}% ({value})")
print(f"------------------------------\n Winner: {vMax}\n------------------------------")
# with open('output.txt', 'w') as outfile:
#     outfile.write(output)
#     outfile.close()
# print(output)
# Specify the file to write to
output_path = os.path.join("PyPoll", "Resources", "Output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results \n------------------------------"])
    csvwriter.writerow([f"Total Votes: {count} \n------------------------------"])
    for key, value in cand.items():
        csvwriter.writerow([f"{key}:  {round(value/count*100,3)}%   ({value})"])
    csvwriter.writerow([f"------------------------------\n Winner: {vMax}\n------------------------------"])


