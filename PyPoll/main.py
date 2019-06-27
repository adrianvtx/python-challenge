# PyPoll

# ![Vote-Counting](Images/Vote_counting.png)

# * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# First we'll import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("PyPoll","Resources","election_data.csv")
voter = {}
name = str
# coInfo = []
# x = 0
# pftCh = []
# bkPft = float(0)
# bkLss = float(0)
# diff = 0
# sm=0



with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # coInfo = list(csvreader)
    # Define the function and have it accept the 'wrestler_data' as its sole parameter
    def voter(csvreader):
        vId = int(csvreader[0])
        county = str(csvreader[1])
        name = str(csvreader[2])
        return
print(csvreader)




    #     date.append(row[0])
    #     coInfo.append(row[1])
    #     revenue = revenue + int(row[1])
    # for x in range(1,len(coInfo)):
    #     diff = int(coInfo[x]) - int(coInfo[x - 1])
    #     sm=diff+sm
    #     pftCh.append((diff))
    #     bkPft = max(pftCh)
    #     pftCh.index(max(pftCh))
    #     bkLss = (min(pftCh))
    #     chAvg = int(sm) / (len(coInfo)-1)  
# print("Election Results \n------------------------------")
# print(f"Total Votes: {len(date)}")
# print(f"Total: ${revenue}")
# print(f"Average Change: {round(chAvg,2)}")
# print(f"Greatest Increase in Profits: {date[(pftCh.index(max(pftCh))+1)]} ${ (bkPft)}")
# print(f"Greatest Decrease in Profits: {date[(pftCh.index(min(pftCh))+1)]} ${ (bkLss)}")


# # Specify the file to write to
# output_path = os.path.join("PyBank", "Resources", "new.csv")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     csvwriter.writerow(["Financial Analysis"])
#     csvwriter.writerow(["------------------------------"])
#     csvwriter.writerow([f"Total Months: {len(date)}"])
#     csvwriter.writerow([f"Total: ${revenue}"])
#     csvwriter.writerow([f"Average Change: {round(chAvg,2)}"])
#     csvwriter.writerow([f"Greatest Increase in Profits: {date[(pftCh.index(max(pftCh))+1)]} ${ (bkPft)}"])
#     csvwriter.writerow([f"Greatest Decrease in Profits: {date[(pftCh.index(min(pftCh))+1)]} ${ (bkLss)}"])