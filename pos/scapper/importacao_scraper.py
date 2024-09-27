import requests
from bs4 import BeautifulSoup
from utils import parse_quantidade, send_to_api

# Dicionário para mapear os tipos de processamento e suas subopções
TIPOS_IMPORTACAO = {
    "Vinhos de mesa": "subopt_01",
    "Espumantes": "subopt_02",
    "Uvas frescas": "subopt_03",
    "Uvas passas": "subopt_04",
    "Suco de uva": "subopt_05",
}

def scrape_importacao(ano):
    base_url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&subopcao={subopcao}&opcao=opt_05'
    data = []
    # Iterar pelos diferentes tipos de processamento
    for tipo_importacao, subopcao in TIPOS_IMPORTACAO.items():
        url = base_url.format(ano=ano, subopcao=subopcao)
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Erro ao acessar a página para o ano {ano}, tipo {tipo_importacao}: {response.status_code}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='tb_base tb_dados')

        if not table:
            print(f"Nenhuma tabela encontrada para o tipo {tipo_importacao} no ano {ano}")
            continue

        for row in table.find('tbody').find_all('tr'):
            columns = row.find_all('td')
            if len(columns) == 3:
                pais_origem = columns[0].get_text(strip=True)
                quantidade_text = columns[1].get_text(strip=True)
                quantidade = parse_quantidade(quantidade_text)

                valor_text = columns[1].get_text(strip=True)
                valor = parse_quantidade(valor_text)

                data.append({
                    "categoria": tipo_importacao,
                    "pais_origem": pais_origem,
                    "quantidade": quantidade,
                    "valor": valor,
                    "ano": ano
                })
    return data

