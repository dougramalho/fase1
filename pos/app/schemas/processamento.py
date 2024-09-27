from pydantic import BaseModel

class CultivoBase(BaseModel):
    categoria_cultivo: str
    tipo_processamento: str
    descricao_cultivo: str
    quantidade: float
    ano: int

class CultivoCreate(CultivoBase):
    pass

class Cultivo(CultivoBase):
    id: int

    class Config:
        orm_mode = True