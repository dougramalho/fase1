import argparse
from producao_scraper import scrape_producao
from processamento_scraper import scrape_processamento
from comercializacao_scraper import scrape_comercializacao
from importacao_scraper import scrape_importacao
from exportacao_scraper import scrape_exportacao
from utils import send_to_api

# Função principal para rodar o scraper baseado na entidade escolhida
def run_scraper(entidade, ano_inicial, ano_final):
    for ano in range(ano_inicial, ano_final + 1):
        print(f"Scrapando dados para o ano {ano}")
        if entidade == 'producao':
            dados = scrape_producao(ano)
            send_to_api(dados, 'producao')
        elif entidade == 'processamento':
            dados = scrape_processamento(ano)
            send_to_api(dados, 'processamento')
        elif entidade == 'comercializacao':
            dados = scrape_comercializacao(ano)
            send_to_api(dados, 'comercializacao')
        elif entidade == 'importacao':
            dados = scrape_importacao(ano)
            send_to_api(dados, 'importacao')
        elif entidade == 'exportacao':
            dados = scrape_exportacao(ano)
            send_to_api(dados, 'exportacao')
        else:
            print(f"Entidade {entidade} não reconhecida.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scraper para diferentes entidades de viticultura.')
    parser.add_argument('entidade', choices=['producao', 'processamento', 'comercializacao', 'importacao', 'exportacao'],
                        help='Escolha a entidade para scrapping: producao, processamento, comercializacao, importacao, exportacao')
    parser.add_argument('--ano_inicial', type=int, default=1970, help='Ano inicial para scraping (default: 1970)')
    parser.add_argument('--ano_final', type=int, default=2023, help='Ano final para scraping (default: 2023)')

    args = parser.parse_args()

    run_scraper(args.entidade, args.ano_inicial, args.ano_final)
