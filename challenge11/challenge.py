import array
import numpy as np
import random
import requests
import json
from os import environ as env
from dotenv import load_dotenv

# Return shopping list to fulfill requirements for cheapest price
def returnRequirements():
    requirementsMg = {
    "Calcium": 1200,
    "Magnesium": 10,
    "Iron": 18,
    "Potassium": 4700
    }
    print("Returning requirements")
    return requirementsMg

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
    baseurl = "https://api.kroger.com/v1/products?filter.brand=Kroger&filter.term="+term+"&filter.zipCode.near=37803"
    baseurlHeaders =    {
        "Accept": "application/json",
        "Authorization": "Bearer " + token
    }
    baseurlResponse = requests.get(baseurl, headers=baseurlHeaders)
    baseurlJson = baseurlResponse.json()
    print(baseurlJson.get('data')[0]["items"])


def main():
    load_dotenv()
    accessData = getAccessToken(env['API_KEY'])
    token = accessData.get('access_token')
    requestData(token, "Chicken")
    #requestData(token, "Beef")


def returnMenu():
    menu = ["Chicken", "Fish", "Shrimp", "Eggs", "Butter", "Beef", "Turkey"]

    print("Returning menu")
    return menu


def returnPrices():
    prices = []
    print("ReturningPrices")
    return prices

main()
#print(requestData())
