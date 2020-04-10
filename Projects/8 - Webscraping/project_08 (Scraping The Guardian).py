"""Scraping The Guardian
Example for Webscraping

Author: Noah Kamara
"""

import requests
from bs4 import BeautifulSoup

class Filter:
    """Provides a Filter for lists of words
    
    Returns:
        boolean -- Whether or not the string passedd the filter
    """    
    def __init__(self, filterList, isWhiteList = True):
        """
        Arguments:
            filterList {list[str]} -- List of words to look out for when filtering
        Keyword Arguments:
            isWhiteList {bool} -- Whether the Filter should act as whitelist or blacklist (False) (default: {True})
        """        
        self.filterList = filterList
        self.isWhiteList = isWhiteList
        
    def filter(self, text):
        """Filter the text and return true if it passes
        Arguments:
            text {str} -- string to be filtered
        Returns:
            bool -- Whether the string passed the Filter
        """        
        wasFiltered = False
        text = text.casefold()
        # for word in filterList
        for filterWord in self.filterList:
            if filterWord in text: # if word in string return true
                wasFiltered = True
                continue
        
        # Switch success if mode is Blacklist
        if self.isWhiteList:
            return wasFiltered
       	else:
            return not wasFiltered
        

# WordList (Words to be filtered)
wordList = ["covid","corona","virus","pandemic"]

whiteList = Filter(wordList) # Use wordList as whitelist
blackList = Filter(wordList, isWhiteList=False) # and as blacklist

# Request Response from Server
response = requests.get("https://www.theguardian.com/world")
html = response.content

# parse HTML
soup = BeautifulSoup(html, "html.parser")

# find all elements (Headlines)
items = soup.find_all('div', {'class': 'fc-item__content'})

# iterate over items and get headline, kicker, url
for item in items:
    kicker = item.find('span',{'class': 'fc-item__kicker'})
    # if kicker was found -> give text ELSE: -> empty String
    if kicker != None:
        kicker = kicker.text
    else:
        kicker = ""

    headline = item.find('span',{'class': 'u-faux-block-link__cta fc-item__headline'}).text.lstrip().rstrip()
    link = item.find(href=True)['href']

    # As Whitelist
    if whiteList.filter(kicker) or whiteList.filter(headline):
        print(kicker, headline,"\n", link, "\n\n")
    
    # As Blacklist
    if blackList.filter(kicker) or blackList.filter(headline):
        print(kicker, headline,"\n", link, "\n\n")
    
    