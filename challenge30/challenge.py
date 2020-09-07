from fpdf import FPDF
import array
import numpy as np
import random
#

def generateMathsPdf(name, type, numbofquestions, skillLevel):
    # generate a quiz
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=name, ln=1, align="C")
    np_arr = generateAdditionQuestions(numbofquestions, skillLevel)
    counter = 0
    for x in range(numbofquestions):
        counter = counter + 1

        question =  str(np_arr[x, 0]) + " * " + str(np_arr[x, 1]) + " = "
        if (counter % 3 == 0):
            pdf.cell(30)
            pdf.cell(20, 10, txt=question, ln=1)
        else:
            pdf.cell(30)
            pdf.cell(20, 10, txt=question, ln=0)

    pdf.output(name +".pdf")

def generateAdditionQuestions (numbofquestions, skillLevel):
    difficulties = {
        1: 10,
        2: 20,
        3: 40,
        4: 70,
        5: 100
    }
    np_arr  = np.array([random.randint(11, difficulties.get(skillLevel,10)), random.randint(11, difficulties.get(skillLevel,10))])

    for x in range(numbofquestions):
        np_arr2 = np.array([random.randint(11, difficulties.get(skillLevel,10)), random.randint(11, difficulties.get(skillLevel,10))])
        np_arr = np.vstack((np_arr,np_arr2))
    return np_arr

generateMathsPdf("addition6", "choice", 42, 3);
