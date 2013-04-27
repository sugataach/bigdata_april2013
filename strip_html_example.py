#pre process an article for sentiment analysis


import requests
import nltk
import re
from BeautifulSoup import BeautifulSoup

#fetch
response = requests.get('http://www.guardian.co.uk/society/2013/apr/25/society-daily-email')

#parse html
soup = BeautifulSoup(response.text)
body_html = soup.findAll('div', attrs={'id':'article-body-blocks'})
#strip trags
body_text = nltk.clean_html(response.text)
#remove excess spaces
text = re.sub('\s+', ' ', body_text)
#limit to 8000 chars
text = [text[:8000]]