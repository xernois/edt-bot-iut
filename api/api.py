import flask
from flask import jsonify, request
from selenium import webdriver
from selenium.webdriver.common import keys


app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/a1', methods=['GET'])
def edt_a1():
    results = ""
    driver = webdriver.Chrome(
        executable_path="C:\Program Files\chromedriver\chromedriver.exe")
    driver.get("http://edt-iut-info.unilim.fr/edt/A1/")
    l = driver.find_elements_by_xpath("/html/body/table/tbody/tr")
    for i in l:
        results += "\n" + i.text
    driver.quit()
    return results


@app.route('/api/a2', methods=['GET'])
def edt_a2():
    results = ""
    driver = webdriver.Chrome(
        executable_path="C:\Program Files\chromedriver\chromedriver.exe")
    driver.get("http://edt-iut-info.unilim.fr/edt/A2/")
    l = driver.find_elements_by_xpath("/html/body/table/tbody/tr")
    for i in l:
        results += "\n" + i.text
    driver.quit()
    return results


@app.route('/api/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)
    return jsonify(results)


app.run()
