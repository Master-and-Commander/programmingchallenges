from PyDictionary import PyDictionary
import array
import numpy as np

dictionary=PyDictionary()

# would be useful to check if entry is a word or a number
# if a word get type (ex. noun)
# if a number perhaps prefix question with "How many... ?"

def returnQuestions(text, numbofquestions):
    # number questions (question, answer, options)
    np_questions =  np.zeros((numbofquestions, 3), dtype='<U5')
    print(np_questions)



def returnTypeOfWord(word):
    return "Noun"

returnQuestions("hello, my name is John. I am a tall fellow", 2)
