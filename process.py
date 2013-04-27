import urllib2
import simplejson


req = urllib2.Request("http://content.guardianapis.com/search?q=london&format=json")
opener = urllib2.build_opener()
f = opener.open(req)
result = simplejson.load(f)
print result["response"]["status"]