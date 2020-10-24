# import packages to fetch distinguishing features
import numpy as np
import cv2
from matplotlib import pyplot as plt
from fpdf import FPDF
import requests
import urllib.parse
from bs4 import BeautifulSoup
import json
from datetime import date
from datetime import datetime
import random
### OBJECTIVE: print out daily facts
# web scraping for facts on fish
## bible verse
## https://towardsdatascience.com/restful-apis-in-python-121d3763a0e4

# place on pdf file and email it to myself

# Beautiful soup: https://www.tutorialspoint.com/beautiful_soup/index.htm
# Bible verse https://www.biblegateway.com/
# fish websites - oceana . org
# fishbase api: data about fish ecology, ecosystems, fecundity, food items, maturity, population growth, reproduction, species, and swimming, https://www.fishbase.se/search.php
##  https://github.com/ropensci/fishbaseapi
# fishwatch  https://www.fishwatch.gov/api/species

# GET https://fishbaseapi.info/species?Genus=Labroides
# api endpoints




def generateGeneralPdf(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=name, ln=1, align="C")
    return pdf

def main(name):
    pdf = generateGeneralPdf(name)

    pdf.cell(200, 10, txt="Challenges", ln=1, align="C")
    getBibleVerse(pdf)
    pdf.cell(200, 10, txt="Ideas to Share", ln=1, align="C")
    getShareableInfo(pdf)
    pdf.cell(200, 10, txt="Fish in Focus", ln=1, align="C")
    getFishInfo(pdf)

    email(pdf, name)


def getBibleVerse(pdf):
    # bible verse with fill in the blanks
    # take something from Isaiah and romans
    # actually not quite sure what I am meaning to do here
    # https://api.esv.org/docs/passage-text/
    baseurl = "https://api.esv.org/v3/passage/text/?q=John+11:35"
    # I am trying to  memorize Isaiah and romans
    # verses
    today = date.today()
    dayNumber = int(today.strftime("%d"))
    isaiahRange =  (dayNumber % 11) * 6 - 5
    romansRange =  (dayNumber % 8) * 2 - 1
    if romansRange == -1:
        romansRange = 15
    if isaiahRange == -1:
        isaiahRange = 61
    isaiah = {
      1: 31, 2: 22, 3: 26,
      4: 6,  5: 30, 6: 13,
      7: 25, 8: 22, 9: 21,
      10: 34, 11: 16, 12: 6,
      13: 22, 14: 32, 15: 9,
      16: 14, 17: 14, 18: 7,
      19: 25, 20: 6,  21: 17,
      22:25,  23: 18, 24: 23,
      25: 12, 26: 21, 27: 13,
      28: 29, 29: 24, 30: 33,
      31: 9,  32: 20, 33: 24,
      34: 17, 35: 10, 36: 22,
      37: 38, 38: 21, 39: 8,
      40: 31, 41: 29, 42: 25,
      43: 28, 44: 28, 45: 25,
      46: 13, 47: 15, 48: 22,
      49: 26, 50: 11, 51: 23,
      52: 15, 53: 12, 54: 17,
      55: 13, 56: 12, 57: 21,
      58: 14, 59: 21, 60:22,
      61: 11, 62: 12, 63: 19,
      64: 12, 65: 25, 66: 24
    }

    romans = {
     1: 32, 2: 29,
     3: 31, 4: 25,
     5: 21, 6: 22,
     7: 25, 8: 39,
     9: 33, 10: 21,
     11: 36, 12: 21,
     13: 14, 14: 23,
     15: 33, 16: 27
    }

    for x in range(isaiahRange, isaiahRange+6):
        statementstring = "Isaiah " + str(x) + ": " + str(random.randint(1, isaiah[x]))
        if x % 2 != 0:
            pdf.cell(20)
            pdf.cell(10, 5, txt=statementstring, ln=0)
        else:
            pdf.cell(20)
            pdf.cell(10, 5, txt=statementstring, ln=1)

    for x in range(romansRange, romansRange + 2):
        statementstring = "Romans " + str(x) + ": " + str(random.randint(1, romans[x]))
        if x % 2 != 0:
            pdf.cell(20)
            pdf.cell(10, 5, txt=statementstring, ln=0)
        else:
            pdf.cell(20)
            pdf.cell(10, 5, txt=statementstring, ln=1)






def getGermanSentences(pdf):
    #might not be a good thing to do, as it is not a high priority
    #German phrases to learn
    return pdf

def getFishInfo(pdf):
    fishToFetch = {
       1: {
         "species" : "furcatus",
         "genus" : "Ictalurus"
       },
       2: {
         "species" : "macrochirus",
         "genus" : "Lepomis"
       },
       3: {
        "species": "peelii",
        "genus": "Maccullochella"
       }
    }
    randFish = random.randint(1, 3)
    baseurl = "https://fishbase.ropensci.org//species?Genus="+fishToFetch[randFish]["genus"] + "&Species="+fishToFetch[randFish]["species"]
    print(baseurl)
    #baseurl = "https://fishbase.ropensci.org//species?Genus=Tilapia"
    fishresponse = requests.get(baseurl)
    fishjson = fishresponse.json()
    fishdata = fishjson.get("data")

    # attributes to print out: Genus, Species, fresh, brack, saltwater, LongevityCaptive, Weight, PriceCateg
    itemsToFetch = {
        0: "Genus",
        1: "Species",
        2: "Comments",
        3: "Weight"
    }
    for item in fishdata:
        for x in range(len(itemsToFetch)):
            key = str(itemsToFetch.get(x))
            wholestring =  str(item.get(key))
            increment = 75
            step = 0
            value = wholestring[(step*increment):(step+1)*increment-len(wholestring)]
            step = step + 1

            statementstring = str(key) + ": " + str(value)
            pdf.cell(20)
            pdf.cell(10, 5, txt=statementstring, ln=1)
            breaksUsed = False
            while len(wholestring) > step*increment:
                breaksUsed = True
                value = wholestring[(step*increment):(step+1)*increment-len(wholestring)]
                statementstring = str(value)
                if len(statementstring) != 0:
                    pdf.cell(20)
                    pdf.cell(10, 5, txt=statementstring, ln=1)
                step = step + 1
            if breaksUsed == True:
                value = wholestring[(step-1)*increment:]
                statementstring = str(value)
                pdf.cell(20)
                pdf.cell(10, 5, txt=statementstring, ln=1)








def getShareableInfo(pdf):
    # could be quote from spurgeon, article from voice of the Martyrs, whatever
    return pdf

def email(pdf, name):
    pdf.output(name + str(random.randint(11,20)) + ".pdf")


main("Fish Facts")
