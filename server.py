from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return open('templates/index.html').read()

@app.route('/search')
def search():
    place = request.args.get('place')
    return json.dumps({'name': place})

if __name__ == '__main__':
    app.run()