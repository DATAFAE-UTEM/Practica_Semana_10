#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importaciones
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Set options & open server
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options,
                          executable_path="C:\\Program Files (x86)\\chromedriver.exe")

# Definicion de url
url = 'https://es.finance.yahoo.com/quote/COPEC.SN/key-statistics?p=COPEC.SN'

# Informacion asociada a la tabla
driver.get(url)
print(driver.title)
time.sleep(8)

# Estructura de data
data1 = {}
df1 = pd.DataFrame(
    columns=['Info'])  # Nombres de los header de tabla

rows = len(driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[1]/div/div/div/div/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[1]/div/div/div/div/table/tbody/tr[2]/td"))

print(rows)
print(cols)

# Considerar Alinear elementos dentro de 'data['']' segun definicion de headers
# PERMITE EXTRAER HASTA ZAMBIA, LUEGO EL MODELO SE QUIEBRA POR ESTRUCTURA DE TABLA PRESENTE AL FINAL.

# Tabla

data = {}
df = pd.DataFrame(columns=['Medidas de valorizacion', 'Valores'])

for r in range(1, rows + 1):
        data['Medidas de valorizacion'] = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[1]/div/div/div/div/table/tbody/tr["+str(r)+"]/td[1]").text
        data['Valores'] = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[1]/div/div/div/div/table/tbody/tr["+str(r)+"]/td[2]").text
        df = df.append(data, ignore_index=True)
        print(df)
        df.to_csv('Tabla Copec')

