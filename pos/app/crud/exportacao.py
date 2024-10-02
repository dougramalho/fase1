from sqlalchemy.orm import Session
from app.models.exportacao import Exportacao
from app.schemas.exportacao import ExportacaoCreate

def get_exportacoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Exportacao).offset(skip).limit(limit).all()

def get_exportacao_by_ano(db: Session, ano: int, skip: int = 0, limit: int = 10):
    return db.query(Exportacao).filter(Exportacao.ano == ano).offset(skip).limit(limit).all()

def get_exportacao(db: Session, exportacao_id: int):
    return db.query(Exportacao).filter(Exportacao.id == exportacao_id).first()

def create_exportacao(db: Session, exportacao: ExportacaoCreate):
    db_exportacao = Exportacao(
        categoria = exportacao.categoria,
        pais_destino = exportacao.pais_destino,
        quantidade= exportacao.quantidade,
        valor= exportacao.valor,
        ano= exportacao.ano
    )
    db.add(db_exportacao)
    db.commit()
    db.refresh(db_exportacao)
    return db_exportacao

def update_exportacao(db: Session, exportacao_id: int, exportacao: ExportacaoCreate):
    db_exportacao = db.query(Exportacao).filter(Exportacao.id == exportacao_id).first()
    if db_exportacao:
        db_exportacao.categoria = exportacao.categoria
        db_exportacao.pais_destino = exportacao.pais_destino
        db_exportacao.quantidade = exportacao.quantidade
        db_exportacao.valor = exportacao.valor
        db_exportacao.ano = exportacao.ano
        db.commit()
        db.refresh(db_exportacao)
    return db_exportacao

def delete_exportacao(db: Session, exportacao_id: int):
    db_exportacao = db.query(Exportacao).filter(Exportacao.id == exportacao_id).first()
    if db_exportacao:
        db.delete(db_exportacao)
        db.commit()
