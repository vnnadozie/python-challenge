
import os
import csv


#File pathway
budget_data = os.path.join("Resources", "budget_data.csv")

#Open and read csv file
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    # Net amount of profit and loss
    P = []
    months = []

    # Read each row of data
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    # Revenue change
    revenue_change =[]

    for x in range(1, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))

    # Average revenue change
    revenue_average_change = sum(revenue_change) / len(revenue_change)
    revenue_average = round(revenue_average_change, 2)

    # Total months
    total_months = len(months)

    # Greatest increase in revenue
    greatest_increase = max(revenue_change)

    #Greatest decrease in revenue
    greatest_decrease = min(revenue_change)


    # Print Results in Terminal
    print ("Financial Analysis")

    print("-------------------------")

    print ("Total Months:" + str(total_months))

    print("Total:" + "$" + str(sum(P)))

    print ("Average Change:" + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")")

    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")")


    # Export to a text file
    file = open("result.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("-------------------------" + "\n")

    file.write("Total months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(P)) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")\n")

    file.close()