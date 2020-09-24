# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:22:23 2020

@author: Tomas
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome('C:/Users/Tomas/Documents/GitHub/Waltmart_scrapper/chromedriver.exe')
#Pagina Web
driver.get("https://www.clarin.com/economia/")
#Scroll
sleep(2) #:

driver.execute_script("window.scrollBy(0,3000)","")

driver.execute_script("window.scrollBy(0,3000)","")
sleep(1) #seconds
#detecta todos los productos y los convierte en una lista
noticias_superior = driver.find_elements_by_xpath(".//div[@class='border box col-lg-6 col-md-8 col-sm-12 col-xs-12 no-p border']//a[1]")


noticias_superior2 = driver.find_elements_by_xpath(".//div[@class='box col-lg-3 col-md-4 col-sm-6 col-xs-12 no-p border ']//a[1]")

noticias =   driver.find_elements_by_xpath('.//div[@class="box col-lg-4 col-md-6 col-sm-12 no-p border "]//a[1]')
links_de_la_pagina = []

for k in noticias_superior2:
    links_de_la_pagina.append(k.get_attribute("href"))
    print(links_de_la_pagina)
    
for k in noticias_superior:
    links_de_la_pagina.append(k.get_attribute("href"))
    print(links_de_la_pagina)


for l in noticias:
    links_de_la_pagina.append(l.get_attribute("href"))
    print(links_de_la_pagina)
    
    
d=[]

for link in links_de_la_pagina:
    try:
        driver.get(link)
        titulo= driver.find_elements_by_xpath('.//div[@class="title"]//h1[@id="title"]')
        fecha=  driver.find_elements_by_xpath('.//div[@class="class="breadcrumb col-lg-6 col-md-12 col-sm-12 col-xs-12""]//span]')
        nota=   driver.find_elements_by_xpath('.//div[@class="body-nota"]//p')
        
        for t in titulo:
            tit =   t.text
        for f in fecha:
            fec =   f.text
        for n in nota:
            no =    n.text
        d.append({"titulo":titulo,"fecha":fecha,"nota":nota,"link":link })
    except:
        print("Error")
    
    
d
import pandas as pd
Final=pd.DataFrame(d)
Final.to_csv("./Scrapping.csv")

fec


