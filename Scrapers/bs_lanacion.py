# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:17:52 2020

@author: Tomas
"""

import requests
from bs4 import BeautifulSoup 
import requests

 
# URL SEMILLA
url = 'https://www.lanacion.com.ar/opinion/seguro-desempleo-debate-impostergable-nid2444396'
 
# REQUERIMIENTO AL SERVIDOR
respuesta = requests.get(url)
 
soup = BeautifulSoup(respuesta.text)
 
article = soup.find(id="nota")
parrafos = article.find_all('p')
titulos = soup.find_all(class_='titulo') # ENCONTRAR POR CLASE

fechas = soup.find_all(class_='fecha')# ENCONTRAR POR CLASE
for parrafo in parrafos:
  print (parrafo.text)
  
  
for titulo in titulos:
  print (titulo.text)
  
for fecha in fechas:
  print (fecha.text)
  
  