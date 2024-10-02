## Ativando o ambiente

```
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

## Instalando as dependências

```
pip install -r requirements.txt
```

## Executando a API

```
uvicorn app.main:app --reload
```

## Consultando a documentação da API

http://127.0.0.1:8000/docs

## Realizando uma carga de dados a partir do scrapper

python main_scraper.py producao --ano_inicial 1970 --ano_final 2023
python main_scraper.py processamento --ano_inicial 1970 --ano_final 2023
python main_scraper.py comercializacao --ano_inicial 1970 --ano_final 2023
python main_scraper.py importacao --ano_inicial 1970 --ano_final 2023
python main_scraper.py exportacao --ano_inicial 1970 --ano_final 2023
