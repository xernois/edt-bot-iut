import requests
import pathlib
import main
import os
import pdf2image
from datetime import datetime
from bs4 import BeautifulSoup


def download_edt(file_name):
    print(datetime.now().strftime(
        "[%d/%m/%Y %H:%M:%S]"), 'Download :', file_name)
    pdf = requests.get(
        'http://edt-iut-info.unilim.fr/edt/' + file_name, stream=True)
    pages = pdf2image.convert_from_bytes(pdf.raw.read())
    for page in pages:
        page.save('edt/'+file_name.split('/')[1].split('.')[0]+".jpg", 'JPEG')
        main.main('edt/'+file_name.split('/')[1].split('.')[0]+".jpg")
        if os.path.exists('edt/'+file_name.split('/')[1].split('.')[0]+".jpg"):
            os.remove('edt/'+file_name.split('/')[1].split('.')[0]+".jpg")


def fetch_edt():
    html = BeautifulSoup(requests.get(
        "http://edt-iut-info.unilim.fr/edt/").content, features="html.parser")
    listPromo = html.select('td a')
    listPromo.pop(0)
    for link in listPromo:
        html = BeautifulSoup(requests.get(
            "http://edt-iut-info.unilim.fr/edt/"+link.get('href')).content, features="html.parser")
        listEdt = html.select('tr')
        for edt in listEdt[3:-1]:
            data = edt.select('td')
            name = data[1].find('a').get('href')
            date = data[2].text.split(' ')
            date_edt = [int(data) for data in date[0].split("-")]
            heure_edt = [int(data) for data in date[1].split(":")]
            date = datetime(int(date_edt[0]), int(date_edt[1]), int(
                date_edt[2]), heure_edt[0], heure_edt[1])
            try:
                with open('edt/' + name.split('.')[0] + '.json') as f:
                    if(datetime.fromtimestamp(pathlib.Path('edt/' + name.split('.')[0] + '.json').stat().st_ctime) < date):
                        download_edt(link.get('href')+name)
            except IOError:
                download_edt(link.get('href')+name)


fetch_edt()
