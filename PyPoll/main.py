import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

candidates = []
num_votes = []
percent_votes = []
total_votes = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

percent_votes = [(votes / total_votes) * 100 for votes in num_votes]

winning_candidate_index = num_votes.index(max(num_votes))
winning_candidate = candidates[winning_candidate_index]

print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percent_votes[i]:.3f}% ({num_votes[i]})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

output_file = "output.txt"
with open(output_file, "w") as output:
    output.write("Election Results\n")
    output.write("--------------------------\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("--------------------------\n")
    for i in range(len(candidates)):
        output.write(f"{candidates[i]}: {percent_votes[i]:.3f}% ({num_votes[i]})\n")
    output.write("--------------------------\n")
    output.write(f"Winner: {winning_candidate}\n")
    output.write("--------------------------\n")
