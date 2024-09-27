from pydantic import BaseModel

class ProducaoBase(BaseModel):
    categoria_produto: str
    descricao_produto: str
    quantidade: float
    ano: int

class ProducaoCreate(ProducaoBase):
    pass

class Producao(ProducaoBase):
    id: int

    class Config:
        orm_mode = True