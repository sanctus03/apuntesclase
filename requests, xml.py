#   requests y xml
#   ambos requests y xml son librerias no estandar, hay que instalarlas
#   instalar el modulo desde la ventana packages

#   lxml, este módulo permite hacer scraping de paginas html
#   el modulo de requests permite interactuar con paginas web

""" web scrapping example"""
import requests
from lxml import html

url = "https://www.timeaanddate.com/worldclock/venezuela/caracas"
page = requests.get(url)
print('\n\n\nhtml:\n', page.text, '\n\n\n')
tree = html.fromstring(page, content)
print('\n\n\ntree:\n', tree, '\n\n\n')

time = tree.xpath('//span[@class="h1"]/text()')
print("\nHora: ", time)
