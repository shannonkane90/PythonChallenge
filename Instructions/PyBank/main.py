import os
import csv

csvpath = os.path.join('Instructions', 'PyBank', 'Resources', 'budget_data.csv')

outputfile= os.path.join("Analysis", "BudgetAnalysis.txt")



total_months= 0
total=0
change_list=[]
month=[]
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999]


with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    
    header= next(csvreader)
    first_row=next(csvreader)
    total_months=total_months+1
    total += int(first_row[1])
    previous_row = int(first_row[1])

    for row in csvreader:
        total_months=total_months+1
        total += int(row[1])

      #Average Changes  
        net_change=int(row[1])-previous_row
        previous_row=int(row[1])
        change_list= change_list + [net_change]
        month= month+ [row[0]]
        average_change= sum(change_list)/len(change_list)

#find greatest increase/decrease
        if net_change> greatest_increase[1]:
          greatest_increase[0]=row[0]
          greatest_increase[1]=net_change

        if net_change < greatest_decrease[1]:
          greatest_decrease[0]=row[0]
          greatest_decrease[1]=net_change
  
print(total_months)
print(total)
print(average_change)
print(greatest_decrease)
print(greatest_increase)


#change to dollar amounts...

# # #----------------------------
# # Total Months: 86
# # Total: $38382578
# # Average  Change: $-2315.12
# # Greatest Increase in Profits: Feb-2012 ($1926159)
# # Greatest Decrease in Profits: Sep-2013 ($-2196167)



# # for greatest increase/decrease
#   #i = i-1      

       

# #still need to export to file...

# # total=0
# # with open(csvpath) as csvfile:
# #     csvreader=csv.reader(csvfile)
# #     next(csvreader)
# #     for row in csvreader:
# #         total += int(row[1])
# #     print (total)

# bank_results=(
#     f"Total Months: {total_months}"
# )
# print (bank_results)
    










