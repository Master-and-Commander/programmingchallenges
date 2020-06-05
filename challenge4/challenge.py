import pandas as pd
import matplotlib as plt
import numpy as np
import requests
import json
import openpyxl
from openpyxl.chart import (
    LineChart,
    Reference,
)


#generate a daily report
### 1 data gathering
## a) API keys

## b) parameters
interval = 15
range = 1
tesla = {
    "symbol": "TSLA",
    "api_token" : stockkey,
    "interval" : interval,
    "range" : range,
    "sort" : "oldest"
}
amazon = {
    "symbol": "AMZN",
    "api_token" : stockkey,
    "interval" : interval,
    "range" : range,
    "sort" : "oldest"
}

apple = {
    "symbol": "AAPL",
    "api_token" : stockkey,
    "interval" : interval,
    "range" : range,
    "sort" : "oldest"
}

weatherzip = "92592"
weathercountry = "us"
## c) requests
teslaresponse = requests.get("https://intraday.worldtradingdata.com/api/v1/intraday", params = tesla)
amazonresponse = requests.get("https://intraday.worldtradingdata.com/api/v1/intraday", params = amazon)
appleresponse = requests.get("https://intraday.worldtradingdata.com/api/v1/intraday", params = apple)
# responseweather = requests.get("https://api.openweathermap.org/data/2.5/weather?zip="+ weatherzip + ","+weathercountry)
### 2 processing data
## a) loading data
tesladata = json.loads(teslaresponse.text)
amazondata = json.loads(amazonresponse.text)
appledata = json.loads(appleresponse.text)
#with open('stocksdata.txt') as json_file:
#    stocksdata = json.load(json_file)

# making use of data

teslavalues = []
amazonvalues = []
applevalues = []

for price in tesladata["intraday"].values():
    teslavalues.append(float(price['open']))

for price in amazondata["intraday"].values():
    amazonvalues.append(float(price['open']) - 1500)

for price in appledata["intraday"].values():
    applevalues.append(float(price['open']))




myindex = []
beginning = 0
for y in teslavalues:
    myindex.append(beginning)
    beginning = beginning + 1

tesla = pd.Series(teslavalues, index=myindex)
amazon = pd.Series(amazonvalues, index=myindex)
apple = pd.Series(applevalues, index=myindex)


alldata = {"Tesla" : tesla,
      "Amazon": amazon,
      "Apple" : apple
      }
data = pd.DataFrame(alldata)


wb = openpyxl.Workbook()
sheet = wb.active
for row in data.itertuples():
    sheet.append(row)
dimensions = Reference(sheet, min_col = 2, min_row = 1, max_col=4, max_row = 26)

chart = LineChart()
chart.add_data(dimensions)
sheet.add_chart(chart,"H2")
wb.save("infotoday3.xlsx")
