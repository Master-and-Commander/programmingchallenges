import re
import random
import copy
from PIL import Image
import pandas as pd
import os
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO
from io import BytesIO
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Image
from dataclasses import dataclass
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth

"""
  command to run
py compiledocuments.py [structure] [subject]


filestructures (name of structure is passed to find file here)
     {entails the ordering of a new file which may include many templates}
     {fields: templatename repeatable
subjecttypedata
     > Persons
      sampleperson
        data.csv
        {fields - templatename templatefield content}
     > Studies
     > etc.
the name of a template is repeated in drawings and fields and both are used to
correctly render subject type data
templatedrawings
     {entails the lines and figures drawn on the template}
     {fields: drawtype - slot1 - slot2 - slot3 - slot4 - slot5 - code}
templatefields
     {entails fields on the documents}
     {fields: templatefield - font - size

Given structure
    and subjecttypedata

structuredf = pd.read_csv(structure)
# now you have the required templates and the order of them
subjecttypdatadf = pd.read_csv(subjecttypedata)
# now you have the data to enter into the templates
canvas = Canvas("document name")
for structuredfrow in structuredf.index:
    # each row is a reference to a template
    canvas = renderfromtemplate(structuredf.loc[index]["templatename"], canvas)
    # here we get data relevant to the template file on hand
    relevantsection = subjecttypedatadf[subjecttypedatadf[templatename] == structuredf.loc[index]["templatename"] ]
    canvas = populateTemplate(canvas, relevantsection)
    canvas.showPage()





py compiledocuments.py [structure] [subject]
"""
def drawTable(canvas, xs, ys, columns, rows, labels):
    # x1+x2, y1+y2, columns, rows, labels

    # format could be
    # number of rows, []-[]-[]
    xlist = xs.split('+')
    ylist = ys.split('+')
    xspot = 0
    yspot = 0
    space = 5
    givenlabels = labels.split('+')
    canvas.setFont("Times-Roman", 9)
    for label in givenlabels:
        print(label)
        canvas.drawString(xlist[xspot] + space, ylist[yspot] + space, label)



    return canvas
def renderfromtemplate(templatename, canvas):
    templatedf = pd.read_csv(os.path.dirname(__file__) + "/templatedrawings/" + templatename +  ".csv")

    if len(templatedf) > 0:
        for drawing in templatedf.index:
            slots = templatedf.loc[drawing].to_dict()
            datalist = list()
            for x in range(1,6):
                datalist.append(slots["slot" + str(x)])
            instructionsdict = {
               "rect" : (canvas.rect, 4, dict({"fill":1}), False),
               "string" : (canvas.drawString, 3, dict({}), True),
               "table": (drawTable,5, dict({}), False)

            }
            action, argsused, extra, textUsed = instructionsdict[slots["drawtype"]]
            if(textUsed):
                canvas.setFont(slots["slot4"], slots["slot5"])

            if (slots["drawtype"] == "table"):
                canvas = drawTable(canvas, *datalist[:argsused])
            action(*datalist[:argsused], **extra)

    return canvas

def populateTemplate(canvas, relevantsection, templatename):
    templatedf = pd.read_csv(os.path.dirname(__file__) + "/templatefields/" + templatename +  ".csv")
    for fieldindex in relevantsection.index:
        fieldsrenderingdata = templatedf[templatedf["templatefield"] == relevantsection.loc[fieldindex]['templatefield'] ]
        #091293
        if len(fieldsrenderingdata) > 0:
            fieldsrenderingdata = fieldsrenderingdata.iloc[0]

            canvas.setFont(fieldsrenderingdata["font"], fieldsrenderingdata["size"])
            if(fieldsrenderingdata["startingfrom"] != "None"):
                # get x from adjusted width
                relevantdatarow = templatedf[templatedf["templatefield"] == fieldsrenderingdata["startingfrom"] ].iloc[0]

                entrydata = relevantsection[relevantsection["templatefield"] == fieldsrenderingdata["startingfrom"]].iloc[0]

                workingwidth = relevantdatarow["x"] + stringWidth( entrydata['content'] + " ", relevantdatarow["font"], relevantdatarow["size"])
                canvas.drawString(workingwidth, fieldsrenderingdata['y'], relevantsection.loc[fieldindex]['content'])
            else:
                canvas.drawString(fieldsrenderingdata["x"], fieldsrenderingdata['y'], relevantsection.loc[fieldindex]['content'])

    return canvas

def main(structurefile, datafile, givenname):

    dirname = os.path.dirname(__file__)
    structuredf = pd.read_csv(dirname + "/filestructures/" + structurefile)
    subjecttypedatadf = pd.read_csv(dirname + "/subjecttypedata/" + datafile)
    canvas = Canvas(givenname + ".pdf")

    for structuredfrow in structuredf.index:
        canvas = renderfromtemplate(templatename:=structuredf.loc[structuredfrow]["templatename"], canvas)
        relevantsection = subjecttypedatadf[subjecttypedatadf["templatename"] == templatename]
        canvas = populateTemplate(canvas, relevantsection, templatename)
        canvas.showPage()
    canvas.save()

main("/profile.csv", "/persons/doe/data.csv" , "profile")
