import csv
import os


csvpath = os.path.join('H:\Github Repositories\python-challenge\PyBank\Resources', 'budget_data.csv')

with open(csvpath, encoding= 'utf') as csvfile:
#Initialising reader to read csvfile
    csvreader = csv.reader(csvfile, delimiter = ',')
   #Skipping the first row (header)
    next(csvreader)
   #Excluding first month from for loop
    budget_data = [next(csvreader)]
    #Initialising net amount with first profit or loss 
    net_amount = int(budget_data[0][1])
    changes = []
    #Will be used to calculate change inside for loop
    previous_profit_loss = net_amount

    for line in csvreader:
        # Total months included in dataset
        budget_data.append(line)
       
        # Net total amount of Profit/Losses over entire period
        net_amount = net_amount + int(line[1])
       
       # Changes in profit/loss over entire period
        changes.append(int(line[1])-previous_profit_loss)

        # Average changes of profit/loss
        previous_profit_loss = int(line[1])


# Greatest increase in profit (date and amount)
index_max_change = changes.index(max(changes))
# print(budget_data[index_max_change+1])

#Greatest decrease in profit (date and amount)
index_max_loss = changes.index(min(changes))
# print(budget_data[index_max_loss+1])

# Export result to text file and print analysis in terminal
output = f'''  Financial Analysis
  ----------------------------
  Total Months: {len(budget_data)}
  Total: ${net_amount}
  Average Change: ${round(sum(changes)/(len(changes)),2)}
  Greatest Increase in Profits: {budget_data[index_max_change+1][0]} (${max(changes)})
  Greatest Decrease in Profits: {budget_data[index_max_loss+1][0]} (${min(changes)})
  
  '''
print(output)
csvpath = os.path.join('H:\Github Repositories\python-challenge\PyBank\Analysis', 'analysis_results.txt')
with open(csvpath,'w') as textfile:
    textfile.write(output)
