import flask, json
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from flask import jsonify, request, render_template, redirect, send_file
from selenium import webdriver
from selenium.webdriver.common import keys

app = flask.Flask(__name__)

semaine_defaut = 1

#######################################
##                                   ##
##            Fonctions              ##
##                                   ##
#######################################
def fetch_groupe(data,group):
    try: 
        return json.dumps(data[list(data)[list(data).index(group.upper())]])
    except ValueError:
        res = {}
        for key in (list(data)):
            if(key[:len(group)] == group.upper()):
                res[key] = data[key]
        return json.dumps(res) if len(res) != 0 else jsonify(code=401,message="Groupe non disponible")

def fetch_modules(data, module):
    res = {}
    for key in (list(data)):
        for key2 in (list(data[key])):
            if (key2 == module):
                res[key2] = data[key][key2]
                print(res)
    return json.dumps(res) if len(res) != 0 else jsonify(code=412,message="Module introuvable")
##param pour prendre les modules incomplets

def fetch_modules_list(data, semestre):
    res = {}
    for key in (list(data)):
        if(key == 'semestre '+str(semestre)):
            res = data[key]
    return res if len(res) != 0 else jsonify(code=411,message="Modules introuvables")
#######################################
##                                   ##
##        listes des routes          ##
##                                   ##
#######################################
##route pour la page de doc
@app.route('/doc', methods=['GET'])
def doc_page():
    return render_template('Doc_API_125216.html')
##redirection vers / quand la route n'existe pas
@app.errorhandler(404)
def page_not_found(e):
    return redirect('/doc')
#######################################
##                                   ##
##          routes pour A1           ##
##                                   ##
#######################################
@app.route('/api/edt/a1', methods=['GET'])
def edt_a1():
    try:
        with open('edt/A1_S'+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+'.json', encoding='utf-8') as f:
            content = json.load(f)
    except IOError:
        return jsonify(code=400,message="Edt non disponible")
    if request.args.get('img') == 'true':
        return send_file('edt/A1_S'+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+'.jpg', mimetype='image/jpeg')
    if request.args.get('g') != None:
        return fetch_groupe(content,request.args.get('g').upper())
    return json.dumps(content)
#######################################
##                                   ##
##          routes pour A2           ##
##                                   ##
#######################################
@app.route('/api/edt/a2', methods=['GET'])
def edt_a2():
    try:
        with open('edt/A2_S'+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+'.json', encoding='utf-8') as f:
            content = json.load(f)
    except IOError:
        return jsonify(code=400,message="Edt non indisponible")
    if request.args.get('img') == 'true':
        return send_file('edt/A2_S'+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+'.jpg', mimetype='image/jpeg')    
    if request.args.get('g') != None:
        return fetch_groupe(content,request.args.get('g').upper())
    return json.dumps(content)
#######################################
##                                   ##
##          routes pour A3           ##
##                                   ##
#######################################
@app.route('/api/edt/a3', methods=['GET'])
def edt_a3():
    try:
        with open('edt/A3_S'+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+'.json', encoding='utf-8') as f:
            content = json.load(f)
    except IOError:
        return jsonify(code=400,message="Edt non indisponible")
    if request.args.get('img') == 'true':
        return send_file('edt/A3_S'+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+'.jpg', mimetype='image/jpeg')    
    if request.args.get('g') != None:
        return fetch_groupe(content,request.args.get('g').upper())
    return json.dumps(content)
#######################################
##                                   ##
##       routes pour MODULES         ##
##                                   ##
#######################################
@app.route('/api/modules', methods=['GET'])
def modules():
    try:
        with open('modules/modules.json', encoding='utf-8') as f:
            content = json.load(f)
    except IOError:
        return jsonify(code=410,message='Les modules ne sont pas disponible')
    if request.args.get('m') != None:
        return fetch_modules(content, request.args.get('m').upper())
    if request.args.get('s') != None:
        return fetch_modules_list(content, request.args.get('s').upper())
    return json.dumps(content)



app.run(debug=True, port=80, host='0.0.0.0')


