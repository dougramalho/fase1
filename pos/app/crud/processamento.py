from sqlalchemy.orm import Session
from app.models.processamento import Cultivo
from app.schemas.processamento import CultivoCreate

def get_processamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cultivo).offset(skip).limit(limit).all()

def get_processamento_by_ano(db: Session, ano: int, skip: int = 0, limit: int = 10):
    return db.query(Cultivo).filter(Cultivo.ano == ano).offset(skip).limit(limit).all()

def get_processamento(db: Session, cultivo_id: int):
    return db.query(Cultivo).filter(Cultivo.id == cultivo_id).first()

def create_processamento(db: Session, cultivo: CultivoCreate):
    db_cultivo = Cultivo(
        categoria_cultivo=cultivo.categoria_cultivo,
        descricao_cultivo=cultivo.descricao_cultivo,
        tipo_processamento=cultivo.tipo_processamento,
        quantidade=cultivo.quantidade,
        ano=cultivo.ano
    )
    db.add(db_cultivo)
    db.commit()
    db.refresh(db_cultivo)
    return db_cultivo

def update_processamento(db: Session, cultivo_id: int, cultivo: CultivoCreate):
    db_cultivo = db.query(Cultivo).filter(Cultivo.id == cultivo_id).first()
    if db_cultivo:
        db_cultivo.categoria_cultivo = cultivo.categoria_cultivo
        db_cultivo.descricao_cultivo = cultivo.descricao_cultivo
        db_cultivo.quantidade = cultivo.quantidade
        db_cultivo.ano = cultivo.ano
        db_cultivo.tipo_processamento=cultivo.tipo_processamento,
        db.commit()
        db.refresh(db_cultivo)
    return db_cultivo

def delete_processamento(db: Session, cultivo_id: int):
    db_cultivo = db.query(Cultivo).filter(Cultivo.id == cultivo_id).first()
    if db_cultivo:
        db.delete(db_cultivo)
        db.commit()
