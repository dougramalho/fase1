from fastapi import FastAPI
from app.routers import producao, processamento, comercializacao, importacao, exportacao
from app.database import engine
from app.models import producao as producao_model
from app.models import processamento as processamento_model

# Criar as tabelas no banco de dados
producao_model.Base.metadata.create_all(bind=engine)
processamento_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluindo os routers
app.include_router(producao.router)
app.include_router(processamento.router)
app.include_router(comercializacao.router)
app.include_router(importacao.router)
app.include_router(exportacao.router)

@app.get("/")
def read_root():
    return {"message": "API Vitivinicultura"}
