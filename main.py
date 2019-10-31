import pandas as pd
import plotly.express as px
from datetime import datetime

# Import interest rate data
interest_rate = pd.read_csv("Bank Rate  Bank of England Database.csv")

print(interest_rate.head())
print(interest_rate.columns)

def date_change(x):
    
    months = {
        "Jan": "January", 
        "Feb": "February", 
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December"}
    
    day, month, year = x.split(' ')

    astr = year + months[month] + day

    date_object = datetime.strptime(astr, '%y%B%d')

    return date_object

interest_rate['NewDate'] = interest_rate['Date Changed'].apply(date_change)


fig = px.line(interest_rate, x='NewDate', y='Rate', line_shape='vh')
fig.show()

















hpi = pd.read_csv("UK-HPI-full-file-2019-06.csv")

print(hpi.columns)
print(hpi.head())

avg_prices = pd.read_csv("Average-prices-2019-06.csv")

print(avg_prices.columns)
print(avg_prices.head())

criteria = avg_prices['Region_Name'] == "England"

new = avg_prices[criteria]

new = new[["Date", "Region_Name", "Average_Price"]]

print(new)




#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = px.line(new, x='Date', y='Average_Price')
fig.show()