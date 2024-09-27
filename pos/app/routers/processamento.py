from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db


router = APIRouter(
    prefix="/processamento",
    tags=["Processamento"]   
)

@router.get("/", response_model=list[schemas.Cultivo])
def get_processamentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_processamentos(db=db, skip=skip, limit=limit)

@router.get("/ano/{ano}", response_model=list[schemas.Cultivo])
def get_processamento_por_ano(ano: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    processamentos = crud.get_processamento_by_ano(db=db, ano=ano, skip=skip, limit=limit)
    if not processamentos:
        raise HTTPException(status_code=404, detail="Nenhum processamento encontrado para este ano")
    return processamentos

@router.post("/", response_model=schemas.Cultivo)
def create_processamento(cultivo: schemas.CultivoCreate, db: Session = Depends(get_db)):
    return crud.create_processamento(db=db, cultivo=cultivo)

@router.put("/{cultivo_id}", response_model=schemas.Cultivo)
def update_processamento(cultivo_id: int, cultivo: schemas.CultivoCreate, db: Session = Depends(get_db)):
    db_processamento= crud.get_processamento(db=db, cultivo_id=cultivo_id)
    if db_processamento is None:
        raise HTTPException(status_code=404, detail="Processamento não encontrada")
    return crud.update_processamento(db=db, cultivo_id=cultivo_id, cultivo=cultivo)

@router.delete("/{cultivo_id}")
def delete_processamento(cultivo_id: int, db: Session = Depends(get_db)):
    db_processamento = crud.get_processamento(db=db, cultivo_id=cultivo_id)
    if db_processamento is None:
        raise HTTPException(status_code=404, detail="Processamento não encontrada")
    crud.delete_processamento(db=db, cultivo_id=cultivo_id)
    return {"message": "Processamento deletada com sucesso"}
