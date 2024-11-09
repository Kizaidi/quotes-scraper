import requests
from bs4 import BeautifulSoup
import json

# URL do site
url = "https://quotes.toscrape.com/"

# Lista para armazenar os dados coletados
quotes_list = []

# Função para coletar citações
def collect_quotes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar todas as citações na página
    quotes = soup.find_all('div', class_='quote')
    
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        
        quotes_list.append({
            'text': text,
            'author': author,
            'tags': tags
        })

# Coletar dados da primeira página
collect_quotes(url)

# Salvar os dados em um arquivo JSON
with open('quotes.json', 'w', encoding='utf-8') as f:
    json.dump(quotes_list, f, ensure_ascii=False, indent=4)

print("Dados coletados e salvos em quotes.json")
