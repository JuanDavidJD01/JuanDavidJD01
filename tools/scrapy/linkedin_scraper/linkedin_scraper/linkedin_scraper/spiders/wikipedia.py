#!/usr/bin/env python3
import scrapy


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["es.wikipedia.org"]
    start_urls = ["https://es.wikipedia.org/wiki/Scrapy"]

    def parse(self, response):
        # Extraer el texto principal de la página
        titulo = response.css('h1::text').get()  # Extrae el título de la página
        parrafos = response.css('p::text').getall()  # Extrae todos los párrafos
        
        # Combinar párrafos en un solo texto
        contenido = "\n".join(parrafos)

        # Mostrar el texto extraído
        print("\n=== TÍTULO ===\n")
        print(titulo)
        print("\n=== CONTENIDO ===\n")
        print(contenido)
