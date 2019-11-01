import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots
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
fig.update_layout(xaxis_range=['1975-01-01','2019-01-01'])
fig.update_layout(title_text='Time Series with Rangeslider',
                  xaxis_rangeslider_visible=True)
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

#fig = px.line(interest_rate, x='NewDate', y='Rate', line_shape='vh')


# Make lists from Pandas series
a = interest_rate["NewDate"].tolist()
b = interest_rate["Rate"].tolist()
c = new["Date"].tolist()
d = new["Average_Price"].tolist()


# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=a, y=b, name="yaxis data", line_shape='vh'),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=c, y=d, name="yaxis2 data"),
    secondary_y=True,
)

# Add figure title
fig.update_layout(
    title_text="Double Y Axis Example",
    xaxis_range=['1975-01-01','2019-01-01']
)

# Set x-axis title
fig.update_xaxes(title_text="xaxis title")

# Set y-axes titles
fig.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
fig.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)

fig.show()