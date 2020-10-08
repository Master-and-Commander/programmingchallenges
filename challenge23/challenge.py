from fpdf import FPDF
import array
import numpy as np
import random
from numpy import *
import csv
import sys
import pandas

def main(name,file):
    # point of script is to display weekly events and challenges
    # using csv files as ways to make informed decisions
    # should run on every Sunday at 4:00AM (if this is possible)
    pdf = generateGeneralPdf(name)
    #fields are: type	extra	date	start	end	value	statement
    # fields of type 'day' are used for scheduling. 'Extra' field will indicate if it is a one time event or continous (if one-time, this may be promptly removed from csv file)
    # fields of type 'challenge' are incremented

    csvFile = pandas.read_csv(file)
    pdf = displayWeeklyEvents(pdf, csvFile)
    pdf = displayChallenges(pdf, csvFile)
    renderPdf(pdf,name)

def generateGeneralPdf(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=name, ln=1, align="C")
    return pdf

def displayWeeklyEvents(pdf, csvFile):
    #display weekly events
    print(csvFile)
    return pdf

def displayChallenges(pdf, csvFile):
    # display challenges
    return pdf


def renderPdf(pdf,name):
    pdf.output(name + str(random.randint(1,100)) + ".pdf")


main('Weekly Report','weeklydetails.csv')
