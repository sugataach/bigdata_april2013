import urllib2
import simplejson

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