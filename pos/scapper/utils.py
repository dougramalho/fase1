import requests
import time

def parse_quantidade(quantidade_text):
    """
    Converte a quantidade de string para float, removendo pontos e vírgulas. 
    Substitui '-' por 0.0.
    """
    if quantidade_text in ['-', 'nd', '*'] or not quantidade_text:
        return 0.0
    return float(quantidade_text.replace('.', '').replace(',', '.'))

def send_to_api(data, endpoint):
    """
    Envia os dados para a API no endpoint especificado.
    """
    api_url = f'http://127.0.0.1:8000/{endpoint}/'
    headers = {'Content-Type': 'application/json'}
    
    for entry in data:
        response = requests.post(api_url, json=entry, headers=headers)
        if response.status_code in [200, 201]:
            print(f"Dados enviados com sucesso: {entry}")
        else:
            print(f"Erro ao enviar os dados: {response.status_code} - {response.text}")
        time.sleep(0.2)  # Delay de 1 segundo entre requisições
