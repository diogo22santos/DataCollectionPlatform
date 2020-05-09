# libs
import ssl
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def request(*, baseline_url=None, baseline_headers=None):
    """Makes the request to the URL page"""
    try:
        req = requests.get(baseline_url, headers=baseline_headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        return soup
    except ConnectionRefusedError:
        print('Connection refused by the server')
        time.sleep(2)


def save_dataframe(*, data=None, columns: list, path_to_save: str, file_name: str):
    saved_dataframe = pd.DataFrame.from_records(data, columns=columns)
    saved_path = f'{path_to_save}/{file_name}'
    saved_dataframe.to_csv(path_or_buf=saved_path, index=None)
    print('Saved file', saved_path)


def worten_scrapping(*, soup=None):
    """Makes the scrap to Worten Page"""
    data = []

    containers = soup.find_all('div', class_='w-product')
    for container in containers:
        if container.find('div', class_='w-flag top right') is not None:
            # guardar produtos
            produto = container.find('div', class_='w-product__title__wrapper').h3.text

            # guardar promocoes
            promocao = container.find('div', class_='w-flag top right').text.replace('\n', ' ').strip()

            # guardar preco
            preco = container.find('span', class_='w-currentPrice iss-current-price').text

            # guardar preco antigo
            if container.find('span', class_='w-oldPrice') is not None:
                preco_antigo = container.find('span', class_='w-oldPrice').text
            else:
                preco_antigo = preco

            # guardar descricao do produto
            descricao = container['data-category'].split('/')[1].replace('-', ' ')

        data.append([produto, promocao, preco, preco_antigo, descricao])
    return data