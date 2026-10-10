# Financial Transaction and Corporate Financial Analysis

## About the Project

I built this project to apply Python and data analysis to financial information rather than relying only on traditional accounting calculations. It started with personal financial transactions and then moved into a more detailed analysis of corporate financial performance.

The project combines financial knowledge with practical work in Python, Pandas, NumPy, SQL, and data visualisation. My main goal was to understand how these tools can be used to analyse financial results, identify trends, and make the findings easier to interpret.

## Tools Used

- **Python** for calculations and analysis
- **Pandas** for working with and transforming datasets
- **NumPy** for numerical calculations and scenario analysis
- **SQL and SQLite** for querying financial data
- **Matplotlib** for creating charts

## 1. Personal Financial Analysis

The first part focuses on transaction data. I worked with income and expenses, grouped transactions by category and month, and examined spending patterns.

I also created additional columns to classify transactions and calculate values that could be used for further analysis. This helped me practise manipulating DataFrames and turning raw transaction records into more useful summaries.

## 2. Corporate Financial Analysis

The second part uses a corporate financial dataset covering 2020–2025. I calculated and analysed several financial metrics to understand how the company's performance changed over time.

The analysis covers:

- Revenue, gross profit, EBITDA, and net income
- Gross profit, EBITDA, and net profit margins
- Working capital, current ratio, and quick ratio
- Receivables days and asset turnover
- Operating cash flow and free cash flow
- Return on assets (ROA) and return on equity (ROE)
- DuPont analysis to examine the factors behind ROE
- Revenue growth assumptions and EBITDA scenarios

I also added comments explaining what the results suggest, rather than treating the calculations as the end of the analysis.

## 3. SQL and Data Visualisation

I used SQLite to store the corporate dataset and practise querying it. The SQL exercises include retrieving the highest values, calculating average margins, examining revenue growth, and filtering results using financial ratios.

I created Matplotlib charts to make the main trends easier to see, including revenue, profitability margins, the current ratio, free cash flow, and DuPont ROE.

## What the Results Showed

Between 2020 and 2025, revenue increased from 85,000 to 145,000, while net income rose from 7,600 to 30,100. EBITDA increased from 16,000 to 42,500 over the same period.

Liquidity also improved: the current ratio increased from approximately 2.41x to 3.75x. Free cash flow rose from 4,000 to 9,500, and DuPont ROE increased from approximately 23.03% to 36.62%.

Asset turnover remained broadly stable. This suggests that the increase in revenue was accompanied by growth in the company's asset base, rather than a substantial improvement in revenue generated per unit of assets.

These results show improving profitability, liquidity, and cash generation in the supplied dataset. They do not, on their own, explain the reasons behind every change or establish how the company would perform in the future.

## Data Limitations

During the analysis, I identified inconsistencies in the reported shareholders' equity figures after 2020. To keep the equity-based calculations internally consistent, I calculated adjusted equity as total assets minus total liabilities.

This adjustment does not confirm which original figures are correct, so the equity-based results should be interpreted with that limitation in mind.

The 2026 revenue and EBITDA scenarios are estimates based on assumed growth rates and a constant EBITDA margin. They are intended to show how different assumptions affect the results, not to predict actual company performance.

The corporate figures are from the supplied dataset and should not be treated as verified financial statements for a real company.

## What I Practised

Through this project, I worked on financial ratio analysis, Pandas DataFrame manipulation, numerical calculations, SQL queries, and chart creation. I also practised checking the consistency of financial data and explaining what the results mean.

The project is a starting point for further work in financial data analytics and FinTech, particularly in combining financial analysis with programming.

## Running the Project

1. Download or clone the repository.
2. Install Python and the required libraries.
3. Open the project folder in VS Code.
4. Run the relevant Python file from the project directory.

The project uses CSV data and a local SQLite database for the corporate analysis.
