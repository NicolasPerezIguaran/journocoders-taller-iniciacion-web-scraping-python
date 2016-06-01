# -*- encoding: utf-8 -*-
#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import csv
import unicodecsv

#defino y llamo a la url

url = 'http://www.cnmv.es/Portal/Consultas/MostrarListados.aspx?id=3'

response = requests.get(url)
html = response.content

#paso la url por BeautifulSoup

soup = BeautifulSoup(html, 'lxml')

#encuentro la tabla dentro del html

table = soup.find('table', attrs = {'id': 'ctl00_ContentPrincipal_grdListadoEsis'})

#disecciono la tabla en filas y columnas

for row in table.findAll('tr')[1:]:
    columns = row.findAll('td')
    denominacion_social = columns[0].string
    num_registro = columns[1].string
    fecha_registro = columns[2].string
    num_registro_gestora = columns[3].string
    denominacion_gestora = columns[4].string
    denominacion_social_depositaria = columns[5].string

    record = (denominacion_social,num_registro,fecha_registro,num_registro_gestora, denominacion_gestora,denominacion_social_depositaria)

    informacion = []
    informacion.append(record)

    ficherocsv = open("./fondos-inversion-cnmv.csv", "ab")
    contenido = unicodecsv.writer(ficherocsv)
    contenido.writerows(informacion)
