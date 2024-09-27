from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Exportacao(Base):
    __tablename__ = "exportacoes"

    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String, index=True)
    pais_destino = Column(String, index=True)
    quantidade= Column(Integer)
    valor= Column(Float)
    ano= Column(Integer)
    
