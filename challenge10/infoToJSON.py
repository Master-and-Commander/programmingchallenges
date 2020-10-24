# import packages to fetch distinguishing features
import numpy as np
import cv2
from matplotlib import pyplot as plt
from fpdf import FPDF
import requests
import urllib.parse
from bs4 import BeautifulSoup
import json
import random



def textToJSON(text):
    #Format: '{"1":{"german":"Und Ich werde mit ihm gehen", "english":"And I will go with him"}, "2":{"german":"Und Ich werde mit ihm gehen", "english":"And I will go with him"}}'
    jSONString = '{'

    jSONString = jSONString + '}'

def printStuff():
    jSONString = '{'
    for x in range(1001):
        jSONString = jSONString + '"' + str(x) + '": {"german":"", "english":""}, '
    jSONString = jSONString + '}'
    print(jSONString)

def splitByPeriods(text):
    array = text.split('.')
    for x in array:
        print(x)

text = input("Input text: ")
splitByPeriods(str(text))
