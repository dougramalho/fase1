# Base image - Usaremos a versão oficial do Python
FROM python:3.12

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o conteúdo do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Expor a porta que será usada pela aplicação
EXPOSE 8000

# Comando para rodar a aplicação usando Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
