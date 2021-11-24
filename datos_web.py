#   crear un modulo llamado datos_web con una clase llamada GetWebData que tiene los siguientes métodos
#       1. __init__(self, url) se le pasa la URL de la página de la que queremos obtener información
#       2. get_data(self, parser) se le pasa la estructura xml de la pagina donde encontrar el dato.
#           devuelve el dato
#   solicitar por teclado el pais y la ciudad de la que se quiere consultar la hora
#   desde el modulo principal crear la URL necesaria para consultar la hora de esa ciudad en www.timeanddate.com crear un objeto con esa URL
#   usar el metodo gte_data del objeto creado para consultar la hora en la ciudad



import requests
from lxml import html

url = "https://www.timeaanddate.com/worldclock/españa/madrid"
page = requests.get(url)
print('\n\n\nhtml:\n', page.text, '\n\n\n')
tree = html.fromstring(page, content)
print('\n\n\ntree:\n', tree, '\n\n\n')

time = tree.xpath('//span[@class="h1"]/text()')
print("\nHora: ", time)
