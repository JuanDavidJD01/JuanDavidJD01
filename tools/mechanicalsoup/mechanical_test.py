#!/usr/bin/env python3
import mechanicalsoup

#Crear el navegador
browser = mechanicalsoup.StatefulBrowser()

#Abrir la pagina de Wikipedia de Scrapy
browser.open("https://es.wikipedia.org/wiki/Scrapy")

#Extraer el texto de la pagina
page = browser.get_current_page()

#Buscar el contenido principal del articulo
content = page.find('div', {'class': 'mw-parser-output'})

#Extraer los parrafos
paragraphs = content.find_all('p')

#Imprimir los parrafos encontrados
for paragraph in paragraphs:
    print(paragraph.get_text(strip=True))
    print("="*40)