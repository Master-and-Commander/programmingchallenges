# import packages to fetch distinguishing features
import numpy as np
import cv2
from matplotlib import pyplot as plt
from fpdf import FPDF
import requests
import urllib.parse
from bs4 import BeautifulSoup
import json
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

def main():
    pdf = generateGeneralPdf("Daily Facts")
    pdf = getBibleVerse(pdf)
    pdf = getFishInfo(pdf)
    pdf = getShareableInfo(pdf)
    email(pdf)


def getBibleVerse(pdf):
    return pdf


def getFishInfo(pdf):
    baseurl = "https://fishbase.ropensci.org//species?Genus=Labroides"
    #fishresponse=requests.get(baseurl)
    fishresponse = requests.get(baseurl)
    print(fishresponse.json())
    #print(fishresponse)
    # fishbase seabase
    return pdf


def getShareableInfo(pdf):
    return pdf

def email(pdf):
    return(pdf)


main()
