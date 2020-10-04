# import packages to fetch distinguishing features
import numpy as np
import cv2
from matplotlib import pyplot as plt
from fpdf import FPDF

### OBJECTIVE: print out daily facts
# web scraping for facts on fish
## bible verse
##

# place on pdf file and email it to myself

def generateGeneralPdf(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=name, ln=1, align="C")
    return pdf

def main():
    pdf = generateGeneralPdf("Daily Facts")


def getBibleVerse():


def getFishInfo():


def email():


main()
