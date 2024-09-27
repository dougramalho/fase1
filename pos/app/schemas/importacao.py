from pydantic import BaseModel

class ImportacaoBase(BaseModel):
    categoria: str
    pais_origem: str
    quantidade: int
    valor: float
    ano: int

class ImportacaoCreate(ImportacaoBase):
    pass

class Importacao(ImportacaoBase):
    id: int

    class Config:
        orm_mode = True