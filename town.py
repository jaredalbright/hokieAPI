import requests
from bs4 import BeautifulSoup as BS

website = 'https://www.blacksburg.gov'

def createBS():
    '''
    Creates the soup object from blacksburgs website
    '''
    page = requests.get(website).content
    soup = BS(page, "html.parser")
    return soup

def getHeadlines():
    '''
    Puts the headlines from Blacksburgs homepage into link form    
    '''
    soup = createBS()
    jsonDic = {}

    #section where headlines are held
    headLineSection = soup.find('section', {'id':'ColumnUserControl7'})

    headLines = []

    #iterates through all headlines on the front page
    for line in headLineSection.find_all('li'):
        newEntry = {}
        linkHolder = line.find_next('a')
        newEntry['Headline'] = linkHolder.text.strip()
        newEntry['Link'] = website + linkHolder['href']
        headLines.append(newEntry)

    jsonDic['Headlines From Blacksburg.gov'] = headLines

    return jsonDic

def getEvents():
    '''
    Puts the next events from Blacksburgs homepage into link form  

    To-Do = Add functionality for date and time  
    '''
    soup = createBS()
    jsonDic = {}

    #section where events are held
    eventSection = soup.find('section', {'id':'ColumnUserControl8'})

    events = []

    for line in eventSection.find_all('li'):
        newEntry = {}
        linkHolder = line.find_next('a')
        newEntry['Event'] = linkHolder.text.strip()
        newEntry['Link'] = website + linkHolder['href']
        events.append(newEntry)

    jsonDic['Headlines From Blacksburg.gov'] = events

    return jsonDic

def getWeather():
    '''
    Find Blackburg Weater
    To-Do
    '''
    return 0  