# import libraries
import urllib.request
from bs4 import BeautifulSoup
import requests
import lxml.html as lh
import pandas as pd

# specify the url
quote_page = urllib.request.Request('https://fbref.com/en/comps/9/keepers/Premier-League-Stats')

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('div', attrs={'class':'wisbb_fullPlayer'})

#print(soup)

# convert html to string
soupStr = str(soup)

# only keep the goalkeepers section. remove everything else
startWord = 'div_stats_keepers_players'
start_index = soupStr.find(startWord)

soupStr = soupStr[start_index:]

# only keep the goalkeepers section. remove everything else
startWord = '<tbody>'
endWord = '</tbody>'
start_index = soupStr.find(startWord)
end_index = soupStr.find(endWord)

soupStr = soupStr[start_index:end_index]

#print(soupStr)

# this file will have all the pl goalkeeper names
file  = open('goalkeeperStats.txt', 'w')

file.write(soupStr)
file.close()