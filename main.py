#Module for reading csv files

import os
import csv

#Set path

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#List variables

Total_Months = []
Net_Total = []
Average_Change = []
Greatest_Increase_in_Profits = []
Greatest_Decrease_in_Profits = []

#Open CVS file

with open(budget_csv, encoding='utf-8') as cvsfile:
    csvreader = csv.reader(cvsfile, delimiter=",")
    csv_reader= next(csvreader)
    for row in csvreader:

#Total of months & Profits/Losses
        
        Total_Months.append(row[0])
        Net_Total.append(row[1])
    print(len(Total_Months))

#The net total amount of "Profit/Losses" in the entire period 

    Net_Total=[int(x)for x in Net_Total]
    Net_Total_sum=sum(Net_Total)
    print(Net_Total_sum)

#Changes in "Profits/Losses" in the entire period

for i in range(len(Net_Total)-1):
    Average_Change.append(Net_Total[i+1]-Net_Total[i])