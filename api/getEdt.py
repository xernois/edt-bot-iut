from selenium import webdriver
from selenium.webdriver.common import keys
driver = webdriver.Chrome (executable_path="C:\Program Files\chromedriver\chromedriver.exe")
driver.get("http://edt-iut-info.unilim.fr/edt/")
folders = driver.find_elements_by_xpath ("/html/body/table/tbody/tr")
for folder in folders:
    info = folder.text.split(" ")
    if(info[0].startswith('A')):
        print(info)
        driverEdt = webdriver.Chrome (executable_path="C:\Program Files\chromedriver\chromedriver.exe")
        driverEdt.get("http://edt-iut-info.unilim.fr/edt/"+info[0])
        edts = driverEdt.find_elements_by_xpath ("/html/body/table/tbody/tr")
        for edt in edts : 
            print(edt.text)
        driverEdt.quit()
driver.quit ()