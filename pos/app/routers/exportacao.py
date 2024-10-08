from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/exportacao",
    tags=["Exportação"]   
)

@router.get("/", response_model=list[schemas.Exportacao])
def get_exportacoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_exportacoes(db=db, skip=skip, limit=limit)

@router.get("/ano/{ano}", response_model=list[schemas.Exportacao])
def get_exportacao_por_ano(ano: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    exportacoes = crud.get_exportacao_by_ano(db=db, ano=ano, skip=skip, limit=limit)
    if not exportacoes:
        raise HTTPException(status_code=404, detail="Nenhuma produção encontrada para este ano")
    return exportacoes

@router.post("/", response_model=schemas.Exportacao)
def create_exportacao(exportacao: schemas.ExportacaoCreate, db: Session = Depends(get_db)):
    return crud.create_exportacao(db=db, exportacao=exportacao)

@router.put("/{exportacao_id}", response_model=schemas.Exportacao)
def update_exportacao(exportacao_id: int, exportacao: schemas.ExportacaoCreate, db: Session = Depends(get_db)):
    db_exportacao = crud.get_exportacao(db=db, exportacao=exportacao_id)
    if db_exportacao is None:
        raise HTTPException(status_code=404, detail="Produção não encontrada")
    return crud.update_exportacao(db=db, exportacao_id=exportacao_id, exportacao=exportacao)

@router.delete("/{exportacao_id}")
def delete_exportacao(exportacao_id: int, db: Session = Depends(get_db)):
    db_exportacao = crud.get_exportacao(db=db, exportacao_id=exportacao_id)
    if db_exportacao is None:
        raise HTTPException(status_code=404, detail="Produção não encontrada")
    crud.delete_exportacao(db=db, exportacao_id=exportacao_id)
    return {"message": "Produção deletada com sucesso"}
