import requests
from bs4 import BeautifulSoup
import time

def scrape_producao(ano):
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02'
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erro ao acessar a página para o ano {ano}: {response.status_code}")
        return []

    # Parseando o conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrando a tabela de interesse
    table = soup.find('table', class_='tb_base tb_dados')
    
    data = []
    current_category = None

    # Iterando pelas linhas da tabela
    for row in table.find('tbody').find_all('tr'):
        columns = row.find_all('td')
        if len(columns) == 2:
            # Limpando os dados
            categoria = columns[0].get_text(strip=True)
            quantidade_text = columns[1].get_text(strip=True)
            quantidade = parse_quantidade(quantidade_text)
            
            # Atualizando a categoria se for uma nova
            if "tb_item" in columns[0]['class']:
                current_category = categoria
            # Se for uma subcategoria, mantém a categoria corrente
            elif "tb_subitem" in columns[0]['class']:
                descricao = categoria
                data.append({
                    "categoria_produto": current_category,
                    "descricao_produto": descricao,
                    "quantidade": quantidade,
                    "ano": ano
                })

    return data

def parse_quantidade(quantidade_text):
    if quantidade_text == '-' or not quantidade_text:
        return 0.0
    return float(quantidade_text.replace('.', '').replace(',', '.'))

def send_to_api(data):
    api_url = 'http://127.0.0.1:8000/producao/'  # Endpoint da API de Produção
    headers = {'Content-Type': 'application/json'}
    
    for entry in data:
        response = requests.post(api_url, json=entry, headers=headers)
        if response.status_code in [200, 201]:
            print(f"Dados enviados com sucesso: {entry}")
        else:
            print(f"Erro ao enviar os dados: {response.status_code} - {response.text}")
            print(entry)
            
        time.sleep(1)

    

if __name__ == '__main__':
    for ano in range(1970, 2024):
        print(f"Scrapando dados para o ano {ano}")
        producoes = scrape_producao(ano)
        
        if producoes:
            print(f"Enviando {len(producoes)} registros para o ano {ano}")
            send_to_api(producoes)
        else:
            print(f"Nenhuma produção encontrada para o ano {ano}")



