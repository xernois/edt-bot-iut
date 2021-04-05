import flask, json
from flask import jsonify, request
from selenium import webdriver
from selenium.webdriver.common import keys

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<u><h1>API EDT IUT</h1></u>
    <ul>
        <li>
            <h3>liste des requetes faisables</h3>
            <ul>
            <li>/api/edt/a1       <i>(retourne le json de l'edt des a1)</i></li>
            <li>/api/edt/a2       <i>(retourne le json de l'edt des a1)</i></li>
            <li>/api/edt/a3       <i>(retourne le json de l'edt des a1)</i></li>
            </ul>
        </li>
        <li>
            <h3>liste des options</h3>
            <ul>
            <li>?s=X       <i>(retourne l'edt de la semaine X)</i></li>
            </ul>
        </li>
    <ul>
    '''

    
@app.route('/api/edt/a1', methods=['GET'])
def edt_a1():
    if request.args.get('s') == None:
        semaine = 1
    else:
        semaine = request.args.get('s')
    try:
        with open('edt/A1_S'+str(semaine)+'.json') as f:
            content = json.load(f)
    except IOError:
        return 'L\'edt de la semaine '+str(semaine)+' n\'est pas disponible'
    return content

@app.route('/api/edt/a2', methods=['GET'])
def edt_a2():
    if request.args.get('s') == None:
        semaine = 1
    else:
        semaine = request.args.get('s')
    try:
        with open('edt/A2_S'+str(semaine)+'.json') as f:
            content = json.load(f)
    except IOError:
        return 'L\'edt de la semaine '+str(semaine)+' n\'est pas disponible'
    return content

@app.route('/api/edt/a3', methods=['GET'])
def edt_a3():
    if request.args.get('s') == None:
        semaine = 1
    else:
        semaine = request.args.get('s')
    try:
        with open('edt/A3_S'+str(semaine)+'.json') as f:
            content = json.load(f)
    except IOError:
        return 'L\'edt de la semaine '+str(semaine)+' n\'est pas disponible'
    return content












app.run()
