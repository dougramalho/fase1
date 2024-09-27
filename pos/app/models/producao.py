from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Producao(Base):
    __tablename__ = "producoes"

    id = Column(Integer, primary_key=True, index=True)
    categoria_produto = Column(String, index=True)
    descricao_produto = Column(String, index=True)
    quantidade = Column(Float)
    ano = Column(Integer)
