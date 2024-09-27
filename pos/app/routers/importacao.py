from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/importacao",
    tags=["Importação"]   
)

@router.get("/", response_model=list[schemas.Importacao])
def get_importacoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_importacoes(db=db, skip=skip, limit=limit)

@router.get("/ano/{ano}", response_model=list[schemas.Importacao])
def get_importacao_por_ano(ano: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    importacoes = crud.get_importacao_by_ano(db=db, ano=ano, skip=skip, limit=limit)
    if not importacoes:
        raise HTTPException(status_code=404, detail="Nenhuma produção encontrada para este ano")
    return importacoes

@router.post("/", response_model=schemas.Importacao)
def create_importacao(importacao: schemas.ImportacaoCreate, db: Session = Depends(get_db)):
    return crud.create_importacao(db=db, importacao=importacao)

@router.put("/{importacao_id}", response_model=schemas.Importacao)
def update_importacao(importacao_id: int, importacao: schemas.ImportacaoCreate, db: Session = Depends(get_db)):
    db_importacao = crud.get_importacao(db=db, importacao_id=importacao_id)
    if db_importacao is None:
        raise HTTPException(status_code=404, detail="Produção não encontrada")
    return crud.update_importacao(db=db, importacao_id=importacao_id, importacao=importacao)

@router.delete("/{importacao_id}")
def delete_importacao(importacao_id: int, db: Session = Depends(get_db)):
    db_importacao = crud.get_importacao(db=db, importacao_id=importacao_id)
    if db_importacao is None:
        raise HTTPException(status_code=404, detail="Produção não encontrada")
    crud.delete_importacao(db=db, importacao_id=importacao_id)
    return {"message": "Importação deletada com sucesso"}
