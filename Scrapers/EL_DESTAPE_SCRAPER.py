# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:33:34 2020

@author: Tomas
"""


from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome('C:/Users/Tomas/Documents/GitHub/Waltmart_scrapper/chromedriver.exe')
#Pagina Web
driver.get("https://www.eldestapeweb.com/buscar/economia")




#BUCLE DE PAGINACION HORIZONTAL
i = 0
link_de_paginas=[]
while i < 1:
    sleep(10)
    
        
    driver.execute_script("window.scrollBy(0,3000)","")
    #boton = driver.find_element(By.XPATH, ('//button[@data-tipo="seccion"]'))
    #boton.click()
    
    i += 1 
links = driver.find_elements_by_xpath('//div[@class="titulo"]//h2/a')
    
for k in links:
    link_de_paginas.append(k.get_attribute("href"))
print(link_de_paginas)
#paginacion vertical
import requests
from bs4 import BeautifulSoup     
    
d = []

for l in link_de_paginas:
    respuesta = requests.get(l)
 
    soup = BeautifulSoup(respuesta.text)
     
    titulos = soup.find_all(itemprop="headline")
    for ti in titulos:
        tit = ti.text
        print(tit)
        
    fechas = soup.find_all(class_='fecha')
    for fe in fechas:
        fec = fe.text
        print(fec)
    article = soup.find(class_="nota_contenido")
    nota = article.find_all('p')
    
    notta = ""
    for no in nota:
        nott = no.text
        notta += nott
        
    print(notta)
    d.append({"titulo":tit,"fecha":fec,"nota":notta,"link":l})
#    except:
        
 #       eee= "error"
  #      d.append({"titulo":l,"fecha":eee,"nota":eee,"link":l })
    
    
import pandas as pd
Final=pd.DataFrame(d)
Final.to_csv("./eldestape_final.csv")

d
