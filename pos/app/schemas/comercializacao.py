from pydantic import BaseModel

class ComercializacaoBase(BaseModel):
    categoria_produto: str
    descricao_produto: str
    quantidade: float
    ano: int

class ComercializacaoCreate(ComercializacaoBase):
    pass

class Comercializacao(ComercializacaoBase):
    id: int

    class Config:
        orm_mode = True