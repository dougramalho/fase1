from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Cultivo(Base):
    __tablename__ = "cultivos"

    id = Column(Integer, primary_key=True, index=True)
    categoria_cultivo = Column(String, index=True)
    descricao_cultivo = Column(String, index=True)
    tipo_processamento = Column(String, index=True)
    quantidade = Column(Float)
    ano = Column(Integer)
