import pandas as pd
import numpy as np

Corp=pd.read_csv("data/2211.csv")
print(Corp)

print(Corp.info())


#INCOME STATEMENT for the accounting period 12/23-12/24


#Shows the percentage growht in revenue over the years

Corp["Revenue_Growth"]=Corp["Revenue"].pct_change()*100
print(Corp)



Corp["Gross_profit"]=Corp["Revenue"]-Corp["COGS"]
print(Corp)



#Shows the operating profit and the profit before interest,depreciation,and tax expense
Corp["EBITDA"]=Corp["Gross_profit"]-Corp["Operating_Expenses"]
print(Corp)

#shows the profit after deducting depreciation expense
Corp["EBIT"]=Corp["EBITDA"]-Corp["Depreciation"]
print(Corp)

#Shows the profit after deducting interest expense , helpful to find how much interest cover there is
Corp["EBT"]=Corp["EBIT"]-Corp["Interest_Expense"]

print(Corp)

Corp["Net_Profit"]=Corp["EBT"]-Corp["Tax_Expense"]
print(Corp)

#The company demonstrates a consistent expansion in its operating scale over the six-year period, with revenue increasing from 85,000 in 2020 to 145,000 in 2025. This indicates sustained revenue growth and an expanding business, although the data alone cannot establish whether this resulted from higher demand, pricing changes, or shifts in product mix.

#Gross profit increased from 34,000 to 69,000 over the same period, while gross margin improved from 40.0% to approximately 47.6%. The improvement in gross margin indicates that the company has become more effective at managing its cost of goods sold relative to revenue. For a consumer goods and retail distribution business, this may reflect improved procurement economics, pricing power, product mix, or greater operating scale.

#EBITDA increased from 16,000 to 42,500, while EBITDA margin expanded from 18.8% in 2020 to approximately 29.3% in 2025. This is particularly significant because EBITDA grew substantially faster than revenue, indicating that the company generated stronger operating earnings as it expanded.

#EBIT also increased throughout the period after incorporating depreciation, indicating that the improvement in operating performance remains visible after accounting for the cost of the company's long-term asset base.

#EBT increased from 9,500 to 35,300, while interest expense declined from 2,500 to 1,700. This combination indicates that financing costs placed a smaller burden on earnings before tax. The improvement in interest coverage further supports the conclusion that the company's ability to meet interest obligations strengthened over the period.

#Net income increased from 7,600 in 2020 to 30,100 in 2025. Overall, the income statement indicates a company experiencing both strong top-line expansion and improving operating profitability. The combination of revenue growth, expanding margins, and rising net income suggests improving underlying financial performance rather than growth being achieved at the expense of profitability.
    





#Shows the percentage of Gross profit that the revenue is able to cover , meaning what is the gross return margin

Corp["Gross_margin"]=Corp["Gross_profit"]/Corp["Revenue"]*100
print(Corp)

#Shows how much each unit of the revenue is coverted into EBITDA before the effects of interest tax and depreciation

Corp["EBITDA_Margin"]=Corp["EBITDA"]/Corp["Revenue"]*100
print(Corp)




Corp["EBIT_Margin"]=Corp["EBIT"]/Corp["Revenue"]*100
print(Corp)

# this shows the centric ability of the company to genrerate overall profits through each unit of revenue
Corp["Net_Profit_Margin"]=Corp["Net_Profit"]/Corp["Revenue"]*100
print(Corp)



#The company's margin profile shows a broad improvement across the six-year period. Gross margin increased from 40.0% to approximately 47.6%, indicating that a larger proportion of each unit of revenue is being retained after direct product costs.

#EBITDA margin also strengthened materially over the period, demonstrating that the improvement in gross profitability is translating into stronger operating earnings after operating expenses. This suggests improving cost discipline and operating leverage as the business expands.

#The continued improvement in EBIT and net profitability indicates that the benefits of operating growth are flowing through to the bottom line rather than being absorbed entirely by depreciation, financing costs, or taxation.

#From an industry perspective, the trend is favourable for a consumer goods and retail distribution business. Expanding margins alongside revenue growth can indicate improved purchasing efficiency, economies of scale, stronger pricing, and a more profitable revenue mix.

#However, margin expansion alone does not establish that the company's financial position is becoming stronger. The next stages of the analysis will therefore examine whether this profitability is supported by healthy liquidity, efficient working-capital management, sustainable cash generation, and an appropriate level of financial leverage.




#BALANCE SHEET ITEMS


Corp["Current_Assets"]=Corp["Cash"]+Corp["Accounts_Receivable"]+Corp["Inventory"]
print(Corp)


Corp["Total_Assets"]=Corp["Current_Assets"]+Corp["PPE"]
print(Corp)


Corp["Current_Liabilities"]=Corp["Accounts_Payable"]+Corp["Short_Term_Debt"]
print(Corp)

Corp["Total_Liabilities"] = Corp["Current_Liabilities"] + Corp["Long_Term_Debt"]
print(Corp)


#Shows the companies short term financial decision making after covering current obligations with current assets    
Corp["Working_Capital"] = Corp["Current_Assets"] - Corp["Current_Liabilities"]
print(Corp)


#MARGINS&RATIOS



#Working capital increased from 19,000 in 2020 to 44,200 in 2025.

#This indicates that the company's current assets grew faster than its current liabilities,

#increasing the short-term financial buffer stock available to support operations.




Corp["Current_Ratio"]=Corp["Current_Assets"]/Corp["Current_Liabilities"]
print(Corp)

#Asses whether the company has short-term assets to cover its short-term obligations, providing a basic measure of short-term liquidity and financial flexibility


Corp["Quick_Ratio"]=(Corp["Current_Assets"]-Corp["Inventory"])/Corp["Current_Liabilities"]
print(Corp)

#whether the company can cover its short-term obligations without relying on the sale of inventory


Corp["Balance_Check"]=Corp["Total_Assets"]-(Corp["Total_Liabilities"]+Corp["Shareholders_Equity"])
print(Corp)
#Accounting-Equation



print(Corp[["Year","Total_Assets","Total_Liabilities","Shareholders_Equity"]])




Corp["Adjusted_Equity"]=Corp["Total_Assets"]-Corp["Total_Liabilities"]
print(Corp)



#This shows how much cash is left after funding all of the companies operating expenditue, this shows how much cash left for debt repayments,dividends, or reinvestments


Corp["Free_Cash_Flow"]=Corp["Operating_Cash_Flow"]-Corp["Capital_Expenditure"]
print(Corp)


#Measure how much of each unit of each revenue remains as free cash after capital expenditure. This lets us compare cash-generation effeciency as thew company grows
Corp["FCF_Margin"]=Corp["Free_Cash_Flow"]/Corp["Revenue"]*100
print(Corp)


#Asses how signficant investment cashflows are relative to the cash generated from operations. This helps evaluate how aggresively the company is reinvesting into long term assets

Corp["Investing_CF_Ratio"]=Corp["Investing_Cash_Flow"]/Corp["Operating_Cash_Flow"]
print(Corp)


#Measures how quickly a company collects cash from customers who bought on credit, lower days generally mean that customers are actually paying thier dues at times
Corp["Receivable_Days"]=Corp["Accounts_Receivable"]/Corp["Revenue"]*365
print(Corp)

#Measures how quickly the inventory is being sold
Corp["Inventory_Days"]=Corp["Inventory"]/Corp["COGS"]*365
print(Corp)


#Measures how long the company takes to pay its suppliers.helps assessing the correct management of working capital
Corp["Payable_Days"]=Corp["Accounts_Payable"]/Corp["COGS"]*365
print(Corp)

#Measures how effeicenly thecompany uses its assets base to generate revenue
Corp["Asset_Turnover"]=Corp["Revenue"]/Corp["Total_Assets"]
print(Corp)

#Meausures how effectively company convert its assets base into profits , this tells us whetehr the company is generating reutnrs or not
Corp["Return_on_Assets"]=Corp["Net_Profit"]/Corp["Total_Assets"]*100
print(Corp)

#measures the profit genrarted for the shareholders capital
Corp["ROE"]=Corp["Net_Profit"]/Corp["Adjusted_Equity"]*100

print(Corp)

#This shows the capital structure of the company  whether they r more debt based or equity based, this varies industyr to industry

Corp["Debt_To_Equity"]=Corp["Total_Liabilities"]/Corp["Adjusted_Equity"]
print(Corp)

#Shows how comfortably the oeprating profit of the company can cover interest payments
Corp["Interest_Coverage"]=Corp["EBIT"]/Corp["Interest_Expense"]
print(Corp)


#leverage compound of DPont ROE
Corp["Equity_multiplier"]=Corp["Total_Assets"]/Corp["Adjusted_Equity"]
print(Corp)


#breaksdown the DUPont driver into 3 ;profitabltiy,effeciency and financial leverage

Corp["Dupont_ROE"]=Corp["Net_Profit_Margin"]*Corp["Equity_multiplier"]*Corp["Asset_Turnover"]
print(Corp)


#The current ratio increased from approximately 2.41x in 2020 to 3.75x in 2025,

#while the quick ratio increased from 1.59x to 2.70x. Both ratios indicate

#an improving ability to cover short-term liabilities using current assets,

#including assets other than inventory. However, these ratios should be

#considered alongside working-capital efficiency and the quality of receivables.

#The balance check identified inconsistencies between reported shareholder

#equity and the accounting equation after 2020. Adjusted equity was calculated

#as total assets minus total liabilities for use in equity-based ratios.

#This adjustment supports analytical consistency but does not establish the

#correctness of the original financial statements.


#QUANTATIVE ANALYSIS

#shows how volatile the companies annual revenue growth has been, For financial anlaysis


Corp["Revenue_Growth_volatility"]=Corp["Revenue_Growth"].std()


print(Corp)

#assumptions of situation that revneue grows 5%
revenue_conservative=Corp["Revenue"].iloc[-1]*1.05
print(revenue_conservative)

#assumptions of situation that revneue grows 10%
revenue_base=Corp["Revenue"].iloc[-1]*1.1
print(revenue_base)
#assumptions of situation that revneue grows 15%
revenue_strong=Corp["Revenue"].iloc[-1]*1.15
print(revenue_strong)

#Measures the spread between the highest and lowest revenue scenarios

revenue_scenario_range=np.ptp([revenue_conservative,revenue_base,revenue_strong])
print(revenue_scenario_range)


#calcautes the average across all three results

revenue_scenario_average=np.mean([revenue_conservative,revenue_base,revenue_strong])
print(revenue_scenario_average)


#measures how sensitive revenue projection for 2026 is to differnet growht assuptions, this is mostly used for forecasting
revenue_difference_scenario=(revenue_strong-revenue_conservative)/revenue_conservative*100
print(revenue_difference_scenario)

ebitda_conservative = revenue_conservative * (Corp["EBITDA_Margin"].iloc[-1] / 100)
ebitda_base = revenue_base * (Corp["EBITDA_Margin"].iloc[-1] / 100)
ebitda_strong = revenue_strong * (Corp["EBITDA_Margin"].iloc[-1] / 100)

print(ebitda_conservative)
print(ebitda_base)
print(ebitda_strong)



#The revenue scenario analysis estimate 2026 revenue under three illustrative growth assumptions:5%,10%,and 15%. Based on 2025 revenue of 145000 , the projected outcomes range from 152250 under the conservative scenrio to 166750 under the strong-growth scenario, with a base-case estimate of 159500

#The differnce between conservative and strong-growth scenarios is 14500  equivalent to approximately 9.52% of the conservative scenario. This demonstrates how different growth assumptions can affect financial projections and highlights the importance of testing multiple scenarios rather than relying on a single estimate.

#Projected EBITDA ranges from approximately 44,625 to 48,875, assuming the latest EBITDA margin remains constant at approximately 29.31%. These figures illustrate how revenue growth could translate into higher operating earnings if the company's margin performance is maintained. However, the projections are assumption-based estimates and do not account for potential changes in costs, pricing, or operating conditions.

#Revenue growth volatility measures the historical variablity of annual revenue growth.It provides additional context for assessing the consistency of the company's growth , but historical volatility alone cannot determine future performance













import sqlite3
conn= sqlite3.connect("corporate_financials.db")
Corp.to_sql("Corp",conn,if_exists="replace",index=False)

query= "SELECT * FROM Corp"
sql_data=pd.read_sql(query,conn)

print(sql_data)



query=""" SELECT Year,Revenue FROM Corp ORDER BY Revenue DESC LIMIT 1;"""

result=pd.read_sql(query,conn)
print(result)



query=""" SELECT AVG(Net_Profit_Margin) AS Average_Net_Profit_Margin FROM Corp;"""

result=pd.read_sql(query,conn)
print(result)

query=""" SELECT Year, Revenue FROM Corp ORDER BY Year;"""

result=pd.read_sql(query,conn)
print(result)



query = """
SELECT
Year,
Revenue,
LAG(Revenue) OVER (ORDER BY Year) AS Previous_Revenue,
Revenue - LAG(Revenue) OVER (ORDER BY Year) AS Revenue_Change,
(Revenue - LAG(Revenue) OVER (ORDER BY Year)) * 100.0
/ LAG(Revenue) OVER (ORDER BY Year) AS Revenue_Growth
FROM Corp
ORDER BY Year;
"""

result = pd.read_sql(query, conn)
print(result)

query=""" SELECT Year,Net_Profit_Margin FROM Corp ORDER BY Net_Profit_Margin DESC LIMIT 1;"""

result = pd.read_sql(query, conn)
print(result)


query=""" SELECT Year,Current_Ratio FROM Corp WHERE Current_Ratio >3.0 ORDER BY Current_Ratio DESC;"""
result = pd.read_sql(query, conn)
print(result)

query = """
SELECT Year, Current_Ratio, Net_Profit_Margin
FROM Corp
WHERE Current_Ratio > 3.0
AND Net_Profit_Margin > 15.0
ORDER BY Year;
"""

result = pd.read_sql(query, conn)
print(result)



query=""" SELECT Year,Revenue ,Net_Profit_Margin,Current_Ratio,Asset_Turnover,Dupont_ROE FROM Corp ORDER BY Dupont_ROE DESC;"""
result = pd.read_sql(query, conn)
print(result)


conn.close()

import matplotlib.pyplot as plt



#REVENUE TREND
plt.plot(Corp["Year"],Corp["Revenue"])
plt.show()


# Profitablity Trend= Revenue growth wont show how good the company is doing that means profitability will be shown and visualized throught the net profit margin

plt.plot(Corp["Year"],Corp["Net_Profit_Margin"])
plt.xlabel("Year")
plt.ylabel("Net Profit Margin (%)")
plt.title("Net Profit Margin Trend")
plt.show()


#Comparison between EBITDA Margin And Net profit margin , this would assist us in understanding how much does the taxation and the other costs that are non operating have an effecton the margins andhow they react to revenue
plt.plot(Corp["Year"],Corp["EBITDA_Margin"],label="EBITDA Margin")
plt.plot(Corp["Year"],Corp["Net_Profit_Margin"],label="NET Profit Margin")


plt.xlabel("Year")
plt.ylabel("Margin (%)")
plt.title("EBITDA Margin Vs Net Profit Margin")
plt.legend()
plt.show()


#shows whetehre the copmany is able to cover its current liabilities and whether they have strenghtened or weakened over time


plt.plot(Corp["Year"],Corp["Current_Ratio"])

plt.xlabel("Year")
plt.ylabel("Current Ratio (x)")
plt.title("Current Ratio Trend")
plt.show()


#Show whether the company is generating increasing cash after funding its capital expenditures.

plt.plot(Corp["Year"],Corp["Free_Cash_Flow"])

plt.xlabel("Year")
plt.ylabel("Free Cash Flow")
plt.title("Free Cash Flow Trend")
plt.show()


#DuPont ROE, this shows the overall returns generated for shareholders over time. this is a useful final chart because DuPont ROE incorporates profitabality and asset effeciency as well as equity multiplier
plt.plot(Corp["Year"],Corp["Dupont_ROE"])

plt.xlabel("Year")
plt.ylabel("DuPont ROE(%)")
plt.title("Du Pont ROE TREND")
plt.show()


print(Corp[["Year","Revenue","EBITDA","EBITDA_Margin"]])


#Estimates EBITDA under each revenue scenario, assuming the latest
#EBITDA margin remains constant in 2026.


print("Conservative EBITDA:", ebitda_conservative)
print("Base-case EBITDA:", ebitda_base)
print("Strong-growth EBITDA:", ebitda_strong)

