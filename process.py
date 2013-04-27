import urllib2
import simplejson
import requests
import nltk
import re
from BeautifulSoup import BeautifulSoup


user_input = "london"
web_string = "http://content.guardianapis.com/search?q="+user_input+"&format=json"
req = urllib2.Request(web_string)
opener = urllib2.build_opener()
f = opener.open(req)
result = simplejson.load(f)
print result["response"]["status"]

ret_dict = []
count = 0
for article in result["response"]["results"]:
    entry = str(article["webUrl"])
    ret_dict.append(entry)

print ret_dict


#for each url...
url = 'http://www.guardian.co.uk/society/2013/apr/25/society-daily-email'
response = requests.get(url)
#parse html
soup = BeautifulSoup(response.text)
body_html = soup.findAll('div', attrs={'id':'article-body-blocks'})
#strip trags
body_text = nltk.clean_html(response.text)
#remove excess spaces
text = re.sub('\s+', ' ', body_text)
#limit to 8000 chars
text = [text[:8000]]
print text

