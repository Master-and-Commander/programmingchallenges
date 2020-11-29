import sys
import json
from datetime import date
from datetime import datetime
import copy
from fpdf import FPDF
import random


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
           craftQuiz(path, pathNumber,scope)







def craftQuiz(path, pathNumber, scope):
    questions = scope.get("questions")
    answers = {}
    correctNumber = 0
    for x in range( scope.get("questionCount")):
        print()
        questionNumber = random.randint(1,len(questions))
        print(scope.get("questions").get(str(questionNumber)).get("question"))
        answers[x] = input().strip()
        if answers[x] == scope.get("questions").get(str(questionNumber)).get("answer"):
            correctNumber = correctNumber + 1

        else:
            print("Answer actually was '" +  scope.get("questions").get(str(questionNumber)).get("answer") + "'")
            print("For more info check reference such and such")


    print("You received a " + str(correctNumber) + "/" + str(scope.get("questionCount")) )





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
