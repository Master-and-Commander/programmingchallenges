import array
import numpy as np
import random
import requests
import json
import urllib.request
from os import environ as env
from dotenv import load_dotenv
import re
# Return shopping list to fulfill requirements for cheapest price


def getAccessToken(key):
    oauthurl = "https://api.kroger.com/v1/connect/oauth2/token"
    oauthurlHeaders = {"Authorization": "Basic " + key,
    "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {"grant_type":"client_credentials","scope":"product.compact"}
    oauthurlResponse = requests.post(oauthurl, headers=oauthurlHeaders, params=params)
    oauthurlJson = oauthurlResponse.json()
    return oauthurlJson



def requestData(token, term):
    #specific baseurl = "https://api.kroger.com/v1/products?filter.productId=0073114951527&filter.locationId=02600862"
    baseurl = "https://api.kroger.com/v1/products?filter.term="+term+"&filter.locationId=02600862&filter.limit=3"
    productdetails = []
    baseurlHeaders =    {
        "Accept": "application/json",
        "Authorization": "Bearer " + token
    }
    baseurlResponse = requests.get(baseurl, headers=baseurlHeaders)
    baseurlJson = baseurlResponse.json()
    #url = "https://www.kroger.com/p/"+description.replace(" ","-")+"/"+id
    #returnDetailsforProduct(url)
    sizepattern = r'(?P<number>\d+) (?P<unit>\w+)'
    compiledsizepattern = re.compile(sizepattern)
    for product in baseurlJson.get('data'):
        # price per weight
        productId = product.get('productId')
        price = product.get('items')[0].get("price").get("regular") if (product.get('items')[0].get("price").get("promo") == 0) else product.get('items')[0].get("price").get("promo")
        match = compiledsizepattern.match(product.get('items')[0].get("size"))
        # ounce to pound is .0625
        if match != None:
            if match.group('unit') == "oz":
                numberinpounds = float(match.group('number')) * .0625
            else:
                numberinpounds = float(match.group('number'))
            priceperpound = price / numberinpounds
            priceperpound = round(priceperpound,2)

            productdetails.append({
                "productId": productId,
                "price": price,
                "priceperpound": priceperpound,
                "description": product.get('description'),
                "poundage":numberinpounds
                #"aisleLocations": product.get('aisleLocations')
            })


    return sorted(productdetails, key = lambda item: item['priceperpound'])

def returnText(uri):
    load_dotenv()
    krogerpath = uri[22:]
    expandedHeaders = {
        "user-agent":env['USER-AGENT'],
        "accept":env['KROGER-ACCEPT'],
        "cookie":env['KROGER-COOKIE'],
        "path": krogerpath,
        "accept-language":env["ACCEPT-LANGUAGE"]}
        # see if you need cache-control:no-cache and pragma no cache

    basicHeaders = {
        "user-agent":env['USER-AGENT']
    }

    # determine which headers to use
    headers = expandedHeaders if "kroger" in uri else basicHeaders
    req = urllib.request.Request(uri, headers=headers)
    try:
        with urllib.request.urlopen(req,timeout=7) as source:
            text = source.read().decode()
        return text
    except Exception as err:
        print(err)
        return None

def returnDetailsforProduct(uri):
    tries = 0
    text = None
    while (text == None or tries < 3 ):
        tries +=1
        text = returnText(uri)
    if text != None:
        patterns = [
                r'<[A-z \-"=></]+kds-Price-promotional[A-z \-"=/><.]+>(?P<dollars>\d+)<[A-z \-/"=<>]+>',
                r'<[A-z \-"=></]+kds-Price-superscript[A-z \-"=/><.]+>(?P<cents>\d+)<[A-z \-/"=<>]+>',
                r'Located in Aisle (?P<Aisle>\d+)',
                r'[A-z <>/\d]+Serving size[A-z <>/\d]+\((?P<servinggrams>[\d.]+)[ g]+\)',
                r'<[A-z \-"=]+price-mantissa[A-z \-"=]+>(?P<cents>[\d,]+)<[A-z \-/"=]+>',
                r'<[A-z \-"=]+price-characteristic[A-z \-"=]+>(?P<dollars>[\d,]+)<[A-z \-/"=]+>'
            ]

        interests = [
            "Total Fat", "Saturated Fat",
            "Trans Fat", "Polyunsaturated Fat",
            "Monounsaturated Fat", "Cholesterol",
            "Sodium", "Dietary Fiber",
            "Sugar", "Calcium",
            "Vitamin A", "Vitamin C",
            "Calories", "Iron",
            "Protein"]
        # setting patterns for nutrition facts
        for interest in interests:
            standardized = interest.lower().replace(" ", "")

            patterns.append(r'[A-z <>/\."]+' + interest + r'[A-z <>/\."]+(?P<'+ standardized + r'>[\d,.]+)')

        resultsdict = {}
        for x in patterns:
            details = re.search(x,text)
            if details != None:
                key = list(details.groupdict().keys())[0]
                resultsdict[key] = details.groupdict()[key]

        return resultsdict
    else:
        print("There was no successful connection")
        return {}


def evaluateProduct(product, weeklyNeeds):
    url = "https://www.kroger.com/p/item/" + product.get("productId")
    productNutrition = returnDetailsforProduct(url)
    detailsToReturn = product

    # 1 gram is 0.00220462 pounds
    # return percentage of weekly needs per bag
    if "servinggrams" not in productNutrition:
        return {}
    servinggrams = float(productNutrition.get("servinggrams"))
    gramsinproduct = product.get("poundage") / .00220462
    multiplier = gramsinproduct / servinggrams

    for nutrient in weeklyNeeds.keys():
        if nutrient in productNutrition:
            servingsizenutrient = float(productNutrition.get(nutrient))
            bagInput = multiplier * servingsizenutrient
            servingpercentage = round(bagInput/weeklyNeeds.get(nutrient)*100,2)
            detailsToReturn[nutrient] = servingpercentage
            detailsToReturn[nutrient+"toPrice"] = round(bagInput/product.get("price"),2)
            detailsToReturn[nutrient+"inProduct"] = bagInput
        else:
            detailsToReturn[nutrient+"toPrice"] = 0
            detailsToReturn[nutrient+"inProduct"] = 0

    return detailsToReturn



def returnHowMuchToBuy(shoppingList, weeklyNeeds):
    # for each nutrient in weekly needs order shopping list by the best food for that nutrient, then meet need, then add to final finalList
    weeklyFulfillments  = weeklyNeeds
    finalList = []
    for nutrient in weeklyNeeds.keys():
        # order shopping list by that nutrient
        workingList = sorted(shoppingList, key = lambda item: item[nutrient+'toPrice'], reverse=True)
        winningProductForNutrient = workingList[0]
        numberOfOrders = 1
        while winningProductForNutrient[nutrient+"inProduct"]*numberOfOrders < weeklyFulfillments.get(nutrient)* 0.75:
            numberOfOrders+=1

        # reduce other needed nutrients as well
        for nutrient in weeklyNeeds.keys():
            weeklyFulfillments[nutrient] = weeklyFulfillments.get(nutrient) - winningProductForNutrient[nutrient+"inProduct"]*numberOfOrders

        finalList.append(str(numberOfOrders) + " " + winningProductForNutrient['description'] + ": " + str(winningProductForNutrient["price"]*numberOfOrders) )

    print(weeklyFulfillments)
    return finalList

def main():
    weeklyNeeds = {
        "calcium":7000,
        "iron":56,
        "protein":1050,
        "calories":14000
    }
    weeklyNeeds = {
        "iron":56,
        "protein":1050,
        "calories":14000
    }
    load_dotenv()
    #use key and token for access
    accessData = getAccessToken(env['API_KEY'])
    token = accessData.get('access_token')
    topcategories = {}
    shoppingList = []

    # issues
    # milk serving size comes in mL, also 'size' may be different


    # request local data on fish, meat, vegetables
    for term in ["shrimp", "beef", "chicken", "milk", "spinach"]:
        topcategories[term] = requestData(token, term)
        # best price per pound goes to top per category
        product = evaluateProduct(topcategories[term][0],weeklyNeeds)
        if product != {}:
            shoppingList.append(evaluateProduct(topcategories[term][0],weeklyNeeds))

    # now how much to buy for each thing

    finalList = returnHowMuchToBuy(shoppingList, weeklyNeeds)
    for item in finalList:
        print(item)




#main()
load_dotenv()
#use key and token for access
accessData = getAccessToken(env['API_KEY'])
token = accessData.get('access_token')
print(requestData(token, "salmon"))
