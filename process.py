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
consumerKey = "c18c1d22-e189-4a92-b34d-dc1155964446"
consumerSecret = "e7faedd6-70c2-487f-a43a-ad89aebf04e9"
initialTexts = [
    "Lisa - there's 2 Skinny cow coupons available $5 skinny cow ice cream coupons on special k boxes and Printable FPC from facebook - a teeny tiny cup of ice cream. I printed off 2 (1 from my account and 1 from dh's). I couldn't find them instore and i'm not going to walmart before the 19th. Oh well sounds like i'm not missing much ...lol",
    "In Lake Louise - a guided walk for the family with Great Divide Nature Tours  rent a canoe on Lake Louise or Moraine Lake  go for a hike to the Lake Agnes Tea House. In between Lake Louise and Banff - visit Marble Canyon or Johnson Canyon or both for family friendly short walks. In Banff  a picnic at Johnson Lake  rent a boat at Lake Minnewanka  hike up Tunnel Mountain  walk to the Bow Falls and the Fairmont Banff Springs Hotel  visit the Banff Park Museum. The \"must-do\" in Banff is a visit to the Banff Gondola and some time spent on Banff Avenue - think candy shops and ice cream.",
    "On this day in 1786 - In New York City  commercial ice cream was manufactured for the first time."
]


def onRequest(sender, result):
    print("\n", "REQUEST: ", result)


def onResponse(sender, result):
    print("\n", "RESPONSE: ", result)


def onError(sender, result):
    print("\n", "ERROR: ", result)


def onDocsAutoResponse(sender, result):
    print("\n", "AUTORESPONSE: ", len(result), result)


def onCollsAutoResponse(sender, result):
    print("\n", "AUTORESPONSE: ", len(result), result)

# Creates JSON serializer instance
serializer = semantria.JsonSerializer()
# Initializes new session with the serializer object and the keys.
session = semantria.Session(consumerKey, consumerSecret, serializer, use_compression=True)

session.Error += onError

for text in initialTexts:
    # Creates a sample document which need to be processed on Semantria
    # Unique document ID
    # Source text which need to be processed
    doc = {"id": str(uuid.uuid1()).replace("-", ""), "text": text}
    # Queues document for processing on Semantria service
    status = session.queueDocument(doc)
    # Check status from Semantria service
    if status == 202:
        print("\"", doc["id"], "\" document queued successfully.", "\r\n")


length = len(initialTexts)
results = []


while len(results) < length:
    print("Retrieving your processed results...", "\r\n")
    # As Semantria isn't real-time solution you need to wait some time before getting of the processed results
    # In real application here can be implemented two separate jobs, one for queuing of source data
    # another one for retreiving
    # Wait ten seconds while Semantria process queued document
    time.sleep(2)	
    # Requests processed results from Semantria service
    status = session.getProcessedDocuments()
    # Check status from Semantria service
    if isinstance(status, list):
        for object_ in status:
            results.append(object_)



for data in results:
    # Printing of document sentiment score
    print("Document ", data["id"], " Sentiment score: ", data["sentiment_score"], "\r\n")

    # Printing of document themes
    if "themes" in data:
        print("Document themes:", "\r\n")
        for theme in data["themes"]:
            print("	", theme["title"], " (sentiment: ", theme["sentiment_score"], ")", "\r\n")

    # Printing of document entities
    if "entities" in data:
        print("Entities:", "\r\n")
        for entity in data["entities"]:
            print("\t",
                  entity["title"], " : ", entity["entity_type"],
                  " (sentiment: ", entity["sentiment_score"], ")", "\r\n"
            )
































