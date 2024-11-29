#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def fetch_page_content(url):
    """
    Fetches the content of the given URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def extract_text_from_page(html_content):
    """
    Extracts the main text content from the HTML page.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    #Extraer el titulo
    title = soup.title.string if soup.title else "No Title Found"

    paragraphs = [p.get_text() for p in soup.find_all('p')]

    return {
        "title": title,
        "paragraphs": paragraphs,
    }

if __name__ == "__main__":
    #URL a scrapear
    url = "https://es.wikipedia.org/wiki/Scrapy"

    html_content = fetch_page_content(url)

    if html_content:
        #Extraer datos
        extracted_data = extract_text_from_page(html_content)

        #Imprimir datos extraidos
        print(f"Title: {extracted_data['title']}\n")
        print("Content:")
        for paragraph in extracted_data['paragraphs']:
            print(paragraph)
            print("-" * 80)