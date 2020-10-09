# To inform me in my planning decisions has to what is the next best move given my resources
# Format of json file to use
# {
#  "personal" : {},
#  "resources" : [{"name":"finances", "quantity": "1", "amount": "$5,000", "yield": "$1,500"}, {"name":"house", "quantity": "0", "amount": "$30,000",  "yield": "$0"}],
#  "goals": [{"name":"Aquponics system for catfish", "value": "12" }]
#  "items": [{"name":"Aquponics system for catfish", "requirements": [{"name":"clay pellets", "quantity": "100lb", "price": "$99.99"}] }]
# }

import numpy as np
import sys
import json
from datetime import date
from datetime import datetime

def main(file):
    today = date.today()
    d2 = today.strftime("%d/%m/%Y")
    # read json file, see resources and check what is possible
    # recommend whatever is the next best thing to start
    with open(file, "r") as openfile:
        jsonData = json.load(openfile)
    # 1: check goals
    # 2:

    if(str(jsonData.get("currentDollars").get("lastDate")) == str(d2)):
        print("Nothing to update")
    else:
        # from that last month on, go through resources and increment gains
        showGains(jsonData, d2)


    # begin with recommendations
    # ask if any of the recommendations have been accomplished
    # if so update capital.json and exit

def writeToFile(jsonData):
    # write existing json data to capital.json
    return 5


def showGains(jsonData, last):
    d1 = datetime.strptime(jsonData.get("currentDollars").get("lastDate"), "%d/%m/%Y").date()
    d2 = datetime.strptime(last,"%d/%m/%Y").date()
    print("d1: " + str(d1.month))
    print("d2: " + str(d2.month))
    difference = (d1.year - d2.year) * 12 + d1.month - d2.month
    print(difference)


def questionIfDone(jsonData, options):
    return 5

def getPriceOfItem(jsonData, name):
    # used recursively to calculate the cost of something
    # as well as feasibility
    return 5


main("capital.json")
