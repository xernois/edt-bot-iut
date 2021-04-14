import flask, json
from flask import jsonify, request, render_template, redirect
from selenium import webdriver
from selenium.webdriver.common import keys

app = flask.Flask(__name__)
app.config["DEBUG"] = True

semaine_defaut = 1

#######################################
##                                   ##
##            Fonctions              ##
##                                   ##
#######################################
def fetch_groupe(data,group):
    try: 
        return data[list(data)[list(data).index(group)]]
    except ValueError:
        res = {}
        for key in (list(data)):
            if(key[:len(group)] == group):
                res[key] = data[key]
        return res if len(res) != 0 else "ce groupe n'existe pas"
#######################################
##                                   ##
##        listes des routes          ##
##                                   ##
#######################################
##route pour la page d'accueil
@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')
##route pour la page de doc
@app.route('/doc', methods=['GET'])
def doc_page():
    return render_template('doc.html')
##redirection vers / quand la route n'existe pas
@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')
#######################################
##                                   ##
##          routes pour A1           ##
##                                   ##
#######################################
@app.route('/api/edt/a1', methods=['GET'])
def edt_a1():
    try:
        with open('edt/A1_S'+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+'.json') as f:
            content = json.load(f)
    except IOError:
        return 'L\'edt de la semaine '+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+' n\'est pas disponible'
    if request.args.get('g') != None:
        return fetch_groupe(content,request.args.get('g').upper())
    return content
#######################################
##                                   ##
##          routes pour A2           ##
##                                   ##
#######################################
@app.route('/api/edt/a2', methods=['GET'])
def edt_a2():
    try:
        with open('edt/A2_S'+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+'.json') as f:
            content = json.load(f)
    except IOError:
        return 'L\'edt de la semaine '+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+' n\'est pas disponible'
    if request.args.get('g') != None:
        return fetch_groupe(content,request.args.get('g').upper())
    return content
#######################################
##                                   ##
##          routes pour A3           ##
##                                   ##
#######################################
@app.route('/api/edt/a3', methods=['GET'])
def edt_a3():
    try:
        with open('edt/A3_S'+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+'.json') as f:
            content = json.load(f)
    except IOError:
        return 'L\'edt de la semaine '+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+' n\'est pas disponible'
    if request.args.get('g') != None:
        return fetch_groupe(content,request.args.get('g').upper())
    return content











app.run()
