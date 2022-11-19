#Boiler room kenny beats/kaytranada
#Biblioteca para manipulação de dados
import pandas as pd 

#Biblioteca para pausar o código
import time

#Bibliotecas para mineração de dados
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#Abrindo o chrome
#driver = webdriver.Chrome('chromedriver')

#Url do site de estatisticas 
url = 'https://fbref.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

lista_urls = []

for url in soup.find_all('a', href=True):
    lista_urls.append(url['href'])


links_squads = [url for url in lista_urls if 'squad' and 'Men-Stats' in url]

#Retirando as primeiros 5 urls e o último que não são da copa do mundo
lista_url_times = links_squads[6:]
lista_url_times.pop(-1)

assert len(lista_url_times) == 32

link_base = 'https://fbref.com'

#Abrindo o chrome
driver = webdriver.Chrome('chromedriver')

#Iterando por cada url da lista de urls dos times
for url in lista_url_times:
    link = f'{link_base}{url}'
    #Entro no site
    driver.get(link)
    time.sleep(2)

    table = pd.read_html(url)
    print(table)
    time.sleep(2)


    #Crio o dataframe com pandas

    #

#Fechando o chrom
webdriver.close()
webdriver.quit()



