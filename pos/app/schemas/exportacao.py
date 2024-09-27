from pydantic import BaseModel

class ExportacaoBase(BaseModel):
    categoria: str
    pais_destino: str
    quantidade: int
    valor: float
    ano: int

class ExportacaoCreate(ExportacaoBase):
    pass

class Exportacao(ExportacaoBase):
    id: int

    class Config:
        orm_mode = True