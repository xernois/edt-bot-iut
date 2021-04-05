import flask, json
from flask import jsonify, request
from selenium import webdriver
from selenium.webdriver.common import keys

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>requete invalide</h1>
    <h3>liste des requetes faisables</h3>
    <ul>
    <li>/api/edt/a1       <i>(retourne le json de l'edt des a1)</i></li>
    </ul>
    '''

@app.route('/api/edt/a1', methods=['GET'])
def edt_a1():
    with open('a1.json') as f:
        content = json.load(f)
    return content

app.run()
