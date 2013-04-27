from flask import Flask, render_template, request, Response
import json
import time

app = Flask(__name__)


@app.route('/')
def index():
    return open('templates/index.html').read()

@app.route('/search')
def search():
    place = request.args.get('place')
    return json.dumps({'name': place})

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
    app.run()