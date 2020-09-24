# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:31:33 2020

@author: Tomas
"""


from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome('C:/Users/Tomas/Documents/GitHub/Waltmart_scrapper/chromedriver.exe')
#Pagina Web
driver.get("https://www.eldestapeweb.com/politica/precios-cuidados/alberto-fernandez-cuando-uno-gana-mucho-y-otros-pierden-mucho-no-es-una-sociedad-es-una-estafa--202091413410")



link_de_paginas = ["https://www.eldestapeweb.com/politica/precios-cuidados/alberto-fernandez-cuando-uno-gana-mucho-y-otros-pierden-mucho-no-es-una-sociedad-es-una-estafa--202091413410"]
d=[]
for l in link_de_paginas:
    driver.get(l)
    titulos= driver.find_elements_by_xpath('//h1[@class="titulo"]')
    for ti in titulos:
        tit = ti.text
        print(tit)
        
    fecha=  driver.find_elements_by_xpath('//div[@class="fecha"]')
    for fe in fecha:
        fec = fe.text
        print(fec)
    nota=   driver.find_elements_by_xpath('//div[@class="nota_contenido"]//div[@class="cuerpo"]/p')
    nott = ""
    
    for no in nota:
        nott = no.text
        print(nott)
        
        
    d.append({"titulo":tit,"fecha":fec,"nota":nota,"link":l})
#    except:
        
 #       eee= "error"
  #      d.append({"titulo":l,"fecha":eee,"nota":eee,"link":l })
    
    
import pandas as pd
Final=pd.DataFrame(d)
Final.to_csv("./eldestape2z.csv")