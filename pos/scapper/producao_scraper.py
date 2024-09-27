import requests
from bs4 import BeautifulSoup
from utils import parse_quantidade, send_to_api

def scrape_producao(ano):
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erro ao acessar a página para o ano {ano}: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='tb_base tb_dados')

    data = []
    current_category = None

    for row in table.find('tbody').find_all('tr'):
        columns = row.find_all('td')
        if len(columns) == 2:
            categoria = columns[0].get_text(strip=True)
            quantidade_text = columns[1].get_text(strip=True)
            quantidade = parse_quantidade(quantidade_text)

            if "tb_item" in columns[0]['class']:
                current_category = categoria
            elif "tb_subitem" in columns[0]['class']:
                descricao = categoria
                data.append({
                    "categoria_produto": current_category,
                    "descricao_produto": descricao,
                    "quantidade": quantidade,
                    "ano": ano
                })

    return data
