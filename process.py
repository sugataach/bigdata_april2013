from __future__ import print_function
from BeautifulSoup import BeautifulSoup
import urllib2
import simplejson
import requests
import nltk
import re
import semantria
import uuid
import time



def getTextByUrl(url):
	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page)
	soup.prettify()
	body = soup.find("div",{"id":"article-body-blocks"})

	bodytext = ""
	for p in body.findAll(text=True):
		bodytext += str(p)
	return bodytext


#GUARDIAN API - USER INPUT TO URL
user_input = "london"
web_string = "http://content.guardianapis.com/search?q="+user_input+"&format=json"
req = urllib2.Request(web_string)
opener = urllib2.build_opener()
f = opener.open(req)
result = simplejson.load(f)
print (result["response"]["status"])

ret_dict = []
count = 0
for article in result["response"]["results"]:
    entry = str(article["webUrl"])
    ret_dict.append(entry)

print (ret_dict)

#BEAUTIFULSOUP - URL TO TEXT
url = "http://www.guardian.co.uk/politics/2013/apr/27/ed-miliband-plans-autumn-reshuffle"
print (getTextByUrl(url))

#SEMANTRIA



































