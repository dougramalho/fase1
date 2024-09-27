from sqlalchemy.orm import Session
from app.models.producao import Producao
from app.schemas.producao import ProducaoCreate

def get_producoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Producao).offset(skip).limit(limit).all()

def get_producao_by_ano(db: Session, ano: int, skip: int = 0, limit: int = 10):
    return db.query(Producao).filter(Producao.ano == ano).offset(skip).limit(limit).all()

def get_producao(db: Session, producao_id: int):
    return db.query(Producao).filter(Producao.id == producao_id).first()

def create_producao(db: Session, producao: ProducaoCreate):
    db_producao = Producao(
        categoria_produto=producao.categoria_produto,
        descricao_produto=producao.descricao_produto,
        quantidade=producao.quantidade,
        ano=producao.ano
    )
    db.add(db_producao)
    db.commit()
    db.refresh(db_producao)
    return db_producao

def update_producao(db: Session, producao_id: int, producao: ProducaoCreate):
    db_producao = db.query(Producao).filter(Producao.id == producao_id).first()
    if db_producao:
        db_producao.categoria_produto = producao.categoria_produto
        db_producao.descricao_produto = producao.descricao_produto
        db_producao.quantidade = producao.quantidade
        db_producao.ano = producao.ano
        db.commit()
        db.refresh(db_producao)
    return db_producao

def delete_producao(db: Session, producao_id: int):
    db_producao = db.query(Producao).filter(Producao.id == producao_id).first()
    if db_producao:
        db.delete(db_producao)
        db.commit()
