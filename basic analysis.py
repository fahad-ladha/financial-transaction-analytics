

import pandas as pd
transactions = pd.read_csv("data/transactions.csv")

print(transactions.info())


transactions["Date"] = pd.to_datetime(transactions["Date"])
transactions["Month"] = transactions["Date"].dt.month
print(transactions)

transactions = pd.read_csv("data/transactions.csv")
transactions["Date"] = pd.to_datetime(transactions["Date"])
transactions["Month"] = transactions["Date"].dt.month
print(transactions)

Total_expenses=transactions[transactions["Type"]=="Expense"]["Amount"].sum()
print(Total_expenses)

total_income=transactions[transactions["Type"]=="Income"]["Amount"].sum()
print(total_income)

Net_cash_flow=total_income-Total_expenses
print(Net_cash_flow)

expense_breakdown=((transactions[transactions["Type"]=="Expense"]).groupby("Category")["Amount"]).sum()
print(expense_breakdown)

Largest_Individual_Expense=(transactions.loc[4])
print(Largest_Individual_Expense)

transactions["Month"]=transactions["Date"].dt.month
print(transactions)


Monthly_Expenses=(transactions[transactions["Type"]=="Expense"].groupby("Month")["Amount"]).sum()
print(Monthly_Expenses)


category_expense_percentage=expense_breakdown/Total_expenses * 100
print(category_expense_percentage)

category_avg_expense=((transactions[transactions["Type"]=="Expense"]).groupby("Category")["Amount"]).mean()
print(category_avg_expense)

category_summary=((transactions[transactions["Type"]=="Expense"]).groupby("Category")["Amount"]).agg(["sum","mean"])
print(category_summary)

highest_spending_category=category_summary["sum"].idxmax()
print(highest_spending_category)

monthly_cash_flow=(transactions[transactions["Type"]=="Income"].groupby("Month")["Amount"].sum())-Monthly_Expenses
print(monthly_cash_flow)

monthly_income=(transactions[transactions["Type"]=="Income"].groupby("Month")["Amount"].sum())
print(monthly_income)


#Calculate the percentage of income remaining after expenses for each month.
Monthly_savings_rate=monthly_cash_flow/monthly_income * 100
print(Monthly_savings_rate)


Highest_Spending_Month=Monthly_Expenses.idxmax()
print(Highest_Spending_Month)

#Shows the variation between the months and the spending patterns , assists in understanding which month is extensively spent on
votality_Month_by_month=(transactions[transactions["Type"]=="Expense"].groupby("Month")["Amount"]).std()


#Which month had the biggest deviation from the typical monthly spending level
Highest_volatile_Month=votality_Month_by_month.idxmax()

print(Highest_volatile_Month)

#shows the Median value between all months
print(Monthly_Expenses.median())


print(Monthly_Expenses)

#Shows how far the monthly spending varies from the avg this gives us numerical measure of overall consistency


Monthly_spending_std=Monthly_Expenses.std()
print(Monthly_spending_std)

#Measure how much of your monthly spending goes toward each category, so we can compare category importance relative to total spending.
Category_Spending_Percentage=category_summary/(category_summary.sum())*100
print(Category_Spending_Percentage)

#the top 3 spending categories automatically listed rather then manually reading them

Top_3_Spending=category_summary["sum"].sort_values(ascending=False)[:3]
print(Top_3_Spending)


import numpy as np 

transactions["Expense_Flag"]=np.where(transactions["Type"]=="Expense",1,0)
print(transactions)
#mMeasures the expense portion of each transaction amount , this gives us another quantative feature we can usee

transactions["Net_Amount"]=np.where(transactions["Type"]=="Expense",-transactions["Amount"],+transactions["Amount"])
print(transactions)

#Classify Transactions into meaninful size groups 
transactions["Transaction_Size"] = pd.cut(
    transactions["Amount"],
    bins=[-float("inf"), 200, 600, float("inf")],
    labels=["Small", "Medium", "Large"],
    right=True
)

print(transactions)

Transaction_Size_Count = transactions["Transaction_Size"].value_counts()
print(Transaction_Size_Count)

#this shows how much each size of transcation is present

Transactions_Size_Spending=transactions.groupby("Transaction_Size")["Amount"].sum()
print(Transactions_Size_Spending)

#Measures the typical transaction amount withing each zied of category and shows avg
Transactions_Size_AVG=transactions.groupby("Transaction_Size")["Amount"].mean()
print(Transactions_Size_AVG)



total_amount=transactions["Amount"].sum()
print(total_amount)
#Shows what percentage of the dataset values come from small,medium, and large
Transaction_Size_Percentage=Transactions_Size_Spending/total_amount*100
print(Transaction_Size_Percentage)


Category_Transaction_Count = transactions["Category"].value_counts()
print(Category_Transaction_Count)

Category_Spending_Total = transactions.groupby("Category")["Amount"].sum()
print(Category_Spending_Total)

Income_Expense_Summary = transactions.groupby("Type")["Amount"].agg(
    ["count", "sum", "mean"]
)

print(Income_Expense_Summary)


Category_Spending_Share=((transactions.groupby("Category")["Amount"].sum())/total_amount*100).sort_values(ascending=False)
print(Category_Spending_Share)


#Calculate each expense category's share of total expenses


Expense_Category_Share=((transactions[transactions["Type"]=="Expense"].groupby("Category")["Amount"].sum())/Total_expenses*100).sort_values(ascending=False)
print(Expense_Category_Share)

#Identify which expense categories have the highest average transaction value. This helps distinguish categories with frequent small purchases from categories with fewer but larger transactions.
Expense_Category_Avg=(transactions[transactions["Type"]=="Expense"].groupby("Category")["Amount"].mean()).sort_values(ascending=False)
print(Expense_Category_Avg)


#Measures monthly total spending to identify how expenses change over time. this is useful for spotting changing trends
Monthly_Expense_Total=Monthly_Expenses.sum()
print(Monthly_Expense_Total)

#measures monhtly net cashflow
Monthly_Net_Cashflow=(monthly_income.sum()-Monthly_Expense_Total)
print(Monthly_Net_Cashflow)


#Shows how many transactions were performed every month
Monthly_Transaction_Count=transactions.groupby("Month")["Amount"].count()
print(Monthly_Transaction_Count)

#Seperates large transactions only
transactions["High_Transactions_Value"]=np.where(transactions["Amount"]>1000,"high_value","low_value")
print(transactions)

#Transactions frequency overall

Transactions_frequencey=transactions["Category"].value_counts()
print(Transactions_frequencey)