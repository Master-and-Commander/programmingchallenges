from fpdf import FPDF
import array
import numpy as np
import random
from numpy import *
# modified to allow for bigger numbers and more questions

def springMix(name, numbofquestions, skillLevel):
# produces math quiz with addition, subtraction, multiplication, and division
# ratio is 1 : 1 : 5 : 3
    pdf = generateGeneralPdf(name)
    np_arr = generateNumberPairs(numbofquestions, skillLevel)
    counter = 0
    for x in range(numbofquestions):
        counter = counter + 1

        question =  str(np_arr[x, 0]) + returnOperator(10, 10, 50, 30, x, numbofquestions) + str(np_arr[x, 1]) + " = "
        if (counter % 5 == 0):
            pdf.cell(20)
            pdf.cell(10, 5, txt=question, ln=1)
        else:
            pdf.cell(20)
            pdf.cell(10, 5, txt=question, ln=0)

    pdf.output(name +".pdf")


def returnOperator(additionstop, subtractionstop, multiplicationstop, divisionstop, current, total):
    # return a different operator based on the current spot
    # potential operators +, -, /, %
    # potential questions involving: factorial, square root, square (power)
    operands = {
        1: " + ",
        2: " - ",
        3: " * ",
        4: " / "
    }

    stops = {
        1: additionstop,
        2: additionstop + subtractionstop,
        3: additionstop + subtractionstop + multiplicationstop,
        4: 100
    }

    currentPercentage = current / total * 100
    operandtofetch = 4
    counter = 3

    while currentPercentage < stops.get(counter, -1):
        counter = counter - 1
        operandtofetch = operandtofetch - 1

    return operands.get(operandtofetch, " * ")

def generateGeneralPdf(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=name, ln=1, align="C")
    return pdf


def generateDifficulties(len):
    difficulties = {}
    for x in arange(len):
        difficulties[x] = x * 10
    return difficulties

def generateNumberPairs (numbofquestions, skillLevel):
    # the higher the difficulty the bigger the number
    difficulties = generateDifficulties(10)

    np_arr  = np.array([random.randint(11, difficulties.get(skillLevel,10)), random.randint(11, difficulties.get(skillLevel,10))])

    for x in range(numbofquestions):
        np_arr2 = np.array([random.randint(11, difficulties.get(skillLevel,10)), random.randint(11, difficulties.get(skillLevel,10))])
        np_arr = np.vstack((np_arr,np_arr2))
    return np_arr

springMix("test 6", 150, 9)
