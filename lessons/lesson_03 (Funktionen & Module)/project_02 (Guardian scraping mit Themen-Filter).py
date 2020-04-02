import requests
from bs4 import BeautifulSoup

# find in text 01
def findInText(text, wordList):
    casefoldText = text.casefold()
    splitText = casefoldText.split(" ")
    for word in splitText:
        for searchTerm in wordList:
            if word == searchTerm:
                return True
    return False
# find in text 02 --> Will not find 'corona' in 'coronavirus' or 'covid' in 'covid-19'
def findInText2(text, wordList):
    for searchTerm in wordList:
        if searchTerm in text:
            return True
    return False

# WordList
wordList = ["covid","corona","virus","pandemic"]

# Request web-Content
response = requests.get("https://www.theguardian.com/world")
html = response.content

# parse content
soup = BeautifulSoup(html, "html.parser")

# find all article elements
items = soup.find_all('div', {'class': 'fc-item__content'})

# iterate over items and get headline, kicker, url
for item in items:
    kicker = item.find('span',{'class': 'fc-item__kicker'})
    if kicker != None:
        kicker = kicker.text
    else:
        kicker = ""
    headline = item.find('span',{'class': 'u-faux-block-link__cta fc-item__headline'}).text
    link = item.find(href=True)['href']
    if findInText(kicker, wordList) or findInText(headline, wordList):
        print(kicker, headline.lstrip().rstrip(),"\n", link, "\n\n")
    
    