from PyDictionary import PyDictionary
import array
import numpy as np
import random



# would be useful to check if entry is a word or a number
# if a word get type (ex. noun)
# if a number perhaps prefix question with "How many... ?"

# patterns:
## x is y
### Q: why is x = y?
### Q: True/False. x = z
### Q: x is ____

# chaining question usage
# if pattern is
## x is y
## x [verb] z
## x [verb] a
### Q: What y [verb] z ?
### Q: What does x [verb]? options [a, z, b, a and z]

# usage examples
## scripture or text memorization: fill in the blank
## networking / technical text



# sample text


# what I can do
## set a trigger for pattern "the x is/are y" (begin at 'the', stop at [',', '.'])

## check for repeating nouns
### this tells you what to ask questions about

## check for verbs associated with the nouns
### this helps you form questions


def organizeConclusions(text, dictionary):
    # divide into sentences
    organizedConclusions = {}

    sentences = text.split('.')
    for x in sentences:
        # find the subject

        subject = ""
        verb = ""
        factlist = []
        words = x.split()
        nounfound = False
        verbfound = False

        for y in words:
            # find first noun

            if nounfound:
                # find next verb
                if verbfound:
                    factlist.append(y)
                    # time to add to statement
                else:
                    meaning = dictionary.meaning(y)
                    if meaning != None:
                        if "Verb" in meaning:
                            verbfound = True
                            verb = y
            else:
                meaning = dictionary.meaning(y)
                if meaning != None:
                    if "Noun" in meaning:
                        nounfound = True
                        subject = y
        # add to conclusions
        latterstatement = {
            verb : ' '.join(factlist)
        }
        firststatement = {
            subject : latterstatement
        }
        if subject in organizedConclusions:
            organizedConclusions[subject][verb] = ' '.join(factlist)
        else:
            organizedConclusions[subject] = latterstatement
    return organizedConclusions

    # first divide into sentences
    # for each sentence
    # find first noun
    # find closest verb
    # find 'fact'
    # add noun, verb, fact to set, if noun existing and if verb existing, append to set

def returnQuestions(text, numbofquestions, dictionary):
    # number questions (question, answer, options)
    np_questions =  np.zeros((numbofquestions, 3), dtype='<U64')
    #print(np_questions)
    conclusions = organizeConclusions(text, dictionary)
    questioncounter = 0
    for x in conclusions:
        # key for the key
        thekey = conclusions[x].keys();
        np_questions[questioncounter] = makeQuestion(x, conclusions[x], random.randint(1, 3)  )
        questioncounter = questioncounter + 1


    print("these are my conclusions")
    print(np_questions)

def makeQuestion(subject, statement, mode):
    # question types
    # What verb1 fact1 and verb2 fact2?
    # does noun verb1 fact1 or fact2?
    # What does noun do to fact1
    # check if subject

    keys = list(statement)
    print("this is the statement")
    print(keys)
    multiplePossible = False
    length = len(keys)
    randomint = random.randint(0, length-1)
    second = (randomint + 1) % max(length, 1)
    questiondata = np.zeros(3, dtype='<U64')
    answer = "hello"

    if length > 1:
         multiplePossible = True


    print("random int chosen")
    print(randomint)

    if mode == 1:
        question = "What thing " + keys[randomint] + " " + statement.get(keys[randomint])
        answer = subject
    elif mode == 2 and multiplePossible:
        numberToUseFirst = second
        numberToUseSecond = randomint
        if randomint % 2 == 0:
            numberToUseFirst=randomint
            numberToUseSecond=second
        question = "Does " + subject + " " + keys[randomint] + " " + statement.get(keys[numberToUseFirst], "hay") + " or " + statement.get(keys[numberToUseSecond], "hay") + "?"
        answer = statement.get(keys[randomint], "eat hay")
    elif mode == 3:
        question = "What does " + subject + " do to " + statement.get(keys[randomint], "hay")
        answer = keys[randomint]
    else:
        question = "What thing " + keys[randomint] + " " + statement.get(keys[randomint])
        answer = subject

    questiondata[0] = question
    questiondata[1] = answer

        # pattern What key1 fact1 and key2 fact2


    return questiondata


dictionary=PyDictionary()
returnQuestions("I am a tall fellow. Interestingly, donkeys graciously eat cookies. donkeys drink water. Broken cisterns yield no water. Programming breaks laziness. Programming soothes the soul. small cisterns hold some water.", 10, dictionary)


# returnQuestions -> organizeConclusions
# returnQuestions -> makeQuestion

# "Elephant, (family Elephantidae), largest living land animal, characterized by its long trunk (elongated upper lip and nose), columnar legs, and huge head with temporal glands and wide, flat ears. Elephants are grayish to brown in colour, and their body hair is sparse and coarse. They are found most often in savannas, grasslands, and forests but occupy a wide range of habitats, including deserts, swamps, and highlands in tropical and subtropical regions of Africa and Asia."
