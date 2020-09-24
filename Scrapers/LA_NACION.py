# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:18:02 2020

@author: Tomas
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C:/Users/Tomas/Documents/GitHub/Waltmart_scrapper/chromedriver.exe')
#Pagina Web
driver.get("https://buscar.lanacion.com.ar/economia")




#BUCLE DE PAGINACION HORIZONTAL
i = 0
link_de_paginas=[]
while i < 17:
    links = driver.find_elements_by_xpath('//li[@class="floatFix notas"]//span[@class="tituloNota"]//h2/a')
    
    for k in links:
        link_de_paginas.append(k.get_attribute("href"))
        
        
    boton = driver.find_element(By.XPATH, '(//div[@class="grisClaro pag"]//a)[last()]')
    boton.click()
#    if i == 0 :
        
#        boton = driver.find_element(By.XPATH, '(//div[@class="grisClaro pag"]//a)[11]')
#        boton.click()
#    else:
#        boton = driver.find_element(By.XPATH, '(//div[@class="grisClaro pag"]//a)[12]')
#        boton.click()   
#    else:
#        boton = driver.find_element(By.XPATH, '(//div[@class="grisClaro pag"]//a)[12]')
#        boton.click()    
    i += 1 
    
    
    
import requests
from bs4 import BeautifulSoup 
 
# URL SEMILLA

d = []
for url in link_de_paginas:
    respuesta = requests.get(url)
 
    soup = BeautifulSoup(respuesta.text)
     
    article = soup.find(id="nota")
    parrafos = article.find_all('p')
    titulos = soup.find_all(class_='titulo') # ENCONTRAR POR CLASE
    fechas = soup.find_all(class_='fecha')# ENCONTRAR POR CLASE
    notta = ""
    for parrafo in parrafos:
        nott = parrafo.text
        notta += nott
        
        print(parrafo.text)
      
      
    for titulo in titulos:
        
        tit =titulo.text
      
    for fecha in fechas:
        fec =fecha.text
      
      
      
    d.append({"titulo":tit,"fecha":fec,"nota":notta,"link":url })  
        
    
    
'''
#paginacion vertical
d = []
for l in link_de_paginas:
    driver.get(l)
    titulos= driver.find_elements_by_xpath('//section[@class="encabezado"]//h1[@class="titulo"]')
    for ti in titulos:
        tit = ti.text
        print(tit)
        
    fecha=  driver.find_elements_by_xpath('//section[@class="fecha"]')
    for fe in fecha:
        fec = fe.text
        print(fec)
    nota=   driver.find_elements_by_xpath('//section[@id="cuerpo"]//p')
    nott = ""
    for no in nota:
        nott = no.text
        print(nott)
    d.append({"titulo":tit,"fecha":fec,"nota":nott,"link":l})
#    except:
        
 #       eee= "error"
  #      d.append({"titulo":l,"fecha":eee,"nota":eee,"link":l })
    
    '''
import pandas as pd
Final=pd.DataFrame(d)
Final.to_csv("./Lanacion_final_2.csv")

d


