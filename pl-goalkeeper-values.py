# import libraries
import urllib.request
from bs4 import BeautifulSoup
import requests
import lxml.html as lh
import pandas as pd

# specify the url
quote_page = urllib.request.Request('https://fantasy.premierleague.com/player-list/')

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('div', attrs={'class':'wisbb_fullPlayer'})

# convert html to string
soupStr = str(soup)

# only keep the goalkeepers section. remove everything else
startWord = 'Goalkeepers'
endWord = 'Defenders'
start_index = soupStr.find(startWord)
end_index = soupStr.find(endWord)

soupStr = soupStr[start_index:end_index]

# we have the goalkeeprs and other information that is not useful.
# need to clean house
startWord = '</thead>'
start_index = soupStr.find(startWord)

soupStr = soupStr[start_index+len(startWord):]

startWord = '</table>'
endWord = '</thead>'
start_index = soupStr.find(startWord)
end_index = soupStr.find(endWord)

soupStr = soupStr[:start_index] + soupStr[end_index:]

# save the cleaned up html to a text file called goalkeepers
file  = open('goalkeepers.txt', 'w')

file.write(soupStr)
file.close()

# extract the necessary information
fname = 'goalkeepers.txt'
# switch will be used to check if the line before the current one was <tr>
switch = 0
# store the goalkeeper names in strClean
strClean = ''

with open(fname) as f:
    content = f.readlines()
    for i in range(len(content)):
        if '<tr>' in content[i]:
            switch = 1
        elif switch == 1:
            strClean = strClean + content[i]
            switch = 0
        else:
            switch = 0

# this file will have all the pl goalkeeper names
file  = open('goalkeepersClean.txt', 'w')

file.write(strClean)
file.close()