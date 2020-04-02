# 3.1 FUNKTIONEN
## 3.1.1 Funktionen definieren
def greeting():
    print("Hello World")

greeting()

## 3.1.2 Parameter in Funktionen
def greet(name):
    print("Hello "+name)

greet(name = "Simon")
greet("Simon")

## 3.1.1 Warum benutzt man Funktionen?
grades = [3.75, 2.0, 4.25, 3.75, 3.5, 4.0, 5.0, 1.0, 6.0, 5.25, 4.0, 5.25, 5.5, 3.0, 2.5, 1.0, 5.0, 3.5, 5.0, 3.75, 2.0, 2.75, 4.25, 5.0, 1.5, 6.0, 5.75, 1.5, 6.0, 2.25, 5.75, 5.0, 4.5, 2.0, 2.5]

summe = 0 # summe = grades[0] + grades[1] + grades[2] + ... + grades[3]
for grade in grades:
    summe += grade # summe = summe + grade
avg = summe / len(grades)
print("avg: ", avg)

def average(arr):
    summe = 0
    for element in arr:
        summe += element
    avg = summe / len(arr)
    return avg

grades = [3.75, 2.0, 4.25, 3.75, 3.5, 4.0, 5.0, 1.0, 6.0, 5.25, 4.0, 5.25, 5.5, 3.0, 2.5, 1.0, 5.0, 3.5, 5.0, 3.75, 2.0, 2.75, 4.25, 5.0, 1.5, 6.0, 5.75, 1.5, 6.0, 2.25, 5.75, 5.0, 4.5, 2.0, 2.5]
print("avg: ", average(grades))


# ---------------------------------- #

# 3.2 MODULE

## 3.2.1 Das Import Statement
## Import
import datetime
print(datetime.datetime.today())

## Relativ
from datetime import datetime
print(datetime.today())

from datetime import datetime as dt
print(dt.today())


## 3.2.2 Die Python Standard Library
## math modul
import math as m
root = m.sqrt(16)
print(root) # > 4

from math import sqrt
root = sqrt(16^2)
print(root) # > 16

## time modul
import time
timerSeconds = 20
i = 0
# while i < 20:
#     i += 1
#     print("waiting")
#     time.sleep(1)
# print("Kuchen ist fertig")

## 3.2.2 PIP Installer
## pip install bs4

## 3.2.3 Einstieg in das Webscraping
## Requests
import requests
response = requests.get("http://quotes.toscrape.com/")
print(response.status_code) #> 200 (Alles OK)
# print(response.content) #> HTML

## Parsing HTML
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
title = soup.title
print(title) # > <title>Quotes to Scrape</title>
print(title.text) # > Quotes to Scrape
quotes = soup.find_all('div', {'class': 'quote'})
for quote in quotes:
    text = quote.find('span', {'itemprop':'text'}).text
    author = quote.find('small', {'class':'author'}).text
    # print(author, '\n', text, '\n\n')
