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
# later on incorporate sensors


# next step
# print out fish sensor data as a graph


def main(file):
    today = date.today()
    d2 = today.strftime("%d/%m/%Y")

    # read json file
    with open(file, "r") as openfile:
        fishData = json.load(openfile)

    # check if up to date
    if(str(fishData.get("lastDate")) == str(d2)):
        print("Up to date")
    else:
        print("Fish ages may need to be updated")

    writeToFile(file, fishData, d2)


def sensors(pdf):
    sensorData = {}
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Special to Dos", ln=1, align="C")

    for x in range(9):
        # pick up data from sensors
        # maybe print out as a graph
        fish = 20
        pH = 7
        oxygen = 7
        temperature = 60
        quality = 1
        sensorData[x+1] = {
           "fish": fish,
           "pH": pH,
           "oxygen": oxygen,
           "temperature": temperature,
           "quality": quality
        }
        strtouse = "Tank " + str(x+1) + ": " +str(sensorData[x+1]["fish"])
        pdf.cell(20)
        pdf.cell(10, 5, txt=strtouse, ln=1)


    print("Trying to sense")
    print(sensorData)
    return pdf
    # functions that may be done:
    ## counting fish, sense pH level, oxygen level, temp, water quality

def assessTank(pdf, fishData):
    commands = {
      1: "Feed 3 times a day",
      2: "2 Month",
      3: "3 Month",
      4: "4 Month",
      5: "5 Month",
      6: "6 Month",
      7: "7 Month",
      8: "8 Month",
      9: "Time to harvest"
    }
    sensors(pdf)
    # for age
    for tank in fishData.get("tanks"):
        strtouse = "Tank " + str(tank) + ": " +str(commands.get(fishData.get("tanks").get(tank).get("age")))
        pdf.cell(20)
        pdf.cell(10, 5, txt=strtouse, ln=1)
    return pdf

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

    assessTank(pdf, fishData)

    pdf.output(name + str(random.randint(11,20)) + ".pdf")

main("fishinfo.json")
