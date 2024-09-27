from sqlalchemy.orm import Session
from app.models.comercializacao import Comercializacao
from app.schemas.comercializacao import ComercializacaoCreate

def get_comercializacoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Comercializacao).offset(skip).limit(limit).all()

def get_comercializacao_by_ano(db: Session, ano: int, skip: int = 0, limit: int = 10):
    return db.query(Comercializacao).filter(Comercializacao.ano == ano).offset(skip).limit(limit).all()

def get_comercializacao(db: Session, comercializacao_id: int):
    return db.query(Comercializacao).filter(Comercializacao.id == comercializacao_id).first()

def create_comercializacao(db: Session, comercializacao: ComercializacaoCreate):
    db_comercializacao = Comercializacao(
        categoria_produto=comercializacao.categoria_produto,
        descricao_produto=comercializacao.descricao_produto,
        quantidade=comercializacao.quantidade,
        ano=comercializacao.ano
    )
    db.add(db_comercializacao)
    db.commit()
    db.refresh(db_comercializacao)
    return db_comercializacao

def update_comercializacao(db: Session, comercializacao_id: int, producao: ComercializacaoCreate):
    db_comercializacao = db.query(Comercializacao).filter(Comercializacao.id == comercializacao_id).first()
    if db_comercializacao:
        db_comercializacao.categoria_produto = producao.categoria_produto
        db_comercializacao.descricao_produto = producao.descricao_produto
        db_comercializacao.quantidade = producao.quantidade
        db_comercializacao.ano = producao.ano
        db.commit()
        db.refresh(db_comercializacao)
    return db_comercializacao

def delete_comercializacao(db: Session, comercializacao_id: int):
    db_comercializacao = db.query(Comercializacao).filter(Comercializacao.id == comercializacao_id).first()
    if db_comercializacao:
        db.delete(db_comercializacao)
        db.commit()
