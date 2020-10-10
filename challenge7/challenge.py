# To inform me in my planning decisions has to what is the next best move given my resources
# Format of json file to use (check capital.json)


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
    dictionaryCosts = {}
    dictionaryYields = {}
    # leave the option to not mess with the original
    availableResources = copy.deepcopy(jsonData.get("resources"))
    print("Projecting gains for " + str(months) + " months")

    # Get monthly costs and yields associated with each resource
    for resource in availableResources:
        name = resource.get("name")
        quantity = resource.get("quantity")

        # yields and costs associated with resource
        resourceYields = jsonData.get("items").get(name).get("yields")
        print("resource yields for " + name)
        print(resourceYields)
        resourceCosts = jsonData.get("items").get(name).get("costs")

        # for each yield for that item, at to yields to track
        for ayield in resourceYields:
            if ayield.get("repeating") == "yes":
                if(ayield.get("name") in dictionaryYields):
                    dictionaryYields[ayield.get("name")] = months * float(ayield.get("quantity")) + dictionaryYields[ayield.get("name")]
                else:
                    dictionaryYields[ayield.get("name")] = months * float(ayield.get("quantity"))

        # same for costs
        for acost in resourceCosts:
            if acost.get("repeating") == "yes":
                if(acost.get("name") in dictionaryCosts):
                    dictionaryCosts[acost.get("name")] = months * float(acost.get("quantity")) + dictionaryCosts[acost.get("name")]
                else:
                    dictionaryCosts[acost.get("name")] = months * float(acost.get("quantity"))


    for cost in dictionaryCosts:
        for resource in availableResources:
            if resource.get("name") == cost:
                resource["quantity"] = resource["quantity"] - dictionaryCosts[cost]

    # 'yield' is causing syntax error
    for x in dictionaryYields:
        for resource in availableResources:
            if resource.get("name") == x:
                resource["quantity"] = resource["quantity"] + dictionaryYields[x]

    for externalCost in jsonData.get("externalCosts"):
        for resource in availableResources:
            if resource.get("name") == externalCost.get("type"):
                resource["quantity"] = resource["quantity"] - months *  externalCost["cost"]

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
