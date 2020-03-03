#This program will calculate the projected total profit from the total sales of the company.
#February 20, 2020
#CTI-110 P2T1 Sales Prediction
#Jose Ibanez
#

total_sales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

#Display the profit
print("The total profit is $", format(profit, ",.2f"))
