import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []
lista_desc = []
url_ML = 'https://lista.mercadolivre.com.br/'  # URL mercado livre
produto_nome = input('Qual produto você deseja?: ')
response = requests.get(url_ML+produto_nome)
content = response.content

site = BeautifulSoup(content, 'html.parser')
produtos = site.findAll('li', attrs={'class': 'ui-search-layout__item'})
descontos = site.findAll(
    'span', attrs={'class': 'andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript'})
for produto in produtos:
    titulo = produto.find('h2', attrs={
        'ui-search-item__title'})
    link = produto.find('a', attrs={
        'ui-search-link'})
    estrela = produto.find('span', attrs={
        'ui-search-reviews__rating-number'})
    # print('produto:', titulo.text)
    # print('link do produto:', link['href'])

    lista_produtos.append(
        [titulo.text, link['href']])
    # print(lista_produtos)

for desconto in descontos:
    preco2 = desconto.find(
        'span', attrs={'class': 'andes-money-amount__fraction'})
    centavos2 = desconto.find('span', attrs={
                              'class': 'andes-money-amount__cents andes-money-amount__cents--superscript-24'})
    if (centavos2):
        lista_desc.append(
            [preco2.text + ',' + centavos2.text])
    else:
        lista_desc.append(
            [preco2.text])
    lista_desc.append([preco2.text])
    completo = list(zip(lista_produtos, lista_desc))
    # print(lista_desc)

# print(lista_desc)

# print(lista_desc)
# print(lista_desc)


news = pd.DataFrame(completo, columns=[
    'Título', 'Link'])

news.to_excel(produto_nome+' '+'Produto.xlsx', index=False)
print('Tabela criada com sucesso!')

# h2 ui-search-item__title - nome do produto
# span andes-money-amount__fraction - preço
