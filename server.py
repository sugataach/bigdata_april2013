from flask import Flask, render_template, request
import json
import time

app = Flask(__name__)


@app.route('/')
def index():
    return open('templates/index.html').read()

@app.route('/search')
def search():
    place = request.args.get('place')
    time.sleep(5)
    return json.dumps({'name': place})

if __name__ == '__main__':
    app.run()