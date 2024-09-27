import requests
from bs4 import BeautifulSoup
from utils import parse_quantidade, send_to_api

# Dicionário para mapear os tipos de processamento e suas subopções
TIPOS_PROCESSAMENTO = {
    "Viníferas": "subopt_01",
    "Americanas e Híbridas": "subopt_02",
    "Uvas de mesa": "subopt_03",
    "Sem classificação": "subopt_04"
}

def scrape_processamento(ano):
    base_url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&subopcao={subopcao}&opcao=opt_03'
    data = []
    # Iterar pelos diferentes tipos de processamento
    for tipo_processamento, subopcao in TIPOS_PROCESSAMENTO.items():
        url = base_url.format(ano=ano, subopcao=subopcao)
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Erro ao acessar a página para o ano {ano}, tipo {tipo_processamento}: {response.status_code}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='tb_base tb_dados')

        if not table:
            print(f"Nenhuma tabela encontrada para o tipo {tipo_processamento} no ano {ano}")
            continue

        current_category = None

        # Iterar pelas linhas da tabela
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
                        "categoria_cultivo": current_category,
                        "tipo_processamento": tipo_processamento,
                        "descricao_cultivo": descricao,
                        "quantidade": quantidade,
                        "ano": ano
                    })
    return data

