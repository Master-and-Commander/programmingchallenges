import scrapy
from fpdf import FPDF
import numpy as np
import random
import wikipediaapi
from bs4 import BeautifulSoup
from googlesearch import search

# will come back to this to improve

class Quiz():
    questionCount = 10
    subjectArea = "history"
    ## information sources
    # wikepedia for simplicity
    start_urls = ['https://www.wikipedia.org/']
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    np_arr = [questionCount, 2];


    def __init__(self):
        for j in search(queryGenerator(), tld="co.in", num=questionCount, stop=10, pause=2)

        return 5
    def siteScraper():
        return 5
    def questionGenerator():
        return 5
    def queryGenerator():
        return "history general patton"


if __name__ == "__main__":
    app = Quiz()






# prompt user for subject area
## i.e. Science, Math, History, Geology, ...

## prompt user for specific issue

# prompt user for question count

# scrape relevant sites
# generate questions based on that content

# output pdf with that amount of questions
# csv file with questions and answers and section where question was taken from
