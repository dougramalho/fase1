from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/producao",
    tags=["Produção"]   
)

@router.get("/", response_model=list[schemas.Producao])
def get_producoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_producoes(db=db, skip=skip, limit=limit)

@router.get("/ano/{ano}", response_model=list[schemas.Producao])
def get_producao_por_ano(ano: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    producoes = crud.get_producao_by_ano(db=db, ano=ano, skip=skip, limit=limit)
    if not producoes:
        raise HTTPException(status_code=404, detail="Nenhuma produção encontrada para este ano")
    return producoes

@router.post("/", response_model=schemas.Producao)
def create_producao(producao: schemas.ProducaoCreate, db: Session = Depends(get_db)):
    return crud.create_producao(db=db, producao=producao)

@router.put("/{producao_id}", response_model=schemas.Producao)
def update_producao(producao_id: int, producao: schemas.ProducaoCreate, db: Session = Depends(get_db)):
    db_producao = crud.get_producao(db=db, producao_id=producao_id)
    if db_producao is None:
        raise HTTPException(status_code=404, detail="Produção não encontrada")
    return crud.update_producao(db=db, producao_id=producao_id, producao=producao)

@router.delete("/{producao_id}")
def delete_producao(producao_id: int, db: Session = Depends(get_db)):
    db_producao = crud.get_producao(db=db, producao_id=producao_id)
    if db_producao is None:
        raise HTTPException(status_code=404, detail="Produção não encontrada")
    crud.delete_producao(db=db, producao_id=producao_id)
    return {"message": "Produção deletada com sucesso"}
