from flask import Flask, render_template, request, Response
import json
import time
import process

app = Flask(__name__)


@app.route('/')
def index():
    return open('templates/index.html').read()

@app.route('/search')
def search():
    place = request.args.get('place')
    data = process.getUrlFromInput(place)
    #data = {0: ['http://www.guardian.co.uk/football/2013/apr/27/saturday-sundae-barnet-old-boy', 'Football', 'football', [u'neutral', u'european-wide guarantee']], 1: ['http://www.guardian.co.uk/politics/2013/apr/27/ed-miliband-plans-autumn-reshuffle', 'Politics', 'politics', [u'neutral', u'business volumes']], 2: ['http://www.guardian.co.uk/football/2013/apr/27/wolverhampton-wanderers-burnley-championship', 'Football', 'football', [u'negative']], 3: ['http://www.guardian.co.uk/football/football-league-blog/2013/apr/27/football-league-blog', 'Football', 'football', [u'negative', u'failing plan']], 4: ['http://www.guardian.co.uk/lifeandstyle/2013/apr/27/guardian-weekend-magazine-readers-letters', 'Life and style', 'lifeandstyle', [u'negative', u'including manufacturing tariffs']]}
    return json.dumps(data)

#just an example route to show you how we can read from other files
import example
@app.route('/christmas')
def christmas():
    ret = json.dumps({'christmas':example.is_it_christmas()})
    resp = Response(response=ret,
                    status=200,
                    mimetype="application/json")
    return resp


if __name__ == '__main__':
    app.run(debug=True)