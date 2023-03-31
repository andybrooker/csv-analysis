import pandas as pd

df = pd.read_csv("dummy_data.csv")

# Calculate revenue.
revenue = df[df['category'] == "Revenue"]
revenue['date'] = pd.to_datetime(revenue['date'])
monthly_revenue_df = revenue.groupby(pd.Grouper(key='date',
                                                freq='M'))['amount'].sum()

monthly_revenue = monthly_revenue_df[1].mean()
print('Monthly revenue:', monthly_revenue)

# Calculate gross burn rate.
expenses = df[df['amount'] < 0]
expenses['date'] = pd.to_datetime(expenses['date'])
monthly_expenses = expenses.groupby(pd.Grouper(key='date',
                                               freq='M'))['amount'].sum()

gross_burn_rate = -1 * monthly_expenses[1].mean()
print('Gross burn rate:', gross_burn_rate)

# Calculate most recent balance.
df['date'] = pd.to_datetime(df['date'])
final_date = df['date'].max()
final_transactions = df[df['date'] == final_date]
final_balance = final_transactions['balance'].iloc[-1]
print('Final balance:', final_balance)

# Calculate runway
runway = final_balance / gross_burn_rate
print('Runway (months): ', runway)

# Breakdown Revenue by Merchant.
revenue_by_merchant = revenue.groupby('merchant')['amount'].sum()

# Print the revenue by merchant
print('Revenue by Merchant:', revenue_by_merchant)
