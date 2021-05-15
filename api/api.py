import flask, json
import time
import atexit
#import getEdt
from apscheduler.schedulers.background import BackgroundScheduler
from flask import jsonify, request, render_template, redirect
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
        return data[list(data)[list(data).index(group)]]
    except ValueError:
        res = {}
        for key in (list(data)):
            if(key[:len(group)] == group):
                res[key] = data[key]
        return json.dumps(res) if len(res) != 0 else "ce groupe n'existe pas"


def fetch_modules(data, module):
    res = {}
    for key in (list(data)):
        for key2 in (list(data[key])):
            if (key2 == module):
                res[key2] = data[key][key2]
                print(res)
    return json.dumps(res) if len(res) != 0 else "ce module n'existe pas"
##param pour prendre les modules incomplets

def fetch_modules_list(data, semestre):
    res = {}
    for key in (list(data)):
        if(key == 'semestre '+str(semestre)):
            res = data[key]
    return res if len(res) != 0 else "ces modules n'existent pas"
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
        path = '/home/pi/edt-bot-iut/api/edt/A1_S'+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+'.json'
        print(path)
        with open('/home/pi/edt-bot-iut/api/edt/A1_S'+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+'.json', encoding='utf-8') as f:
            content = json.load(f)
    except IOError:
        return 'L\'edt de la semaine '+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+' n\'est pas disponible'
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
        with open('edt/A2_S'+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+'.json') as f:
            content = json.load(f)
    except IOError:
        return 'L\'edt de la semaine '+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+' n\'est pas disponible'
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
        with open('edt/A3_S'+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+'.json') as f:
            content = json.load(f)
    except IOError:
        return 'L\'edt de la semaine '+str(request.args.get('s') if request.args.get('s') != None else semaine_defaut)+' n\'est pas disponible'
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
        return 'Les modules ne sont pas disponible'
    if request.args.get('m') != None:
        return fetch_modules(content, request.args.get('m').upper())
    if request.args.get('s') != None:
        return fetch_modules_list(content, request.args.get('s').upper())
    return json.dumps(content)

# scheduler = BackgroundScheduler()
# scheduler.add_job(func=getEdt.fetch_edt, trigger="interval", seconds=7200)
# scheduler.start()

app.run(debug=True, port=80, host='0.0.0.0')


