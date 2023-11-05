#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

budget_csv = os.path.join(".", "Resources", "budget_data.csv")

#Create a list to store values
months_total = []
total = []
money = []
sum = 0
sum_change = 0

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:       
#The total number of months included in the dataset
        months_total.append(row[0])
#Array generation to calculate profit/losses and stats later
        total.append(int(row[1]))
#The net total amount of "Profit/Losses" over the entire period
        sum = sum + int(row[1])

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
for i in range (len(total)-1):
    money.append(total[i+1]-total[i])
    sum_change = total[i+1]-total[i] + sum_change
change = round(sum_change/len(money),2)


#The greatest increase in profits (date and amount) over the entire period
max_increase = max(money)
for i, j in enumerate(money):
    if j == max_increase:
        max_increase_month = months_total[i+1]

#The greatest decrease in profits (date and amount) over the entire period
max_decrease = min(money)
max_decrease
for i, j in enumerate(money):
    if j == max_decrease:
        max_decrease_month = months_total[i+1]

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(months_total)}')
print(f'Total: ${sum}')
print(f'Average Change: ${change}')
print(f'Greatest Increase in Profits: {max_increase_month} (${max_increase})')
print(f'Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})')


# In[2]:


#Save file
with open('pybank_summary.txt', 'w') as f:
    f.write("Financial Analysis\n"
    "----------------------------\n"
    f'Total Months: {len(months_total)}\n'
    f'Total: ${sum}\n'
    f'Average Change: ${change}\n'
    f'Greatest Increase in Profits: {max_increase_month} (${max_increase})\n'
    f'Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n')


# In[ ]:




