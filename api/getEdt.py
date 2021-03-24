from selenium import webdriver
from selenium.webdriver.common import keys
driver = webdriver.Chrome (executable_path="C:\Program Files\chromedriver\chromedriver.exe")
driver.get("http://edt-iut-info.unilim.fr/edt/A1/")
l = driver.find_elements_by_xpath ("/html/body/table/tbody/tr")
for i in l:
    print(i.text)
driver.quit ()