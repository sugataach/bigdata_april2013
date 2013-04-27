import urllib2
import simplejson
from BeautifulSoup import BeautifulSoup

req = urllib2.Request("http://content.guardianapis.com/search?q=brighton&format=json")
opener = urllib2.build_opener()
f = opener.open(req)
result = simplejson.load(f)
url = result["response"]["results"][0]["webUrl"]
print url

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)
soup.prettify()
body = soup.find("div",{"id":"article-body-blocks"})
print body
print " -- -- --- -"

bodytext = ""
for p in body.findAll(text=True):
	bodytext += str(p)

print bodytext

#print bodytext