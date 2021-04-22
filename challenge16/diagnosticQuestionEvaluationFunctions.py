"""
   test progress in various fields
   log progress
"""
import os
import csv
import pandas as pd
import random
import time
from typing import NamedTuple
from playsound import playsound
from datetime import date
import re



class SubjectScore(NamedTuple):
    subject: str
    time: str
    correct: int
    total: int
    count: int




def askQuestions(subject: str, questions: int = 10) -> SubjectScore:
    """
      ask questions on given subject csv file
      respond with time taken and relavant data
    """

    dirname = os.path.dirname(__file__)
    audio = "audio/"
    data = "data/"
    missedQuestions = list()

    loadedQuestions = pd.read_csv(dirname + "/data/" + subject + ".csv" )
    correct = 0
    starttime = time.time()
    audioEnabled = True if 'audio' in loadedQuestions.columns else False
    optionsGiven = True if 'options' in loadedQuestions.columns else False
    #
    for x in range(questions):
        randomQuestionIndex = random.randint(0,len(loadedQuestions.index) - 1)

        # if exists, play audio
        if audioEnabled and loadedQuestions.loc[randomQuestionIndex]['audio'] != "FALSE":
            playsound(dirname + "/audio/"+ subject + "/" + loadedQuestions.loc[randomQuestionIndex]['audio'] + ".mp3")

        else:
            print(loadedQuestions.loc[randomQuestionIndex]['question'])

        answer = input()
        if compareAnswers(answer, loadedQuestions.loc[randomQuestionIndex]['answer']):
            correct += 1
        else:
            missedQuestions.append(loadedQuestions.loc[randomQuestionIndex]['answer'])

    endtime = time.time()
    time_elapsed = endtime - starttime
    minutes = round(time_elapsed // 60)
    seconds = round(time_elapsed % 60)
    time_string = str(minutes) + ":" + str(seconds)
    print(missedQuestions)
    return SubjectScore(subject, time_string, correct, questions, len(loadedQuestions.index))

def compareAnswers(given: str, answer: str) -> bool:
    given = re.sub("[?,!.]","",given)
    answer = re.sub("[?,!.]","", answer)
    if re.sub('[!.?]','',given).lower().strip() == re.sub('[!.?]','', answer).lower().strip():
        return True


    return False




def runDiagnostic(categories) -> str:


    for category in categories:
        log_file = os.path.dirname(__file__) + '/logging/scores/' + category + '.csv'
        all_data = pd.read_csv(log_file)
        df = pd.DataFrame(columns=all_data.columns)
        scoreData = askQuestions(category)
        df["time"] = pd.Series([scoreData.time])
        df["correct"] = pd.Series([scoreData.correct])
        df["total"] = pd.Series([scoreData.total])
        df["count"] = pd.Series([scoreData.count])


    today = date.today().strftime("%Y-%m-%d")
    df["date"] = pd.Series([today])
    df.to_csv(log_file, mode='a', header=False, index=False)
    return log_file

if __name__ == "__main__":
    print("not main file")
