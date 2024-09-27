from sqlalchemy.orm import Session
from app.models.importacao import Importacao
from app.schemas.importacao import ImportacaoCreate

def get_importacoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Importacao).offset(skip).limit(limit).all()

def get_importacao_by_ano(db: Session, ano: int, skip: int = 0, limit: int = 10):
    return db.query(Importacao).filter(Importacao.ano == ano).offset(skip).limit(limit).all()

def get_importacao(db: Session, importacao_id: int):
    return db.query(Importacao).filter(Importacao.id == importacao_id).first()

def create_importacao(db: Session, importacao: ImportacaoCreate):
    db_importacao = Importacao(
        categoria = importacao.categoria,
        pais_origem = importacao.pais_origem,
        quantidade= importacao.quantidade,
        valor= importacao.valor,
        ano= importacao.ano
    )
    db.add(db_importacao)
    db.commit()
    db.refresh(db_importacao)
    return db_importacao

def update_importacao(db: Session, importacao_id: int, importacao: ImportacaoCreate):
    db_importacao = db.query(Importacao).filter(Importacao.id == importacao_id).first()
    if db_importacao:
        db_importacao.categoria = importacao.categoria
        db_importacao.pais_origem = importacao.pais_origem
        db_importacao.quantidade = importacao.quantidade
        db_importacao.valor = importacao.valor
        db_importacao.ano = importacao.ano
        db.commit()
        db.refresh(db_importacao)
    return db_importacao

def delete_importacao(db: Session, importacao_id: int):
    db_importacao = db.query(Importacao).filter(Importacao.id == importacao_id).first()
    if db_importacao:
        db.delete(db_importacao)
        db.commit()
