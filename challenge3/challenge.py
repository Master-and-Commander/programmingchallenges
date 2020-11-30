import sys
import json
from datetime import date
from datetime import datetime
import copy
from fpdf import FPDF
import random
import requests
import urllib.parse
import re
# perhaps use this as a basic way to remind yourself of stuff you have learned

def main():

    today = date.today()
    d2 = today.strftime("%d/%m/%Y")
    with open("capital.json", "r") as openfile:
        jsonData = json.load(openfile)


    path =  {}
    pathNumber = 1
    scope = jsonData
    stopCondition = 0



    while (stopCondition == 0):
       userChoices = {}
       number = 1
       for item in scope.keys():
           userChoices[number] = item
           number = number + 1
       path[pathNumber] = choicesAndResponse(userChoices, "Select:")
       scope = scope.get(path[pathNumber])
       pathNumber = pathNumber + 1
       if "questions" in scope.keys():
           stopCondition = 1
           print("Starting Quiz")
           craftQuiz(path, pathNumber, scope, jsonData.get("keys"))







def craftQuiz(path, pathNumber, scope, keys):
    questions = scope.get("questions")
    answers = {}
    correctNumber = 0
    for x in range( scope.get("questionCount")):
        print()

        questionNumber = random.randint(1,len(questions))
        questionType = questions.get(str(questionNumber)).get("type")
        if questionType == "standard":
            print(questions.get(str(questionNumber)).get("question"))
            answers[x] = input().strip()
            if answers[x] == questions.get(str(questionNumber)).get("answer"):
                correctNumber = correctNumber + 1
            else:
                print("Answer actually was '" +  questions.get(str(questionNumber)).get("answer") + "'")
                print("For more info check reference such and such")
        elif questionType == "memorization":
            questionNumber = random.randint(scope.get("startRange"),scope.get("endRange"))
            print("This is a Memorization type question")
            verseNumber = random.randint(1,int(questions.get(str(questionNumber)).get("question")))
            baseUrlToUse = str(scope.get("baseurl")) + str(questionNumber) + ":" + str(verseNumber)
            token = "Token " + keys.get("esv")
            headers = {"Authorization": token }
            bibleresponse = requests.get(baseUrlToUse, headers=headers)
            biblejson = bibleresponse.json()
            bibledata = str(biblejson.get("passages"))

            # remove \n's and [] and numbers
            bibledata = removeBibleExtra(bibledata)

            # place these words in an array
            biblewords = bibledata.split()

            numberForRandomUse = 7

            stringBuild = ""
            correctanswerStrings = {}
            answerNumber = 0

            for word in range(2, len(biblewords)):
                randomNumber = random.randint(1,10)
                if randomNumber > numberForRandomUse:
                    stringBuild = stringBuild + " ____ "
                    correctanswerStrings[answerNumber] = biblewords[word]
                    answerNumber = answerNumber + 1

                else:
                    stringBuild = stringBuild + " " +  biblewords[word] + " "


            stringBuild = stringBuild.strip()
            print(biblewords[0] + " " + biblewords[1])
            print(stringBuild)

            doingWellEnough = 1
            answers[x] = input().strip()
            answerStrings = answers[x].split()
            if len(answerStrings) == len(correctanswerStrings):
                for word in range(len(correctanswerStrings)):
                    if removeSpecialCharacters(answerStrings[word]) != removeSpecialCharacters(correctanswerStrings[word]):
                        print("'" + answerStrings[word] + "' should be '" + correctanswerStrings[word] + "'")
                        doingWellEnough = 0
            else:
                doingWellEnough = 0
                print("You did not enter the correct number of arguments.")
                print("Here is what you missed: ")
                print(correctanswerStrings)
            if doingWellEnough == 1:
                correctNumber = correctNumber + 1







    print("You received a " + str(correctNumber) + "/" + str(scope.get("questionCount")) )


def removeSpecialCharacters(text):
    text = re.sub("[^A-Za-z]","",text)
    return text


def removeBibleExtra(bibledata):
    bibledata = re.sub("Footnotes.*", "", bibledata)
    bibledata = re.sub("\\\\n\\\\n(\D*?)\\\\n\\\\n","",bibledata)
    bibledata = re.sub("\[\d+\]|\\\\n|\(ESV\)|\(\d\)|\['|'\]", "", bibledata)
    bibledata = re.sub("\s+", " ", bibledata)
    bibledata = bibledata.strip()
    return bibledata

def choicesAndResponse(userChoices, prompt):
    print(prompt)
    for key in userChoices:
        print(str(key) + ":  " + userChoices[key] )

    response = input()
    if int(response) in userChoices:
        print()
        response = userChoices[int(response)]
    else:
        print()
        response = userChoices[1]
    return response




main()
