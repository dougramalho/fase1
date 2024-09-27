from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Importacao(Base):
    __tablename__ = "importacoes"

    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String, index=True)
    pais_origem = Column(String, index=True)
    quantidade= Column(Integer)
    valor= Column(Float)
    ano= Column(Integer)
    
