# Temos 2 ferramentas mais utilizadas para web scraping

# Selenium - Mais complexo consegue passar por captchas e atuar mais humano
# BeutifulSoup - Mais simples mas bem documentado e bem capaz


# Pega o html da file
with open(r"C:\Users\FranciscoFroes\Documents\GitHub\Python-conceitos-legais\Web Scraping\windham.htm") as wyndham_file:

    # Arquiva a respostas.
    html_text = wyndham_file.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_text,"html.parser")

print(soup.prettify())