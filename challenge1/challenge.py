from PyDictionary import PyDictionary
import array
import numpy as np

dictionary=PyDictionary()

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
            print("subject " + subject + " not found in organizedConclusions" )
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
    np_questions[0,0] = "What name is a tall fellow?"
    np_questions[0,1] = "John"
    #print(np_questions)
    conclusions = organizeConclusions(text, dictionary)
    print("these are my conclusions")
    print(conclusions)




returnQuestions("I am a tall fellow. Interestingly, donkeys graciously eat cookies. donkeys drink water", 2, dictionary)
