# To inform me in my planning decisions has to what is the next best move given my resources
# Format of json file to use (check capital.json)


#### NEXT CHANGE: If item in external cost does not exist in current Resources
##### get dollar amount from "items "

import numpy as np
import sys
import json
from datetime import date
from datetime import datetime
import copy

def main(file):
    today = date.today()
    d2 = today.strftime("%d/%m/%Y")

    # read json file
    with open(file, "r") as openfile:
        jsonData = json.load(openfile)

    # check if not up to date. If not, account for added and lost resources
    if(str(jsonData.get("lastDate")) == str(d2)):
        print("Nothing to update")
    else:
        jsonData = showGains(jsonData, d2)
    showRecommendations(jsonData)
    # offer recommendations

    writeToFile(file, jsonData, d2)
    # ask if any of the recommendations have been accomplished
    # if so update capital.json and exit

def writeToFile(jsonFile, jsonData, d2):
    # update lastupdated date and write to file
    jsonData["lastDate"] = str(d2)
    with open(jsonFile, 'w') as outfile:
        json.dump(jsonData, outfile)


def showGains(jsonData, last):
    # use elapsed time to calculate changes in finances
    d1 = datetime.strptime(jsonData.get("lastDate"), "%d/%m/%Y").date()
    d2 = datetime.strptime(last,"%d/%m/%Y").date()
    months = (d2.year - d1.year) * 12 + d2.month - d1.month
    jsonData['resources'] = getMonthlyGains(jsonData,months)


    return jsonData


def getMonthlyGains(jsonData, months):
    # leave the option to not mess with the original
    availableResources = copy.deepcopy(jsonData.get("resources"))

    print("Projecting gains for " + str(months) + " months")

    externalCosts = jsonData.get("externalCosts")

    # resource Costs
    for item in availableResources.keys():
        if "costs" in  jsonData.get("items").get(item).keys():
            for cost in jsonData.get("items").get(item).get("costs"):
                costtype = cost["name"]
                costamount = cost["quantity"]
                if costtype in availableResources.keys():
                    availableResources[costtype] = availableResources[costtype] -  months * costamount
                else:
                    availableResources['dollars'] = availableResources['dollars'] - months *  jsonData.get("items").get(item).get("dollarValue")
        if "yields" in  jsonData.get("items").get(item).keys():
            for theYield in jsonData.get("items").get(item).get("yields"):
                yieldtype = theYield["name"]
                yieldamount = theYield["quantity"]
                if yieldtype in availableResources.keys():
                    availableResources[yieldtype] = availableResources[yieldtype] + months * yieldamount
                else:
                    availableResources[yieldtype] = months * yieldamount


    ## external costs
    for cost in externalCosts.keys():
        if cost in availableResources.keys():
            availableResources[cost] = availableResources[cost] - months * externalCosts[cost]
        elif cost == "dollars":
            availableResources["dollars"] = availableResources["dollars"] - months * externalCosts.get("dollars")
        else:
            ## get dollar amount
            availableResources["dollars"] = availableResources["dollars"] - months * jsonData.get("items").get(cost).get("dollarValue")





    return availableResources




def showRecommendations(jsonData):
    # look at goals
    # list what goals are lacking
    # whatever is lacking the least goes up
    # recommend buying stuff up to point of costs

    # find out operating costs
    availableResources = getMonthlyGains(jsonData, 1)
    print("Available Resources")
    print(availableResources)


def questionIfDone(jsonData, options):
    return 5

def getPriceOfItem(jsonData, name):
    # used recursively to calculate the cost of something
    # as well as feasibility
    return 5


main("capital.json")
