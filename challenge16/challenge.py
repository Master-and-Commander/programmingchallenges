# print weekly pdf to remind me of what I ought to do for my fish

#

import json
from datetime import date
from datetime import datetime
import copy
from fpdf import FPDF
import random


### GRAND VIEW
# print pdf with daily and weekly tasks
# later on incorporate sensors [count fish, show pH level, oxygen level, temperature, water quality]


# next step

def main(file):
    today = date.today()
    d2 = today.strftime("%d/%m/%Y")

    # read json file
    with open(file, "r") as openfile:
        fishData = json.load(openfile)

    # check if up to date
    if(str(fishData.get("lastDate")) == str(d2)):
        print("Up to date")

    writeToFile(file, fishData, d2)




def writeToFile(jsonFile, fishData, d2):
    # update lastupdated date and write to file
    fishData["lastDate"] = str(d2)
    with open(jsonFile, 'w') as outfile:
        json.dump(fishData, outfile)

    # print out a pdf with details
    name = "Week To Dos"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=name, ln=1, align="C")

    for tank in fishData.get("tanks").keys():
        pdf.cell(20)
        pdf.cell(10, 5, txt=str(fishData.get("tanks").get(tank)), ln=1)

    pdf.output(name + str(random.randint(11,20)) + ".pdf")

main("fishinfo.json")
