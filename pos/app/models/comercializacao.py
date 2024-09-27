from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Comercializacao(Base):
    __tablename__ = "comercializacoes"

    id = Column(Integer, primary_key=True, index=True)
    categoria_produto = Column(String, index=True)
    descricao_produto = Column(String, index=True)
    quantidade = Column(Float)
    ano = Column(Integer)
